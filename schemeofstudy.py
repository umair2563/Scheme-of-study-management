from course import Course
from student import Student

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
