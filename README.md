# OOP Basic Questions

## What do you mean by OOP?

OOP (Object-Oriented Programming) is a programming paradigm based on the concept of "objects," which are instances of classes. It allows developers to structure programs by bundling related data and methods (functions) together. The four main principles of OOP are:
- **Encapsulation**: Bundling data (attributes) and methods (functions) into a single unit or object and restricting access to some of the object's components.
- **Abstraction**: Hiding the complex details and showing only the necessary parts of the object.
- **Inheritance**: Allowing a class to inherit properties and behaviors (methods) from another class.
- **Polymorphism**: The ability to present the same interface for different data types or objects, meaning one function can work in different ways.

OOP helps in making code more reusable, scalable, and easier to maintain.

---

## Define Class
Class is a blueprint for creating objects. Before creating an object, a class is created.

## Define Objects
Object is an instance of a class.

## Define Constructor
It is a special method in Python that gets called automatically when an object is created. In Python, the `__init__` function is called the constructor. It is also used to initialize attributes of that object.

## Define Destructor
It is a method that is used when we want to delete the entire object or a specific property of that object. It is denoted in Python by `del`.

Example:
```python
s1 = Person(“Salis Khan”)
print(s1.name)   # Output: Salis Khan
del s1.name      # Deletes the name attribute of that object
print(s1.name)   # No object available as name
```
## Define Attributes
In OOP, attributes are the data or properties that belong to an object. They define the characteristics of the object, like the name, age etc. of the object Person.

## Classification Of Attributes
class attributes 
object attributes
object attributes > class attributes (Preference basis)

```python
Example:
class Student:
    name = “anonymous”  # class attribute
   def __ init __(self, name):
           self.name = name  # object attribute
           print(self.name)

s1 = Student(“Farjad Ahmed”)
s1.name       # here in output we will get Farjad Ahmed and not anonymous because obj attr has more preference than class attr

```

## Define Method
In OOP, inside the class all functions are said to be methods. Class is constructed with data(attributes) and methods(functions).
``` python
class Student:
    def welcome(self):  #  method
          print(“Welcome !”)
s1 = Student()
print(s1.welcome()) 

```

## Static Method
Methods that don’t use the self parameter. Static method works at the class level.
``` python
class Student:
    @staticmethod   # decorator
     def college():    # static function or method
          print(“420 College”)
s1 = Student()
print(s1.college())

```

## Class Method
Class method is bound to the class and receives the class as an implicit first argument.
``` python
class Student:
        @classmethod   # decorator
        def college(cls):  # class method
               pass

```

## Public & Private
``` python
class Student:
      def __ init __(self,id,pass):
           self.id = id    # public attr
           __self.pass = pass  # private attr
        #this attribute becomes private using __ before self.pass attributes. Since it becomes private attributes outside the Student class we can’t use this pass data. but inside the class if we define another method we can still use pass inside that method. Outside the Student class we can get that pass not directly but get access to the method which used that private attribute pass.

s1 = student(101, abcde)
print(s1.id)  #we get this
print(s1.pass)  #can not get this



```

## Method Overloading
Method overloading is achieved in Python by providing default arguments in the method.
``` python
class Calculator:
       def add(self, a, b=0, c=0):
              return a+b+c
calc = Calculator()
print(calc.add(10))   #Adds one number
print(calc.add(10,20))  #Adds two numbers
print(calc.add(10,20,5)) #Adds three numbers


```

## Method Overriding
When a method in the child class has the same name as the method in the parent class. The child class method overrides the parent method.

```python
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


```

## Sample Basic Problem: (Banking)
```python
class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited: {amount}, New Balance: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance!")
        else:
            self.balance -= amount
            print(f"Withdrawn: {amount}, New Balance: {self.balance}")

class SavingsAccount(BankAccount):  # Inheritance
    def __init__(self, account_holder, balance=0, interest_rate=0.02):
        super().__init__(account_holder, balance)  # Call parent constructor
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        print(f"Interest Added: {interest}, New Balance: {self.balance}")

# Create and use accounts
account = SavingsAccount("John Doe", 1000)
account.deposit(500)
account.withdraw(300)
account.add_interest()



```
