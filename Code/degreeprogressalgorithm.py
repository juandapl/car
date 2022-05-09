from objects import *

def getDegreeProgress(fyp, deg):
    current_semester = "sp2022"
    allClassesTaken = []
    done = []
    left = []

    for term in fyp.terms:
        for course in term.courses:
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

    pct = (len(done)/len(left))*100


    return {
        'required' : allRequirements,
        'done' : done,
        'left' : left,
        'percentage': pct
    }

# f = FourYearPlan("2020")
# deg = Degree("ECON")

# r = degreeProgress(f, deg)
