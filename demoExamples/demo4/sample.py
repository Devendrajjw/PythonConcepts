

def add(a, b):
    return a+b


def multiply(a, b):
    return a*b

class DatabaseConnection:
    def __init__(self):
        self.connected = False

    def connect(self):
        self.connected = True
        print("Database connected")

    def disconnect(self):
        self.connected = False
        print("Database disconnected")
