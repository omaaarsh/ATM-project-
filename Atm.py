from handler import *
from kayboard import *
from screen import *
class Atm_interface:
    def __init__(self,location="",bank=None):
        self.location = location
        self.bank=bank
        self.kayboard=Kayboard()
        self.screen = Screen()
        self.balance_inquire_handler=Balance_inquire_handler()
        self.withdraw_handler=Withdraw_handler(self.screen,self.kayboard)
        self.deposit_handler=Deposit_handler(self.screen,self.kayboard)
        self.transfer_handler=Transfer_handler(self.screen,self.kayboard,self.bank)
        self.pin_handler=PIN_handler(self.screen,self.kayboard)
        self.transactions_history_handler=Transactions_history_handler()
    def display_mainMenu(self,account):
        message="""
    1. Balance Inquire
    2. Withdraw 
    3. Deposit
    4. Trasfer
    5. Change PIN
    6. View transactions
    7. Exit
    Enter your choice: """
        while True:
            choice=int(self.kayboard.get_input(message))
            match choice:
                case 1 :
                    self.balance_inquire_handler.handle(account)
                case 2 :
                    self.withdraw_handler.handle(account)
                case 3 :
                    self.deposit_handler.handle(account)
                case 4 :
                    self.transfer_handler.handle(account)
                case 5 :
                    self.pin_handler.handle(account)
                case 6 :
                    self.transactions_history_handler.handle(account)
                case 7:
                    self.screen.show_message("Ejecting Card...\n GoodBye !")
                    return
                case _:
                    self.screen.show_message("Invalid choice... try again..")
            self.kayboard.get_input("press Enter to continue... ")
            self.screen.clear()