import requests
import base64
import json
from flask import Flask, request, redirect, g, render_template, session
import requests
from urllib.parse import quote
from apicalls import *
from objects import *


#firebase authentication
import pyrebase

firebaseConfig = {'apiKey': "AIzaSyAo0cMHeRTyfby4U3wgiesLi3Zd3w7AUkE",
  'authDomain': "car-se.firebaseapp.com",
  'databaseURL': "https://car-se-default-rtdb.firebaseio.com",
  'projectId': "car-se",
  'storageBucket': "car-se.appspot.com",
  'messagingSenderId': "507983665956",
  'appId': "1:507983665956:web:ae65fcf8220ebe14cd31b1",
  'measurementId': "G-JHG5FT48TX"}

firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()

#login on terminal
email = input("Enter email address")
password = input("Enter password")
auth.sign_in_with_email_and_password(email,password)


app = Flask(__name__)

# change secret key
app.secret_key = 'BAD_SECRET_KEY'

@app.route("/")
def initialise():
    if not session['user']:
        return redirect("/login")
    if not session['fyp']:
        session['fyp'] = FourYearPlan()
    return render_template("index.html")

@app.route("/search")
def courseSearch():
    search_results = []
    departments = (v["name"] for v in abu_dhabi_subjects.values())
    return render_template("courseSearch.html", all_departments = departments)

@app.route("/coursesearchresults", methods = ['POST', 'GET'])
def serveResults():
    if request.method == "POST":
        apiArguments = request.form
        departments = [v["name"] for v in abu_dhabi_subjects.values()]
        position = departments.index(apiArguments["department"])
        subject_code = list(abu_dhabi_subjects.keys())[position]
        search_results =  subject_search(apiArguments["year"], apiArguments["sem"], "UH", subject_code)
        print(search_results, subject_code)
        # courseList = (subject["name"] for subject in search_results)
        return render_template("result.html", search_results = search_results)

@app.route("/addCourse", methods=["GET", "POST"])
def addCourse():
    if request.method == "POST":
        newCourse = request.form
        if session['fyp'].addCourse(Course(newCourse["course_id"], newCourse["section"], newCourse["professor"], newCourse["location"], newCourse["semester"])) == "success":
            return "success"
        return "failure"
