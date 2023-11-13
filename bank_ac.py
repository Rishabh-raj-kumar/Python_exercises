class Bank(object):

    def __init__(self,balance):
        self.balance = balance
    
    def total_amount(self):
        print(f'Total amount in bank : {self.balance}')
    
    def add_amount(self,amount):
        self.balance += amount
    
    def withdraw(self,amount):
        if amount > self.balance:
            print('Please withdraw a valid money.')
        else:
            self.balance -= amount
        

x = Bank(10000)
x.add_amount(7000)
x.withdraw(14000)
x.total_amount()
