class A:
    def show(self):
        print("in A show")

class B(A):
    #if pas then a methods of show will work
    def show(self):
        print("in b show")
    


a1= A()
a1.show()

a2=B()
a2.show()