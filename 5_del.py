class Student:
    def __init__(self,name):
        self.name = name
    
    
s1 = Student("amar")

del s1.name
print(s1.name)