"""class Student:
    name = "amar"
class Car:
    color = "blue"
s1 =Student()
print(s1.name) 
print(s1)
car1 = Car()
print(car1.color)
"""



class Student:
    
    #defult copnstractuers
    college_name = "vit"
    
    name='anai' # print when only matching ofd obj of this instance is created
    def __init__(self,name,marks):
        self.name=name
        self.marks= marks
    
    
    def hello(self):
        print("welcome guys",self.name)
        
    def get_marks(self):
        print("marks",self.marks)
    
    #parameterized construcate
    
    

s1 = Student("amar",97)  # Creating an instance of Student class
print(s1.name,s1.marks)  # Printing the object reference of s1

print(s1.college_name)

s1.hello()
s1.get_marks()

s1.name ="raj"

print(s1.name)


    