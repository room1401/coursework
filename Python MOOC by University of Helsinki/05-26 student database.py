'''
First write a function named add_student, which adds a new student to the 
database. Also write a preliminary version of the function print_student, 
which prints out the information of a single student.

Please write a function named add_course, which adds a completed course to 
the information of a specific student in the database. The course data is a 
tuple consisting of the name of the course and the grade.

Courses with grade 0 should be ignored when adding course information. 
Additionally, if the course is already in the database in that specific 
student's information, the grade recorded in the database should never be 
lowered if the course is repeated.

Please write a function named summary, which prints out a summary based on 
all the information stored in the database.
'''

# Write your solution here
def add_student(db, name):
    db[name] = dict()

def add_course(db, name, info):
    course, grade = info
    if grade:
        db[name][course] = max(db[name].get(course, 0), grade)

def print_student(db, name):
    if name not in db:
        print(f"{name}: no such person in the database")
    else:
        print(f"{name}:")
        record = db[name]
        if not record:
            print(" no completed courses")
        else:
            print(f" {len(record)} completed courses:")
            total = 0
            for course, grade in record.items():
                total += grade
                print(f"  {course} {grade}")
            
            print(f" average grade {total / len(record)}")

def summary(db):
    most, most_id = 0, ""
    best, best_id = 0, ""
    for person, record in db.items():
        ccount = len(record)
        if ccount > most:
            most, most_id = ccount, person
        
        avg = sum(x for x in record.values()) / ccount
        if avg > best:
            best, best_id = avg, person
    
    print("students", len(db))
    print(f"most courses completed {most} {most_id}")
    print(f"best average grade {best} {best_id}")
