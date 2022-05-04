
import requests
# import ratemyprofessor

base_url = "https://schedge.a1liu.com/"
semester = "sp"
year = "2022"
school = "UH"

allsubjects = requests.get(base_url+"subjects")
abu_dhabi_subjects = allsubjects.json()[school]

def get_all_subjects(year,semester,school):
    abu_dhabi_courses  = {}
    abu_dhabi_courses[subject] = requests.get("https://schedge.a1liu.com/"+year+"/"+semester+"/"+school+"/"+subject+"/").json()
    return abu_dhabi_courses

def subject_search(year,semester,school,subject):
    return requests.get("https://schedge.a1liu.com/"+year+"/"+semester+"/"+school+"/"+subject+"/").json()

def get_a_section(year,semester,classID):
    return requests.get("")



