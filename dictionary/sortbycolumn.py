students = [
    {'name': 'John', 'age': 20},
    {'name': 'Alice', 'age': 18},
    {'name': 'Bob', 'age': 22}
]

sr = sorted(students, key=lambda z: z['age'])
print(sr)
