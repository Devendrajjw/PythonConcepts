import unittest

'''
cognitive programmer
https://youtu.be/HKTyOUx9Wf4
'''


def sum(a, b):
    return a + b


class SumTest(unittest.TestCase):
    def setUp(self):
        print("... Setup is called ...")
        self.a = 10
        self.b = 20

    def tearDown(self):
        self.a = 0
        self.b = 0
        print("Tear down called .... ")


    def test_sumfunc_1(self):
        print("Test - 1 Called")
        # Act
        result = sum(self.a, self.b)
        # Assert
        self.assertEqual(result, self.a + self.b)

    def test_sumfunc_2(self):
        print("Test - 2 Called")
        # Act
        result = sum(self.b, self.a)
        # Assert
        self.assertEqual(result, self.a + self.b)


if __name__ == "__main__":
    unittest.main()


