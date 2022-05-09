
class Course:
    def __init__(self, name, course_id, reg_number, section, professor, location, semester):
        self.name = name
        self.course_id = course_id
        self.reg_number = reg_number
        self.section = section
        self.professor = professor
        self.location = location
        self.semester = semester
        self.credits = 4
    def as_dict(self):
        return {
            "name": self.name,
            "courseID": self.course_id
        }


class Term:
    def __init__(self, semester, location="Abu Dhabi"):
        self.courses = []
        self.credits = 0
        self.location = location
        self.semester = semester

    def as_dict(self):
        return {
            "courses": [v.as_dict() for v in self.courses],
            "semester": self.semester
        }

    def addCourse(self, Course):
        if not self.credits + Course.credits > 20 and (self.semester[0:2] == "fa" or self.semester[0:2] == "sp"):
            self.courses.append(Course)
            self.credits += Course.credits
            return "success"
        if not self.credits + Course.credits > 4 and (self.semester[0:2] == "ja" or self.semester[0:2] == "su"):
            self.courses.append(Course)
            self.credits += Course.credits
            return "success"
        return "failure"


class FourYearPlan:
    def __init__(self, startYear):
        startYear = int(startYear)
        self.terms = []
        self.degreesPursuing = []
        self.startYear = startYear
        semesters = ["ja", "sp", "su", "fa"]
        #append first fall
        self.terms.append(Term(("fa"+str(startYear))))
        for i in range(1,4):
            for sem in semesters: 
                self.terms.append(Term((sem+str(startYear+i))))
        #append last spring and jan
        self.terms.append(Term(("ja"+str(startYear+4))))
        self.terms.append(Term(("sp"+str(startYear+4))))
    def addCourse(self, course):
        for term in self.terms:
            if term.semester == course.semester:
                if term.addCourse(course) == "success":
                    return "success"
        return "failure"


class Student:
    def __init__(self, name, email, current_plan):
        self.name = name
        self.email = email
        self.current_plan = current_plan

class Degree:
    def __init__(self, name):
        self.name = name
        self.requirements = [Requirement("CDAD"), Requirement("CCEA"), Requirement("CSTS"), Requirement("CADT"), Requirement("CCOL"), Requirement("CCOL")]
    def addRequirement(self, requirement):
        self.requirements.append(requirement)
    def as_dict(self):
        return {
            "requirements": [v.as_dict() for v in self.requirements],
            "name": self.name
        }


class Requirement():
    def __init__(self, course_id):
        self.name = course_id
        self.prereqs = []
    def addPreReq(self, requirement):
        self.prereqs.append(requirement)
    def as_dict(self):
        return {
            "prereqs": self.prereqs,
            "course_id": self.name
        }

