import time

class Emp:
    def __init__(self):
        # self.name = ""
        # self.salary = 0
        self.salary = []
        self.name = []
        self.emp_menu()

    def emp_menu(self):
        user_input = int(input(""" Select the required option 
                           1. press 1 to give emp name 
                           2. press 2 to give emp salary
                           3. press 3 to display emp name
                           4. press any key to exit
                           """))
        if user_input == 1:
            self.emp_name()
        elif user_input == 2:
            self.emp_salary()
        elif user_input == 3:
            self.getter()
        else:
            print(" Successfully exit ")
            exit()

    def emp_name(self):
        user_name = input(" enter employee name ")
        # self.name = user_name
        if user_name not in self.name:
            self.name.append(user_name)
            print(" Employee name entered successfully ")
        else:
            print("employee name already exist, waiting for 3 seconds")
            time.sleep(3)

        self.emp_menu()

    def emp_salary(self):
        user_salary = int(input("enter salary "))
        # self.salary = user_salary
        self.salary.append(user_salary)
        print(" Employee salary entered successfully ")
        self.emp_menu()

    def getter(self):
        print(self.name)
        print(self.salary)
        self.emp_menu()


obj1 = Emp()
