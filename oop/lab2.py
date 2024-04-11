class Vechile:
    wheels = 4

    def __init__(self, name, doors, seats):
        self.name = name
        self.doors = doors
        self.seats = seats


car = Vechile('car', 2, 2)
van = Vechile('van', 6, 12)

print(car.wheels, car.name, car.doors, car.seats)
print(van.wheels, van.name, van.doors, van.seats)

print(getattr(car, 'doors'))
print(getattr(van, 'wheels'))
