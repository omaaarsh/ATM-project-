from Transactions import *
class Balance_inquire_handler:
    def handle(self,account):
        handle=BalanceInquire()
        handle.excute(account)
class Withdraw_handler:
    def __init__(self,screen,kayboard):
        self.screen = screen
        self.kayboard=kayboard
    def handle(self,account):
        while True:
            try:
                amount=int(self.kayboard.get_input("Enter the amount: "))
                if amount<=0:
                    self.screen.show_message("Please enter a positive amount...")
                    continue
                transaction=WithDraw(amount)
                transaction.excute(account)
                break
            except ValueError:
                self.screen.show_message("Invalid input ,Please enter a valid amount ...")
class Deposit_handler:
    def __init__(self,screen,kayboard):
        self.screen = screen
        self.kayboard=kayboard
    def handle(self,account):
        while True:
            try:
                amount=int(self.kayboard.get_input("Enter the amount: "))
                if amount<=0:
                    self.screen.show_message("Please enter a positive amount...")
                    continue
                transaction=Deposit(amount)
                transaction.excute(account)
                break
            except ValueError:
                self.screen.show_message("Invalid input ,Please enter a valid amount ...")
class Transfer_handler:
    def __init__(self,screen,kayboard,bank):
        self.screen = screen
        self.kayboard =kayboard
        self.bank = bank
    def handle(self,account):
        while True:
            try:
                account_number=int(self.kayboard.get_input("Enter the number of the account to transfer: "))
                if account_number in self.bank.accounts.keys():
                    amount=int(self.kayboard.get_input("Enter the amount: "))
                    transaction=Transfer(amount)
                    transaction.excute(account, account_number,self.bank)
                    return
                else:
                    self.screen.show_message("Account not found!! , please enter a correct account number: ")
                    continue
            except ValueError:
                self.screen.show_message("invalid  inputs please enter correct inputs")
class PIN_handler:
    def __init__(self,screen,kayboard):
        self.screen = screen
        self.kayboard=kayboard
    def handle(self,account):
        while True:
            try:
                if account.linked_card:
                    old_pin=int(self.kayboard.get_input("Please enter old PIN: "))
                    if account.linked_card.validate(old_pin):
                        new_pin=int(self.kayboard.get_input("Please enter new PIN: "))
                        account.linked_card.set_pin(new_pin)
                        self.screen.show_message("Updated successfully")
                        return
                    else:
                        self.screen.show_message("incorrect PIN")
                        continue
            except ValueError:
                self.screen.show_message("invalid PIN")
class Transactions_history_handler:
    def handle(self,account):
        account.display_transaction()