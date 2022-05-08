from objects import *

def generateFYP(fyp, degrees):
    queue = []
    # capture the first semester to modify
    targetSemester = None
    for term in fyp.terms:
        if term.credits == 0 and (term.semester[0:2] == "fa" or term.semester[0:2] == "sp"):
            targetSemester = term.semester

    if targetSemester:
        pass
    # search in the degree requirements what the next courses possible to take are, put them in a queue

    # add these to the fyp for that semester

    # continue iterating