class TestC:
    class_variable = 'Ravi'
    print(class_variable)

    def __init__(self):
        self.a = 'hero'
        print(self.a)


tc = TestC()
tc.class_variable = 'Ram'
print(tc.class_variable)
tc.class_variable = 'Karn'
print(tc.class_variable)
