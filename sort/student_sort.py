"""
A python example of sort and lambda to sort a students list based on various attributes of student object.
"""

class Student:
    def __init__(self, roll_num, name, year, marks):
        self.roll_num = roll_num
        self.name = name
        self.year = year
        self.marks = marks

    def get_student(self):
        return "Roll Number: {}, Name: {}, Year: {}, Marks: {}".format(self.roll_num, self.name, self.year, self.marks)


if __name__ == "__main__":
    students = list()
    students.append(Student(2, "Max", 3, 90))
    students.append(Student(1, "Peter", 3, 80))
    students.append(Student(1, "Maxwell", 4, 80))
    students.append(Student(4, "Sam", 2, 100))
    students.append(Student(3, "Pam", 1, 70))

    students.sort(key=lambda i: (i.marks, -i.roll_num, i.year), reverse=True)

    print("Student List After Sorting: ")
    for st in students:
        print(st.get_student())


