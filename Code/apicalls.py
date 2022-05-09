
import requests
from datetime import datetime, timedelta
import calendar


base_url = "https://schedge.a1liu.com/"
semester = "sp"
year = "2022"
school = "UH"

allsubjects = requests.get(base_url+"subjects")
abu_dhabi_subjects = allsubjects.json()[school]

def get_all_subjects(year,semester,school,subject):
    abu_dhabi_courses = requests.get("https://schedge.a1liu.com/"+year+"/"+semester+"/"+school+"/"+subject).json()
    return abu_dhabi_courses


def subject_search(year,semester,school,subject):
    return requests.get("https://schedge.a1liu.com/"+year+"/"+semester+"/"+school+"/"+subject+"/").json()

def get_a_section(year,semester,classID):
    return requests.get("https://schedge.a1liu.com/"+year+"/"+semester+"/"+classID+"/").json()

def get_course_id_from_course_name(year,semester, school, name):
    query = {
        'query' : name,
        'school' : school,
    }
    results = requests.get("https://schedge.a1liu.com/"+year+"/"+semester+"/search/", params=query).json()
    newCourse = results[0]
    ret = newCourse['subjectCode']['code']+"-"+newCourse['subjectCode']['school']+" "+newCourse["deptCourseId"]
    print(ret)
    return ret

# utility functions to deal with meeting patterns
def getMeetingDays(section):
    res = ""
    if section["meetings"]:
        for m in section['meetings']:
            date_time_str = m['beginDate']
            date_time_obj = datetime.strptime(date_time_str, '%Y-%m-%d %H:%M:%S')
            res += date_time_obj.strftime('%A') + " "
        return res
    return "TBD"

def getMeetingTimes(section):
    if section["meetings"]:
        for m in section['meetings']:
            date_time_str = m['beginDate']
            date_time_obj = datetime.strptime(date_time_str, '%Y-%m-%d %H:%M:%S')
            init_time = date_time_obj.time()
            final_time = date_time_obj + timedelta(minutes= m['minutesDuration'])
        time = init_time.strftime("%H:%M") +"-"+ final_time.strftime("%H:%M")
        return time
    return "TBD"

