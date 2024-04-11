class Vechile:
    color = 'blue'


car = Vechile()
print(car.color)
print(getattr(car, 'color'))
print(hasattr(car, 'color'))

setattr(car, 'color', 'red')
print(getattr(car, 'color'))

setattr(car, 'speed', 120)
print(getattr(car, 'speed'))
print(getattr(car, 'color'))
print(car.speed)

delattr(car, 'speed')
# print(car.speed)
