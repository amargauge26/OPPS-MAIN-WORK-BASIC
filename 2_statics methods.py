
class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks= marks
    
    @staticmethod
    def hello():
        print("welcome guys")
        
    def get_marks(self):
        print("marks",self.marks)



s1=Student("amar",2)
s1.hello()