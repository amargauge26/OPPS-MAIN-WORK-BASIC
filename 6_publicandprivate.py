class Account:
    def __init__(self,acc_no,acc_pass):
        self.acc_no=acc_no
        #private
        self.__acc_pass=acc_pass


    def resetpass(self):
        print(self.__acc_pass)
        


acc1  =Account("1234","abcde")


print(acc1.acc_no)
print(acc1.resetpass())




# second part

class Person:
    __name= "amar"

    
    def __hello(self):
        print("hello person")
    
    
    def welcome(self):
       self. __hello()



p1 =Person()

print(p1.welcome())