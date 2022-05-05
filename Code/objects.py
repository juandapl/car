from tracemalloc import start


class Course:
    def __init__(self, course_id, section, professor, location, semester):
        self.course_id = course_id
        self.section = section
        self.professor = professor
        self.location = location
        self.semester = semester

class Term:
    def __init__(self, semester, location="Abu Dhabi"):
        self.courses = []
        self.credits = 0
        self.location = location
        self.semester = semester
    def addCourse(self, Course):
        if not self.credits + Course.credits > 20:
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
        semesters = ["ja," "sp", "su", "fa"]
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
        self.requirements = []
    def addRequirement(self, requirement):
        self.requirements.append(requirement)

class Requirement(Degree):
    def __init__(self, name, course_id):
        super(self, name)
        self.course_id = course_id