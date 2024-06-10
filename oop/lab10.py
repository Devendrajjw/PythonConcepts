class MyCollection:
    def __init__(self, items):
        self.items = items

    def __len__(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)

# Example usage 1
# my_collection = MyCollection([9, 2, 3, 4, 5])
# print(len(my_collection))  # Output: 5

# Example usage 2
# my_collection = MyCollection("hello")
# print(str(my_collection))

