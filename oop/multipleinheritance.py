class Mother:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello, my name is {self.name}. I am your mother.")

class Father:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello, my name is {self.name}. I am your father.")

class Child(Mother, Father):
    def __init__(self, name, mother_name, father_name):
        Mother.__init__(self, mother_name)
        Father.__init__(self, father_name)
        self.name = name

    def greet(self):
        print(f"Hello, my name is {self.name}.")
        Mother.greet(self)
        Father.greet(self)

# Usage
child = Child("Charlie", "Alice", "Bob")
child.greet()
