class Complex:
    def __init__(self,real,img):
        self.real=real
        self.img=img    
    
    
    def showNum(self):
        print(self.real,"+",self.img,"i")
    
    #dunder fun
    def __add__(self,num2):
        newReal = self.real+num2.real
        
        newImg = self.img + num2.img
        return Complex(newReal,newImg)

    def __sub__(self,num2):
        newReal = self.real-num2.real
        
        newImg = self.img - num2.img
        return Complex(newReal,newImg)

    
    
num1 = Complex(1,2)
num2 = Complex(2,3)



#
#new3.showNum()

num3=num1+num2
num3.showNum()

num4 = num2-num3
num4.showNum()