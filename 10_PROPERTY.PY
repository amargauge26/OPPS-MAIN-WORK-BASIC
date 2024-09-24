class Student:
    def __init__(self,phy,chem,math):
        self.phy=phy
        self.chem=chem
        self.math=math

    @property
    def per(self):
            return str((self.phy+self.chem+self.math)/3)+'%'
s1=Student(98,33,34)

print(s1.per)
s1.phy=54
print(s1.phy)


print(s1.per)