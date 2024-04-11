class Demo:
    def bird(self):
        print("Lion is a Bird")


def demo_bird_patch():
    print("Parrot is a Bird")


# Normal class call
obj1 = Demo()
obj1.bird()

# calling class method after monkey patch
obj1.bird = demo_bird_patch
obj1.bird()
