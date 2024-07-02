import json

class UserData:
    def __init__(self, data=None):
        if data is None:
            self.data = {}
        else:
            self.data = data

    def show_user_data(self):
        for user, details in self.data.items():
            print(f"{user}: AGE = {details['AGE']}, CITY = {details['CITY']}")

    def update_user_data(self, user, age=None, city=None):
        if user in self.data:
            if age is not None:
                self.data[user]['AGE'] = age
            if city is not None:
                self.data[user]['CITY'] = city
            print(f"Updated {user}: AGE = {self.data[user]['AGE']}, CITY = {self.data[user]['CITY']}")
        else:
            print(f"{user} not found in the data.")

    def save_to_file(self, filename):
        with open(filename, 'w') as file:
            json.dump(self.data, file, indent=4)

    @classmethod
    def load_from_file(cls, filename):
        try:
            with open(filename, 'r') as file:
                data = json.load(file)
            return cls(data)
        except FileNotFoundError:
            print(f"{filename} not found.")
            return cls()

# Sample data
users = {
    "USER1": {"AGE": 25, "CITY": "New York"},
    "USER2": {"AGE": 30, "CITY": "Los Angeles"},
    "USER3": {"AGE": 22, "CITY": "Chicago"},
}

# Initialize the class with sample data
user_data = UserData(users)

# Display user data
user_data.show_user_data()

# Update user data
user_data.update_user_data("USER4", age=40, city="Bangalore")

# Save to file
user_data.save_to_file('users.json')

# Load from file and display data
loaded_user_data = UserData.load_from_file('users.json')
loaded_user_data.show_user_data()
