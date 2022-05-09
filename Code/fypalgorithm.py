from objects import *
import pickle


def generateFYP(fyp, degree):
    print("here")
    queue = []
    allClassesTaken = []
    allClassesAssigned = []

    for term in fyp.terms:
        for course in term.courses:
            if course.course_id[0:4] == "CCOL" or course.course_id[0:4] == "CSTS" or course.course_id[0:4] == "CDAD" or course.course_id[0:4] == "CCEA" or course.course_id[0:4] == "CADT" or course.course_id[0:4] == "WRIT":
                allClassesTaken.append(course.course_id[0:4])
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
            if (not (requirement.name in allClassesTaken)) and (not (requirement.name in allClassesAssigned)):
                for prereq in requirement.prereqs:
                    canTake = canTake and (prereq in allClassesTaken)
                    if not (prereq in allClassesTaken) and (not (prereq in allClassesAssigned)):
                        queue.append(prereq)
                        allClassesAssigned.append(prereq)
                if canTake == True:
                    queue.append(requirement.name)
                    allClassesAssigned.append(requirement.name)
            
        # add these to the fyp for that semester
        for term in fyp.terms:
            if term.semester == targetSemester:
                while term.credits <= 12 and not len(queue) == 0:
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



# with open('code/majors.pkl', 'rb') as f:
#     majors = pickle.load(f)

# with open('code/fyp.pkl', 'rb') as f:
#     fyp = pickle.load(f)


# current_major = "Computer Science"

# for maj in majors:
#     if maj.name == current_major:
#         fyp = generateFYP(fyp, maj)
#         for term in fyp.terms:
#             for course in term.courses:
#                 print(course.course_id)
#             print("-")