from objects import *

def generateFYP(fyp, degrees):
    
    queue = []
    allClassesTaken = []

    for term in fyp.terms:
        for course in term.courses:
            allClassesTaken.append(course.course_id)
    
    # capture the first semester to modify
    targetSemester = None
    for term in fyp.terms:
        if term.credits == 0 and (term.semester[0:2] == "fa" or term.semester[0:2] == "sp"):
            targetSemester = term.semester
            break

    while(targetSemester):
        # search in the degree requirements what the next courses possible to take are, put them in a queue
        for degree in degrees:
            for requirement in degree.requirements:
                canTake = True
                for prereq in requirement.requirements:
                    canTake = canTake and (prereq in allClassesTaken) 
                if canTake == true:
                    queue.append(requirement)
            
        # add these to the fyp for that semester
        for term in fyp.terms:
            if term.semester == targetSemester:
            #some loop (TODO)
                added_course = queue.pop(0)
                targetSemester.addCourse(Course("", added_course, "TBD", "TBD", "TBD", "TBD"))
                allClassesTaken.append(added_course)
            
        targetSemester = None
        for term in fyp.terms:
            if term.credits == 0 and (term.semester[0:2] == "fa" or term.semester[0:2] == "sp"):
                targetSemester = term.semester
                break  
    
    return fyp
