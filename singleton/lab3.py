class Sample:
    __instance = None
    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            print('creating instance')
            cls.__instance = super(Sample, self).__new__()
