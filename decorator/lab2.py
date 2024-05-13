class Singeltone:
    __myvar = None

    @staticmethod
    def create_instance():
        if Singeltone.__myvar == None:
            Singeltone()
        return Singeltone.__myvar

    def __init__(self):
        if Singeltone.__myvar != None:
            print('object cannot be created using const')
        else:
            Singeltone.__myvar = self

if __name__ == '__main__':
    s1 = Singeltone.create_instance()
    print(s1)
    s2 = Singeltone.create_instance()
    print(s2)
