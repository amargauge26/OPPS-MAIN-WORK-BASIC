class A:
    varA = "welcome to a"
    

class B:
    varB="welcome to b"
    
    
class C(A,B):
    varC="welome to c"


"""c1 = C()

print(c1.varC)
print(c1.varB)
print(c1.varA)

"""

class Car:
    def __init__(self,type):
        self.type = type

    
    
    @staticmethod
    def start():
        print("car start")
    
    @staticmethod
    def stop():
        print("car stopped")


class ToyotaCar(Car):
    def __init__(self,name,type):
      super().__init__(type)
      self.name=name
      super().start()
      



car1 = ToyotaCar("cc",'ele')
print(car1.type)

