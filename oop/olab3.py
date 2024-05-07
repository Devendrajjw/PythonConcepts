import olab1, olab2


class Olab3:
    def __init__(self):
        print('from olab3 ')
        print(__name__)

    def uname(self):
        print('devendra')


print(__name__)
obj = Olab3()
obj.uname()

