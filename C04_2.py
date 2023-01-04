class bankaccount:
    def __init__(self):
        self.balance=0
        print("Account number=1038958894")
        print("Name:Aparna")
        print("Type of account:Savings account")
    def deposit(self):
        amount=float(input("enter the amount to deposit: "))
        self.balance=self.balance+amount
        print("amount deosited: ",amount)
    def withdrawal(self):
        amount=float(input("Enter the amount for withdrawal: "))
        if self.balance>=amount:
            self.balance=amount
            print("Amount deposited: ",amount)
        else:
            print("no balance available")
    def display(self):
        print("balance available is: ",self.balance)
obj=bankaccount()
while(True):
    print("\n1.Deposit money \n2.Withdraw money \n3.Exit")
    ch=int(input("enter the choice: "))
    if(ch==1):
        obj.deposit()
        obj.display()
    elif(ch==2):
        obj.withdrawal()
        obj.display()
    else:
        exit(0)
obj.display()
        
        
        
        
        
        
        
        
        