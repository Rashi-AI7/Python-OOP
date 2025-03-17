class complexNum:
    def __init__(self, real, img):
        self.real = real
        self.img = img

    def showNumber(self):
        f"{self.real} + {self.img}j"

    def __add__(self, other):
        newReal = self.real + other.real 
        newImg = self.img + other.img
        return complexNum(newReal, newImg)
    
num1 = complexNum(4,5)
num1.showNumber()

num2 = complexNum(7,3)
num2.showNumber()

num3 = num1 + num2
num3.showNumber()