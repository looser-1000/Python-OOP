class Calculator:
    def add(self, a, b=0, c=0):  # Default arguments simulate overloading
        return a + b + c

calc = Calculator()
print(calc.add(10))        # Adds one number
print(calc.add(10, 20))    # Adds two numbers
print(calc.add(10, 20, 30))  # Adds three numbers
