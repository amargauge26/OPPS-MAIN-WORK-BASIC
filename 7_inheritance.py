class Car:
    @staticmethod
    def start():
        print("car start")
    
    
    @staticmethod
    def stop():
        print("car stopped")


class ToyotaCar(Car):
    def __init__(self,barnd):
        self.name=barnd
        
class Caiz(ToyotaCar):
    def __init__(self,type):
        self.type=type


car1 =Caiz("electric")
car1.start()