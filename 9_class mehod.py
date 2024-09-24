class Person:
    #class attribute
    name = "amar"
    
    """ def cn(self,name):
        #diffrent attribute
        #Person.name=name
        self.__class__.name="ruhul"""
        
    @classmethod
    def cn(cls,name):
        cls.name = name



p1 = Person()

p1.cn("ram")
print(p1.name)
print(Person.name)