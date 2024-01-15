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