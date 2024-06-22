class Person:
    def __init__(self, name, date):
        self.name = name
        self.date = date

    def display(self):
        print(self.name, self.date)


if __name__ == "__main__":
    obj = Person('dev', '17/06/24')
    obj.display()
