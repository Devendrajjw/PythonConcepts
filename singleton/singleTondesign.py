class Singleton_ex:
    __instance = None

    @staticmethod
    def get_instance():
        if Singleton_ex.__instance == None:
            Singleton_ex()
        return Singleton_ex.__instance

    def __init__(self):
        if Singleton_ex.__instance != None:
            raise Exception("Singleton exist already")
        else:
            Singleton_ex.__instance = self


if __name__ == '__main__':
    s1 = Singleton_ex.get_instance()
    print(s1)
    s2 = Singleton_ex.get_instance()

    print(s2)

    #s3 = Singleton_ex()
