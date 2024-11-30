# Public & Private

class Account:
    def __init__(self, acc_no,acc_pass):
        self.acc_no = acc_no
        self.__acc_pass = acc_pass
    #     here we can see that by using __ we made acc.pass
    #     attribute private that's why we can access this in another
    #     method inside the class. Outside the class, we can use the private
    #     attributes if it is used in that method, otherwise directly we can never
    #     use the private attribute __acc.pass
    #
    def hello(self):
        print("Hello! Account No: ", self.__acc_pass)

a1 = Account(1010, 123456)
print("Account No: " + str(a1.acc_no))
# print("Account Password: " +  a1.__acc_pass)
print(a1.hello())
