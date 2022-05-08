import requests
import base64
import json
from flask import Flask, request, redirect, g, render_template, session
import requests
from urllib.parse import quote
from apicalls import *
from objects import *
from secret import *
import pyrebase

app = Flask(__name__)
app.secret_key = secret_key


firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()
db = firebase.database()

fyp = FourYearPlan("2020")

@app.route("/")
def initialise():
    try:
        if session['user']:
            return redirect('/main')
    except:
        pass
    return render_template("loginpage.html")

@app.route("/login", methods = ['GET', 'POST'])
def login():
    email = request.form["email"]
    password = request.form['password']
    try:
        user = auth.sign_in_with_email_and_password(email,password)
        session['user'] = user['idToken']
    except:
        return redirect("/")
    return redirect("/main")

@app.route("/main")
def index():
    return render_template("main.html")

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
        search_results =  subject_search(apiArguments["year"], apiArguments["sem"], "UH", subject_code)
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
            return "success"
        return "failure"

@app.route("/fyp")
def fouryearplanpage():
    return render_template("fouryear.html", terms = [v.as_dict() for v in fyp.terms])

@app.route("/generatefyp")
def generatefyp():
    return render_template("fypreport.html", fyp = session['fyp'])
