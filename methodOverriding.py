class Parent:
    def greet(self):
        print("Hello from Parent class!")

class Child(Parent):
    def greet(self):  # Overrides the parent method
        print("Hello from Child class!")

# Create objects
parent = Parent()
child = Child()

# Call methods
parent.greet()
child.greet()
