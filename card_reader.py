from Authenticate import *
class Card_Reader:
    def __init__(self,Atm_interface):
        self.atm_interface = Atm_interface
        self.authenticator = Authenticate(self.atm_interface.bank)
    def insert_card(self,card):
        while True:
            pin=int(self.atm_interface.kayboard.get_input("Enter your card PIN: "))
            account=self.authenticator.authenticate(card.number,pin)
            if account:
                    self.atm_interface.display_mainMenu(account)
                    break
            else:
                self.atm_interface.screen.show_message("invalid PIN!!")