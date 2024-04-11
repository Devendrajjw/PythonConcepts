class ParentClass:

    def parent_method(self):
        return "method in parent class"


# pc = ParentClass()
# print(type(pc.parent_method()))
# print(pc.parent_method())

class ChildClass(ParentClass):

    def child_method(self):
        pass


cc = ChildClass()
print(cc.parent_method())
