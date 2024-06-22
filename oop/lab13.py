class Sample:
    __instance = None
    def __new__(cls):
        if cls.__instance == None:
            cls.__instance = super().__new__(cls)
        return cls.__instance


sam1 = Sample()
sam2 = Sample()

print(id(sam1))
print(id(sam2))
