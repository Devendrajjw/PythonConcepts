class ParentClass:

    def parent_method(self):
        return 'method in parent class'


class ChildClass(ParentClass):
    def child_method(self):
        return 'method in child class'

    def parent_method(self):
        return 'overrided method of parent class'

cc = ChildClass()
print(cc.child_method())
print(cc.parent_method())

# issubclass() To check if class is child class or not
print(issubclass(ChildClass, ParentClass))
