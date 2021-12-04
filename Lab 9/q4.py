class Parent:
    def show(self):
        print("Parent method")
class Child(Parent):
    def display(self):
        print("Child method")
c = Child()
c.display()
c.show()