class Bank:
    def __init__(self,name="",switch_code=0):
        self.name = name
        self.switch_code = switch_code
        self.accounts={}
    def add_customer(self,customer):
        for account in customer.accounts.values():
            self.accounts[account.number]=account