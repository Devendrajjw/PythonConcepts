class Employee:
    retirement_age = 50

    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.remaining_years = None
        self.salary = None

    def years_to_work(self, present_age):
        self.remaining_years = self.retirement_age - present_age
        return self.remaining_years

    def setSalary(self, salary):
        self.salary = salary

    def getSalary(self):
        return self.salary


emp1 = Employee('devendra', 100)
emp1.setSalary(1)
print(emp1.getSalary())
print(emp1.years_to_work(35))
