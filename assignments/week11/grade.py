"""
Create a grade processing system with the following requirements:

A global variable passing_grade = 50

(1) A function input_students(num_students) that:

- Creates and returns a list of dictionaries
- Each dictionary contains: {'name': str, 'scores': [list of 3 scores]}

(2) A function calculate_averages(students) that:

- Uses nested loops to calculate each student's average
- Adds an 'average' key to each student dictionary
- Modifies the original list (demonstrate list mutability)

(3) A function display_results(students) that:

- Loops through students
- Uses the global passing_grade to determine pass/fail
- Prints each student's name, average, and status (PASS/FAIL)
"""

global passing_grade
passing_grade = 50

def input_student():
    student=[
            {"name":"A","score":[25,30,35]}
            ,{"name":"B","score":[50,25,70]}
            ,{"name":"C","score":[87,88,25]}
             ]
    return student

def calculate_averages(students):
    
    for student in students:
        sum = 0
        for score in student["score"]:
            sum = sum + score
        student["average"]= sum/len(student["score"])

    return students


def display_results(students):
    print("student Detaild:")
    for student in students:
        print(f"Name:{student['name']}")
        print(f"Average:{student['average']}")
        if student["average"] > passing_grade:
            print("Status:Pass")
        else:
            print("Status:Fail")

students = input_student()
students = calculate_averages(students)
students = display_results(students)
    