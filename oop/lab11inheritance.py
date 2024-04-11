class Address:
    def __init__(self, city):
        self.city = city

    def get_info_city(self):
        print(f'{self.city} is the city in Rajsthan')


class Students(Address):
    def batch(self):
        print('from batch from Student class')


stu = Students('Mount Abu')
print(f'{stu.city} printed from parent class constructor')
stu.get_info_city()
stu.batch()
