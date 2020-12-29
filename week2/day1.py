#Task 1

class Calculator:
    def __init__(self,para1,para2):
        self.para1 = para1
        self.para2 = para2

    def add(self):
        return self.para1 + self.para2

    def subtract(self):
        return self.para1 - self.para2
        
    def mul(self):
        return self.para1 * self.para2

    def div(self):
        return self.para1 / self.para2

#Inherited class
class ChildCalculator(Calculator):
    def __init__(self,para1,para2):
        super().__init__(para1,para2)
    
    def add(self):
        print(f'Addition of {self.para1} and {self.para2} is {self.para1+self.para2}')

    def mul(self):
        print(f'Multiplication of {self.para1} and {self.para2} is {self.para1*self.para2}')

#main method
def main():
    o1 = Calculator(10,5)
    print(f'Addition :{o1.add()}')
    print(f'Subtraction :{o1.subtract()}')
    print(f'Multiplication :{o1.mul()}')
    print(f'Division :{o1.div()}')

    c1 = ChildCalculator(10,5)
    c1.add()
    c1.mul()

if __name__ == "__main__":
    main()