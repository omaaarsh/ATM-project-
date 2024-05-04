from abc import ABC,abstractmethod
import datetime
from enum import Enum
import uuid
class Transactions_type(Enum):
    DEPOSIT ="Deposit"
    WITHDRAW ="Withdraw"
    BALANCEINQUIRE="BalanceInquire"
    TRANSFER ="Transfer"
class Transactions(ABC):
    def __init__(self,transaction_type,amount=None):
        self.id=uuid.uuid4()
        self.timstamp=datetime.datetime.now()
        self.type=transaction_type
        self.amount=amount
    @abstractmethod
    def excute(self):
        pass
class WithDraw(Transactions):
    def __init__(self,amount):
        super().__init__(Transactions_type.WITHDRAW,amount)
        self.amount = amount
    def excute(self,account):
        if account.balance>= self.amount:
            account.balance-=self.amount
            print(f"successfully processed ,your balance now is{account.balance} ")
            account.addTransaction(self)
        else:
            print(f"failed to process,you don't have enough money")
class Deposit(Transactions):
    def __init__(self,amount):
        super().__init__(Transactions_type.DEPOSIT,amount)            
        self.amount = amount
    def excute(self,account):
        account.balance+=self.amount
        print(f"successfully processed ,your balance now is {account.balance}")
        account.addTransaction(self)
class BalanceInquire(Transactions):
    def __init__(self):
        super().__init__(Transactions_type.BALANCEINQUIRE,amount=0)
    def excute(self,account):
        self.amount=account
        print(f"your balance is: {account.balance}")
        account.addTransaction(self)
class Transfer(Transactions):
    def __init__(self,amount):
        super().__init__(Transactions_type.TRANSFER,amount)
        self.amount=amount
    def excute(self,account,account_number,bank):
        if account.balance>= self.amount:
            account.balance-=self.amount
            bank.accounts[account_number].balance+=self.amount
            print(f"successfully processed ,your balance now is{account.balance} ")
            account.addTransaction(self)
        else:
            print(f"failed to process,you don't have enough money")