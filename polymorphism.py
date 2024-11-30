# 3 i +  5 j
# 4 i +  2 j
# ------------
# 7 i +  7 j
class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img
    def showNumber(self):
        print(self.real, "i + ", self.img, "j")
    #     Dunder function
    def __add__(self, num2):
        newReal = self.real + num2.real
        newImg = self.img + num2.img
        return Complex(newReal, newImg)

num1 = Complex(3,5)
num1.showNumber()
num2 = Complex(4,2)
num2.showNumber()
print("------------")
# num3 = num1.add(num2)
# num3.showNumber()

# better way to do that
num3 = num1 + num2
num3.showNumber()

