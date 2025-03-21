class interCalc:
    def __init__(self, principal, rate, time):
        self.principal = principal
        self.rate = rate
        self.time = time


    @property
    def compInter(self):
        return (self.principal * self.rate * self.time)/100
    
    @property
    def simpInter(self):
        return (self.principal * (1 + self.rate/100)** self.time - self.principal)
    
calc = interCalc(1000, 5, 2)  

print("Simple Interest:", calc.simpInter)   
print("Compound Interest:", calc.compInter) 

calc.principal = 5000

print("Updated Simple Interest: ", calc.simpInter)
print("Updated Compound Interest: ", calc.compInter)