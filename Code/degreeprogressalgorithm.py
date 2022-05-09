from objects import *

def getDegreeProgress(fyp, deg):
    current_semester = "sp2022"
    allClassesTaken = []
    done = []
    left = []

    for term in fyp.terms:
        for course in term.courses:
            if course.course_id[0:4] == "CCOL" or course.course_id[0:4] == "CSTS" or course.course_id[0:4] == "CDAD" or course.course_id[0:4] == "CCEA" or course.course_id[0:4] == "CADT" or course.course_id[0:4] == "WRIT":
                allClassesTaken.append(course.course_id[0:4])
            allClassesTaken.append(course.course_id)
        if current_semester == term.semester:
            break

    allRequirements = []
    for requirement in deg.requirements:
        allRequirements.append(requirement.name)
    
    for req in allRequirements:
        if (req in allClassesTaken):
            done.append(req)
        else:
            left.append(req)

    pct = (len(done)/len(allRequirements))*100


    return {
        'required' : allRequirements,
        'done' : done,
        'left' : left,
        'percentage': pct
    }

# f = FourYearPlan("2020")
# deg = Degree("ECON")

# r = degreeProgress(f, deg)
