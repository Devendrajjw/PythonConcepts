class Sample:
    # __instance = None
    # def __new__(cls, *args, **kwargs):
    #     if cls.__instance == None:
    #         cls.__instance = super().__new__(cls)
    #     return cls.__instance
    #
    def __init__(self):
        print("from init")

ob1 = Sample()
ob2 = Sample()

print(id(ob1))
print(id(ob2))
