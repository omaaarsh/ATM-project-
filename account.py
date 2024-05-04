class Account:
    def __init__(self,number=0):
        self.number = number
        self.balance = 0
        self.linked_card=None
        self.transactions_history=[]
    def addTransaction(self, transaction):
        self.transactions_history.append(transaction)
    def link_card(self, card):
        self.linked_card=card
    def display_transaction(self):
        if(self.transactions_history):
            for transaction in self.transactions_history:
                print(f"*ID:{transaction.id}\n*Type: {transaction.type.value}\n*Time: {transaction.timstamp}\n{"*"*10}\n")
        else:
            print("No transaction available ")