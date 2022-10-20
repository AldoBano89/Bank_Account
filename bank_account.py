class BankAccount:
    bank_name="European Bank"
    accounts = []
    def __init__(self, int_rate, balance, user): 
        self.accountHolder = user
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.accounts.append(self)

    def deposit(self, amount):
        self.balance += amount
        return self
        
    def withdraw(self, amount):
        if (self.balance - amount) < 0 :
            print ("Insufficient funds: Charging a $5 fee")
            self.balance-=5
            return self
        else:
            self.balance -= amount
            return self

    def yield_interest(self):
        if self.balance  <= 0 :
            return self
        else :
            self.balance += (self.balance * self.int_rate)
            return self
            
    @classmethod
    def display_account_info(cls):
        for account in cls.accounts:
            print("Balance of " + account.accountHolder +" : " +  str(account.balance))

sabrina = BankAccount(0.3, 1200, "Sabrina")
fatjon = BankAccount(0.3, 1200 , "Fatjon")

sabrina.deposit(200).deposit(300).withdraw(300).withdraw(200).withdraw(1200).yield_interest().display_account_info()
fatjon.deposit(300).deposit(200).deposit(300).withdraw(500).yield_interest().display_account_info()


