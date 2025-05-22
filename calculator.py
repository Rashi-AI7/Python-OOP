num = int(input("Hey, Enter the number:"))


class Calculator:

    def __init__(self, n):
        self.number = n

    def square(self, n1):
        sq = n1*n1
        return sq
    
    def cube(self, n2):
        cube = n2*n2*n2
        return cube
    
    def sqrt(self, n3):
        sqroot = n3 ** 0.5
        return sqroot
    
num1 = Calculator(num)
print(f"The square root is {num1.sqrt(num)}")
print(f"The square is {num1.square(num)}")
print(f"The cube is {num1.cube(num)}") 