class Employee:
    company = "Microsoft"
    def __init__(self, name, designation, salary):
        self.name = name
        self.designation = designation
        self.salary = salary

e1 = Employee("Manas", "Security Manager", 1000000)
print(e1.name, e1.designation, e1.salary, e1.company)

e2 = Employee("Shreyansh", "Data Scientist", 1500000)
print(e2.name, e2.designation, e2.salary, e2.company)

e3 = Employee("Prakhar", "Human Resources", 1200000)
print(e3.name, e3.designation, e3.salary, e3.company)