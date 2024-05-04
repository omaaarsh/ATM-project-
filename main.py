from account import Account
from Atm import Atm_interface
from bank import Bank
from customer import Customer
from card import Card
from card_reader import Card_Reader
def main():
    CIB=Bank("CIB",1110)
    omar=Customer("omar","127 w pyramids gardens","201030222769","omarsherifelghamry@gmail.com")
    account1=Account(2000)
    account2=Account(2004)
    card=Card(200027721,1975)
    account1.link_card(card)
    omar.add_account(account1)
    omar.add_account(account2)
    CIB.add_customer(omar)
    atm=Atm_interface("127 w pyramids gardens",CIB)
    card_reader=Card_Reader(atm)
    card_reader.insert_card(card)
if __name__ == "__main__":
    main()
