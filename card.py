class Card:
    def __init__(self,number=0,pin=0):
        self.number = number
        self.__pin = pin 
    def get_pin(self):
        return self.__pin    
    def set_pin(self,new_pin):
            self.__pin = new_pin
    def validate(self,old_pin):
        return self.__pin == old_pin