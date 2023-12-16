class Person():
    def __init__(self, name, salary, nationalID):
        self.name = name
        self.salary = salary
        self.__nationalID = nationalID

    def getName(self):
        return self.name
    def setName(self, name):
        self.name = name

    @property
    def x(self):
        return self.salary
    @x.setter
    def x(self, salary):
        self.salary = salary


    def getSalary(self):
        return self.salary
    def setSalary(self, salary):
        self.salary = salary

class Student():
    def __init__(self, name, grades=0):
        self.__name = name
        self.grade = grades

    @property
    def grade(self):
        return self.__grade

    @grade.setter
    def grade(self, newGrade):
        self.__grade = newGrade


s1 = Student('Abdul Ahad')
s2 = Student('Asma')
print(s1._Student__name, s2._Student__name)
s1.grade = 85
s2.grade = 90

print(s1.grade, s2.grade)








# oP1 = Person('Abdul Ahad', 1000, 123)
# oP2 = Person('Asma', 1300, 3121)
#
# print(oP2.name)
# print(oP2.salary)
#
# oP2.salary = 1000
# print(oP2.salary)
# print(oP2._Person__nationalID)
