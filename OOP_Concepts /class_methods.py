# 

class BankAccount:
    bank_name = 'Tech4Girls Bank'
    def __init__(self,account_holder , balance = 0):
        self.account_holder = account_holder
        self.balance = balance
        
    def username(self):
        return f'Bank name: {self.bank_name} \nAccount name : {self.account_holder}'   
    
    def deposit(self, amount):
        if amount < 0:
            print('Enter only positive numbers')
        else:    
            self.balance += amount
        return f'Current Balance = {self.balance}'  
    
    def withdraw(self, amount):
        if amount < 0:
            print('Enter only positive numbers')
        else:    
            self.balance -= amount
        return f'Current Balance = {self.balance}'  
          
        
    def deposit_inp(self):
        """This allows the user to input his own deposit amount rather than passing a number as an argument when
        calling the function"""
        amount =int(input('Enter deposit amount: '))
        if amount < 0:
            print('Enter only positive numbers')
        else:    
            self.balance += amount
        return f'Current Balance = {self.balance}'  
    
    def withdraw_inp(self):
        """This allows the user to input his own withdraw amount rather than passing a number as an argument when
        calling the function"""
        amount =int(input('Enter withdrawal amount: '))
        if amount > self.balance:
            print('You have less amount in your account')
        elif amount < 0:
            print('Enter positive numbers only')    
        else:    
            self.balance -= amount
        return f'Current Balance = {self.balance}'  
    
    
    """ Static and Class methods are accessed by the use of the @ which is called a decorator"""
    @staticmethod
    
    def bank_policy():
        """Details of bank poilcy"""
        return '\nIf your account is under Tech4Girls , then you get a credit of 5$ every month!!!'
    
    @classmethod
    
    def get_bank_name(cls):
        return f'Bank name : {cls.bank_name}'
        
    

# Created an instance to show the user account name    
user1 = BankAccount('Antwiwaa')     

# Calling methods that have been created in the class   
print(user1.username())
print(user1.deposit(54))
print(user1.withdraw(40))

# Calling method that has the input function to allow user to enter amount
print(user1.deposit_inp())
print(user1.withdraw_inp())


#Static methods can only be accessed by the use of the the calss name ie: BankAccount
print(BankAccount.bank_policy())
print(user1.get_bank_name())

