import time

class Emp:
    def __init__(self):
        self.emp_details = ['name', 'salary']
        self.emp_dict = {}
        self.list1 = []
        self.emp_menu()
        self.list1.append(self.emp_dict)

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
        for user_name in self.emp_details:
            user_name = input(f" enter {user_name}: ")
            self.emp_dict[user_name] = user_name
        self.list1.append(self.emp_dict)
        self.emp_menu()

    def emp_salary(self):
        for user_salary in self.emp_details:
            user_salary = input(f" enter {user_salary}: ")
            self.emp_dict[user_salary] = user_salary
        # self.list1.append(self.emp_dict)
        self.emp_menu()

    def getter(self):
        print(self.list1)
        self.emp_menu()


obj1 = Emp()
# [{'name': 'bbb', 'salary': 222}, {'name': 'bbb', 'salary': 222}, {'name': 'bbb', 'salary': 222}, {'name': 'bbb', 'salary': 222}]
obj1.emp_name()
