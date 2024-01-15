from course import Course
from student import Student
from schemeofstudy import SchemeOfStudy

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