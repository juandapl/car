
import requests
from datetime import datetime, timedelta
import calendar

# import ratemyprofessor

base_url = "https://schedge.a1liu.com/"
semester = "sp"
year = "2022"
school = "UH"

allsubjects = requests.get(base_url+"subjects")
abu_dhabi_subjects = allsubjects.json()[school]

# def get_all_subjects(year,semester,school):
#     abu_dhabi_courses  = {}
#     abu_dhabi_courses[subject] = requests.get("https://schedge.a1liu.com/"+year+"/"+semester+"/"+school+"/"+subject+"/").json()
#     return abu_dhabi_courses

def subject_search(year,semester,school,subject):
    return requests.get("https://schedge.a1liu.com/"+year+"/"+semester+"/"+school+"/"+subject+"/").json()

def get_a_section(year,semester,classID):
    return requests.get("https://schedge.a1liu.com/"+year+"/"+semester+"/"+classID+"/").json()

def getMeetingDays(section):
    res = ""
    if section["meetings"]:
        for m in section['meetings']:
            date_time_str = m['beginDate']
            date_time_obj = datetime.strptime(date_time_str, '%Y-%d-%m %H:%M:%S')
            res += date_time_obj.strftime('%A') + " "
        return res
    return "TBD"

def getMeetingTimes(section):
    if section["meetings"]:
        for m in section['meetings']:
            date_time_str = m['beginDate']
            date_time_obj = datetime.strptime(date_time_str, '%Y-%d-%m %H:%M:%S')
            init_time = date_time_obj.time()
            final_time = date_time_obj + timedelta(minutes= m['minutesDuration'])
        time = init_time.strftime("%H:%M") +"-"+ final_time.strftime("%H:%M")
        return time
    return "TBD"


