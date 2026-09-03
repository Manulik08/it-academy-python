print("Задание 1")
from statistics import mean
"""Разработайте класс Student, который хранит информацию о 
студенте: имя, список курсов и оценки. Реализуйте методы 
для расчета среднего балла и добавления новых курсов. 
Создайте группу студентов и найдите студента с лучшей 
успеваемостью 
Добавьте метод для вывода информации о незавершенных 
курсах 
Реализуйте функцию, которая формирует список отличников """

class Student:
    def __init__(self, name):
        self.name = name
        self.courses = []
        self.grades = []

    def add_course_grade(self, course, grade):
        self.courses.append(course)
        self.grades.append(grade)

    @property
    def average_score(self):
        if not self.grades:
            return 0
        return mean(self.grades)

    def incomplete_courses(self):
        incomplete_students = []
        for i, course in enumerate(self.courses):
            if self.grades[i] < 50:
                incomplete_students.append(course)
        return incomplete_students

    def __str__(self):
        return f"Student {self.name} - courses: {self.courses}, grades: {self.grades}"


student1 = Student("Patrik")
student1.add_course_grade("Math", 80)
student1.add_course_grade("Russian", 90)
student1.add_course_grade("Сhemistry", 75)

student2 = Student("Bob")
student2.add_course_grade("Literature", 60)
student2.add_course_grade("English", 55)
student2.add_course_grade("Biology", 30)

student3 = Student("Alex")
student3.add_course_grade("Сhemistry", 90)
student3.add_course_grade("Russian", 95)
student3.add_course_grade("Math", 75)

students = [student1, student2, student3]
best_student = max(students, key=lambda x: x.average_score)
print("Best student: ", best_student)

for student in students:
    incomplete_students = student.incomplete_courses()
    if incomplete_students:
        print(f"{student.name} has unfinished courses - {incomplete_students}")

def get_straight_students(students):
    return [x for x in students if x.average_score > 80]

straight_students = get_straight_students(students)
for student in straight_students:
    print("Straight student: ", student)











