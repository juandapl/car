#API Documentation

#System Description
CAR: Course Analysis and Registration is a web app written in Flask that interacts with Firebase and the Albert API to aid students in their college course planning.

#Modules
- apicalls.py: a module of functions that interact with the Albert API and return results for course search and course lookup by registration number in JSON format. This module also includes utility functions to obtain a course's meeting patterns from the API response.
- objects.py: a module containing how four year plans, semesters, courses, and sets of degree requirements are structured during processing.
- fypalgorithm.py: a module containing the algorithm to suggest four year plans, which returns FourYearPlan objects.
- app.py: a Flask app containing all server routes and responses.

#Scripts
Most of the user interaction with the server is done through AJAX embedded in the frontend pages' scripts.
- addtoplan.js: contains an AJAX script to obtain a course registration number from the Course Search module, send it to the /addCourse route in the server, and add the course to the current session's four-year plan.
- search.js: contains an AJAX script that sends a search query to the server, retrieves a rendered HTML template of search results, and updates the frontend page.

