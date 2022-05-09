import requests
import base64
import json
from flask import Flask, request, redirect, g, render_template, session, url_for
import requests
from urllib.parse import quote
from apicalls import *
from objects import *
from secret import *
import pyrebase
from fypalgorithm import *
from degreeprogressalgorithm import *
import pickle

app = Flask(__name__)
app.secret_key = secret_key


firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()
db = firebase.database()

fyp = FourYearPlan("2020")
majors = [Degree("Undecided")]
abu_dhabi_courses = []
current_major = "Undecided"

print("Getting all subject data")

try:
    with open('majors.pkl', 'rb') as f:
        majors = pickle.load(f)

    with open('fyp.pkl', 'rb') as f:
        fyp = pickle.load(f)

    with open('courses.pkl', 'rb') as f:
        all_abu_dhabi_course_codes = pickle.load(f)
except:
    pass

print("Initialisation done")



@app.route("/")
def initialise():
    session['name'] = "hi."
    try:
        if session['user']:
            return redirect('/main')
    except:
        pass
    return render_template("login.html")

@app.route("/login", methods = ['GET', 'POST'])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form['password']
        try:
            user = auth.sign_in_with_email_and_password(email,password)
            session['user'] = user['idToken']
            session['name'] = email
        except:
            return redirect("/")
        return redirect("/main")

@app.route("/main")
def index():
    return render_template("main.html", currentMajor = current_major, majors = majors, name = session['name'])

@app.route("/search")
def courseSearch():
    search_results = []
    departments = (v["name"] for v in abu_dhabi_subjects.values())
    return render_template("courseSearch.html", all_departments = departments)

# retrieves ajax call from search.js - serves an html of results
@app.route("/coursesearchresults", methods = ['POST', 'GET'])
def serveResults():
    if request.method == "POST":
        apiArguments = request.form
        departments = [v["name"] for v in abu_dhabi_subjects.values()]
        position = departments.index(apiArguments["department"])
        subject_code = list(abu_dhabi_subjects.keys())[position]
        year = apiArguments["year"]
        if int(year) > 2022:
            year = ["2022"]
        search_results =  subject_search(year, apiArguments["sem"], "UH", subject_code)
        print("search done")
        # prepares meeting dates and times in a displayable format
        dateTimes = {}
        for result in search_results:
            for s in result['sections']:
                days = getMeetingDays(dict(s))
                times = getMeetingTimes(dict(s))
                dateTimes[s['registrationNumber']] = {"days" : days, "times" : times}

        return render_template("result.html", search_results = search_results, dateTimes = dateTimes)

# retrieves ajax call from addtoplan.js, returns success if successful, returns failure if trying to add a class after credit overload
@app.route("/addCourse", methods=["GET", "POST"])
def addCourse():
    if request.method == "POST":
        form = request.form
        newCourse = get_a_section(form['year'],form['sem'],form['reg'])
        course_id = get_course_id_from_course_name(form['year'],form['sem'], "UH", newCourse["name"])
        print(course_id)
        if fyp.addCourse(Course(newCourse["name"], course_id, form['reg'], newCourse["code"], [v for v in newCourse["instructors"]], newCourse["location"], form["sem"]+form["year"])) == "success":
            return redirect("/fyp", code=302)
        return "failure"

@app.route("/removeCourse", methods=["GET", "POST"])
def removeCourse():
    if request.method == "POST":
        form = request.form
        reg = form['reg']
        for term in fyp.terms:
            for c in term.courses:
                if c.reg_number == reg:
                    term.courses.remove(c)
                    term.credits -= 4
                    break
                break
        return "success"

@app.route("/fyp")
def fouryearplanpage():
    return render_template("fouryear.html", terms = [v.as_dict() for v in fyp.terms])

@app.route("/admin")
def adminConsole():
    return render_template("dpAdmin.html", majors = majors, all_codes = all_abu_dhabi_course_codes) 

@app.route("/addMajor", methods=["GET", "POST"])
def addDegree():
    if request.method == "POST":
        name = request.form['name']
        majors.append(Degree(name))
        return "success"

@app.route("/addClass", methods=["GET", "POST"])
def addReq():
    if request.method == "POST":
        name = request.form['name']
        if not name in all_abu_dhabi_course_codes:
            return "fail."
        major = request.form['major']
        for maj in majors:
            if maj.name == major:
                maj.addRequirement(Requirement(name))
                break
        return "success"

@app.route("/deleteReq", methods=["GET", "POST"])
def deleteReq():
    if request.method == "POST":
        name = request.form['name']
        major = request.form['major']
        for maj in majors:
            if maj.name == major:
                for c in maj.requirements:
                    if c.name == name:
                        maj.requirements.remove(c)
                        break
                break
        return "success"

@app.route("/addPreReq", methods=["GET", "POST"])
def addPR():
    if request.method == "POST":
        name = request.form['name']
        if not name in all_abu_dhabi_course_codes:
            return "fail."
        cl = request.form['class']
        major = request.form['major']
        for maj in majors:
            if maj.name == major:
                for c in maj.requirements:
                    if c.name == cl:
                        c.addPreReq(name)
                break
        return "success"

@app.route("/changeMajor", methods=["GET", "POST"])
def changeMajor():
    global current_major
    if request.method == "POST":
        newMajor = request.form['maj']
        current_major = newMajor        
        return "success"

@app.route("/generateFYP", methods=["GET", "POST"])
def generatePlan():
    global fyp
    for maj in majors:
        if maj.name == current_major:
            
            fyp = generateFYP(fyp, maj)
            for term in fyp.terms:
                for course in term.courses:
                    print(course.name)
            break
    return "success"

@app.route("/degreeProgress")
def degreeProgress():
    for maj in majors:
        if maj.name == current_major:
            return render_template("degreeProgress.html", major = current_major, r = getDegreeProgress(fyp, maj))

@app.route("/saveSystem")
def saveAll():
    with open('majors.pkl', 'wb') as f:
        pickle.dump(majors, f)
    with open('fyp.pkl', 'wb') as f:
        pickle.dump(fyp, f)
    with open('courses.pkl', 'wb') as f:
        pickle.dump(all_abu_dhabi_course_codes, f)
    print("saving done")
    return render_template("dpAdmin.html", majors = majors)
