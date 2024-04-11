class Customer:
    def __init__(self, name, gender, address):
        self.name = name
        self.gender = gender
        self.address = address

    def get_customer_info(self):
        print(self.name, self.gender, self.address.city, self.address.pin, self.address.state)


class Address:
    def __init__(self, city, pin, state):
        self.city = city
        self.pin = pin
        self.state = state


addr = Address('Bangalore', 560076, 'Karnataka')
cust = Customer('Ankit', 'Male', addr)
cust.get_customer_info()
