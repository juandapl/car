from objects import *



def generateFYP(fyp, degree):
    print("here")
    queue = []
    allClassesTaken = []

    for term in fyp.terms:
        for course in term.courses:
            allClassesTaken.append(course.course_id)

    print(allClassesTaken)

    # capture the first semester to modify
    targetSemester = None
    for term in fyp.terms:
        if term.credits == 0 and (term.semester[0:2] == "fa" or term.semester[0:2] == "sp"):
            targetSemester = term.semester
            break
    

    while(targetSemester):
        # search in the degree requirements what the next courses possible to take are, put them in a queue
        for requirement in degree.requirements:
            canTake = True
            if not (requirement.name in allClassesTaken):
                for prereq in requirement.prereqs:
                    canTake = canTake and (prereq in allClassesTaken)
                    if not (prereq in allClassesTaken):
                        queue.append(prereq)
                if canTake == True:
                    queue.append(requirement.name)
            
        # add these to the fyp for that semester
        for term in fyp.terms:
            if term.semester == targetSemester:
                while term.credits <= 16 and not len(queue) == 0:
                    added_course = queue.pop(0)
                    term.addCourse(Course("TBD", added_course, "TBD", "TBD", "TBD", "TBD", "TBD"))
                    allClassesTaken.append(added_course)
        
        if len(queue) == 0:
            break

        targetSemester = None
        for term in fyp.terms:
            if term.credits == 0 and (term.semester[0:2] == "fa" or term.semester[0:2] == "sp"):
                targetSemester = term.semester
                break  
    
    return fyp

# f = FourYearPlan("2020")
# deg = Degree("ECON")

# f = generateFYP(f, deg)

# for term in f.terms:
#     print(term.semester)
#     for course in term.courses:
#         print(course.course_id)