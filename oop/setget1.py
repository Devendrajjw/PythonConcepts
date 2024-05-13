class emp:
    def __init__(self):
        self.name = ""
        self.salary = 0
    def getter(self):
        return self.name, self.salary
    def setter(self):
        self.name = input("enter name ")
        self.salary = input("enter salary ")
        return self.name, self.salary
    def wfile(self):
        with open("emp_details.log", "a") as af:
            af.write(str(self.setter()))


# obj1 = emp("devendra", 5000000)
# print(obj1.get())

# obj2 = emp()
# obj2.set()
# print(obj2.get())

obj3 = emp()
obj3.wfile()
