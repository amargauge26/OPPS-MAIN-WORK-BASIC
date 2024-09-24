

class Account:
    def __init__(self,bal,acc):
        self.bal =bal
        self.acc = acc
        
    #debit
    
    def debit(self,amount):
        self.bal -=amount
        print(amount,"wAS DEBITED")
        print("bal",self.get_bal())
    
    def credit(self,amount):
        self.bal += amount
        
        print("new bal",amount)
        print("bal",self.get_bal())
        
    def get_bal(self):
        return self.bal
    
acc1 = Account(500,12122)



acc1.debit(10)
acc1.credit(20)