class Vechile:
    wheels = 4

    def __init__(self, name, doors, seat):
        self.name = name
        self.doors = doors
        self.seat = seat

    def distance(self, km):
        return f'{self.name} has travelled {km} kms'


car = Vechile('Nexon', 4, 4)
print(car.distance(40))

print(getattr(car, 'seat'))
print(hasattr(car, 'ac'))
print(hasattr(car, 'name'))
