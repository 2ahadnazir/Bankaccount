#  Employee Manager inheritance
#
# Define the Employee class, which we will use as a base
class Employee():
    def __init__(self, name, title, ratePerHour=None):
        self.name = name
        self.title = title
        if ratePerHour is not None:
            ratePerHour = float(ratePerHour)
        self.ratePerHour = ratePerHour

    def getName(self):
        return self.name
    def getTitle(self):
        return self.title
    def payPerYear(self):
        # 52 weeks * 5 days a week * 8 hours per day
        pay = 52 * 5 * 8 * self.ratePerHour
        return pay

# Define a Manager subclass that inherits from Employee
class Manager(Employee):
    def __init__(self, name, title, salary, reportsList=None):
        self.salary = float(salary)
        if reportsList is None:
            reportsList = []
        self.reportList = reportsList
        super().__init__(name, title)

    def getReports(self):
        return self.reportList

    def payPerYear(self, givenBonus = False):
        pay = self.salary
        if givenBonus:
            pay = pay + (.10 * self.salary)
            print(self.name, "gets a bonus")
        return pay

oE1 = Employee('Asma', 'Pizza Maker', 16)
oE2  =Employee('Wasil', 'Cashier', 14)
oM = Manager('Abdul Ahad','Branch Manager', 45000, [oE1, oE2])

print(oE1.getName())
print(oE1.getTitle())
print(oE1.payPerYear())
print('-------------')
print(oE2.getName())
print(oE2.getTitle())
print(oE2.payPerYear())
print('-------------')
print(oM.getName())
print(oM.getTitle())
print(oM.payPerYear(True))
print('List of employee under' + oM.getTitle())
reportsList = oM.getReports()
for emp in reportsList:
    print(emp.getName()+': '+emp.getTitle())
