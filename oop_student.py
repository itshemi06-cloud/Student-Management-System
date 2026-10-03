from abc import ABC, abstractmethod

print("======Student Management System======")

class person(ABC):
    def __init__(self, name, age):
        self._name = name
        self.age = age

    @abstractmethod
    def show_role(self):
        pass

    def show_name(self):
        print("Name:", self._name)

    
class Student(person):
    def __init__(self, name, age, course):
        super().__init__(name, age)
        self.course = course

    def show_role(self):
        print("i am a student")

    def show_details(self):
        self.show_name()
        print(" age:", self.age)
        print("course:", self.course)


class Teacher(person):
    def __init__(self, name, age):
        super().__init__(name, age)

    def show_role(self):
        print("i am a teacher")

    
student1 = Student("Hemanshi", 20, "Computer Engineering")
teacher1 = Teacher("Nitaben", 45)

student1.show_role()
teacher1.show_role()
print()

student1.show_details()
