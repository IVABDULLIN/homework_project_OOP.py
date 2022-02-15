class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}


    def give_rate_to_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course \
                in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'


    def average_rating_student(self, grades):
        list_1 = []
        list_2 = []
        for key, value in grades.items():
            list_1.append(key)
            list_2 += value
            self.grades = round(sum(list_2) / len(list_2), 1)
        return grades


    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Не корректные данные!')
            return
        return self.grades > other.grades


    def __str__(self):
        self.finished_courses = 'Введение в программирование'.join(self.finished_courses)
        intro = f'Информация о студентах:\nИмя: {self.name}\nФамилия: {self.surname}' \
                f'\nСредняя оценка за лекции: {self.grades}' \
                f'\nКурсы в процессе изучения: {self.courses_in_progress}' \
                f'\nЗавершенные курсы: {self.finished_courses}'
        return intro


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}


    def average_rating_lecturer(self, grades):
        new_list = []
        for number in grades.values():
            new_list += number
            self.grades = round(sum(new_list) / len(new_list), 1)
        return grades


    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print ('Не корректные данные!')
            return
        return self.grades < other.grades


    def __str__(self):
        what = f'Информация о лекторах:\nИмя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.grades}'
        return what


class Reviewer(Mentor):
    def give_rate_to_student(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course \
                in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


    def __str__(self):
        who = f'Информация о проверяющих:\nИмя: {self.name}\nФамилия: {self.surname}'
        return who


some_student = Student('Ruoy', 'Eman', 'male')
some_student.finished_courses += ['Введение в программирование']
some_student.courses_in_progress += ['Python']
some_student.courses_in_progress += ['Git']
some_student.grades = {}

new_student = Student('Erik', 'Goffman', 'male')
new_student.finished_courses += ['Введение в программирование']
new_student.courses_in_progress += ['Python']
new_student.courses_in_progress += ['Git']
new_student.grades = {}

some_lecturer = Lecturer('Nik', 'Norman')
some_lecturer.courses_attached += ['Введение в программирование']
some_lecturer.courses_attached += ['Python']
some_lecturer.courses_attached += ['Git']
some_lecturer.grades = some_lecturer.grades

new_lecturer = Lecturer('Miels', 'Bekstrem')
new_lecturer.courses_attached += ['Введение в программирование']
new_lecturer.courses_attached += ['Python']
new_lecturer.courses_attached += ['Git']
new_lecturer.grades = new_lecturer.grades


some_student.give_rate_to_lecturer(some_lecturer, 'Python', 9)
some_student.give_rate_to_lecturer(some_lecturer, 'Python', 10)
some_student.give_rate_to_lecturer(some_lecturer, 'Python', 10)

some_student.give_rate_to_lecturer(some_lecturer, 'Git', 9)
some_student.give_rate_to_lecturer(some_lecturer, 'Git', 10)
some_student.give_rate_to_lecturer(some_lecturer, 'Git', 10)


new_student.give_rate_to_lecturer(new_lecturer, 'Python', 9)
new_student.give_rate_to_lecturer(new_lecturer, 'Python', 9)
new_student.give_rate_to_lecturer(new_lecturer, 'Python', 10)

new_student.give_rate_to_lecturer(new_lecturer, 'Git', 9)
new_student.give_rate_to_lecturer(new_lecturer, 'Git', 10)
new_student.give_rate_to_lecturer(new_lecturer, 'Git', 10)


print(some_lecturer.grades)
print(new_lecturer.grades)

print()

some_reviewer = Reviewer('Tommi', 'Smith')
some_reviewer.courses_attached += ['Введение в программирование']
some_reviewer.courses_attached += ['Python']
some_reviewer.courses_attached += ['Git']

new_reviewer = Reviewer('Elton', 'Ivanov')
new_reviewer.courses_attached += ['Введение в программирование']
new_reviewer.courses_attached += ['Python']
new_reviewer.courses_attached += ['Git']


some_reviewer.give_rate_to_student(some_student, 'Python', 10)
some_reviewer.give_rate_to_student(some_student, 'Python', 9)
some_reviewer.give_rate_to_student(some_student, 'Python', 9)

some_reviewer.give_rate_to_student(some_student, 'Git', 10)
some_reviewer.give_rate_to_student(some_student, 'Git', 10)
some_reviewer.give_rate_to_student(some_student, 'Git', 9)


new_reviewer.give_rate_to_student(new_student, 'Python', 9)
new_reviewer.give_rate_to_student(new_student, 'Python', 9)
new_reviewer.give_rate_to_student(new_student, 'Python', 10)

new_reviewer.give_rate_to_student(new_student, 'Git', 10)
new_reviewer.give_rate_to_student(new_student, 'Git', 9)
new_reviewer.give_rate_to_student(new_student, 'Git', 9)


print(some_student.grades)
print(new_student.grades)

print()

print(some_reviewer)
print()
print(new_reviewer)
print()
some_lecturer.average_rating_lecturer(some_lecturer.grades)
print(some_lecturer)
print()
new_lecturer.average_rating_lecturer(new_lecturer.grades)
print(new_lecturer)
print()
some_student.average_rating_student(some_student.grades)
print(some_student)
print()
new_student.average_rating_student(new_student.grades)
print(new_student)
print()
print('Результат сравнения по студентам:', some_student.grades < new_student.grades)
print('Результат сравнения по лекторам:', some_lecturer.grades < new_lecturer.grades)
print()


some_student.grades = {'Python': [10, 9, 9], 'Git': [10, 10, 9]}
new_student.grades = {'Python': [9, 9, 10], 'Git': [10, 9, 9]}

main_course = 'Python'
list_student = [some_student.grades, new_student.grades]

def student(main_course, list_student):
    list_grades = []
    for grades in list_student:
        for key, value in grades.items():
            if main_course == key:
                for number in value:
                    list_grades.append(number)
                    average_for_students = round(sum(list_grades)/len(list_grades), 1)
    return average_for_students
print('Cредней оценка за домашние задания по курсу Python:', student(main_course, list_student))


some_lecturer = {'Python': [9, 10, 10], 'Git': [9, 10, 10]}
new_lecturer = {'Python': [9, 9, 10], 'Git': [9, 10, 10]}

first_course = 'Python'
list_lecturer = [some_lecturer, new_lecturer]

def lecturer(first_course, list_lecturer):
    list_marks = []
    for object in list_lecturer:
        for course, sign in object.items():
            if first_course == course:
                for figure in sign:
                    list_marks.append(figure)
                    average_for_lecturer= round(sum(list_marks)/len(list_marks), 1)
    return average_for_lecturer
print('Cредней оценка за лекции по курсу Python:', lecturer(first_course, list_lecturer))