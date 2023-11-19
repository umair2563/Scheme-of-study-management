class Course:
    def __init__(self, course_code, course_name, max_students):
        self.course_code = course_code
        self.course_name = course_name
        self.max_students = max_students
        self.enrolled_students = []

    def add_student(self, student):
        if len(self.enrolled_students) < self.max_students:
            self.enrolled_students.append(student)
            print(f"{student.name} enrolled in {self.course_name}")
        else:
            print(f"Cannot enroll {student.name}. Maximum students reached for {self.course_name}")

    def list_enrolled_students(self):
        print(f"Students enrolled in {self.course_name}:")
        for student in self.enrolled_students:
            print(student.name)

class Student:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name

class SchemeOfStudy:
    def __init__(self):
        self.courses = {}

    def add_course(self, course_code, course_name, max_students):
        if course_code not in self.courses:
            self.courses[course_code] = Course(course_code, course_name, max_students)
            print(f"Course {course_code} - {course_name} added.")
        else:
            print(f"Course {course_code} already exists.")

    def enroll_student(self, student_id, course_code):
        if course_code in self.courses:
            student = Student(student_id, f"Student {student_id}")
            self.courses[course_code].add_student(student)
        else:
            print(f"Course {course_code} does not exist.")

    def list_enrolled_students(self, course_code):
        if course_code in self.courses:
            self.courses[course_code].list_enrolled_students()
        else:
            print(f"Course {course_code} does not exist.")

# Creating Scheme of Study
scheme_of_study = SchemeOfStudy()

# Adding Courses
scheme_of_study.add_course("SE101", "Introduction to Software Engineering", 3)
scheme_of_study.add_course("STA101", "Statistics", 2)

# Enrolling Students
scheme_of_study.enroll_student(2001, "SE101")
scheme_of_study.enroll_student(2002, "SE101")
scheme_of_study.enroll_student(2003, "SE101")
scheme_of_study.enroll_student(2004, "STA101")
scheme_of_study.enroll_student(2005, "STA101")

# Listing Enrolled Students in a Course
scheme_of_study.list_enrolled_students("SE101")
scheme_of_study.list_enrolled_students("STA101")


