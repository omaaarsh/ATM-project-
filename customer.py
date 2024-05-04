class Customer:
    def __init__(self,name="",address="",mobile="",email=""):
       self.name = name
       self.address = address
       self.mobile = mobile
       self.email = email
       self.accounts={}
    def add_account(self, account):
        self.accounts[account.number]=account