class Atm(object):
    def __init__(self, card_num, pin):
        self.card_num = card_num
        self.pin = pin

    def cashWithdrawl(self):
        print("The money has successfully been withdrawed")
    
    def balanceEnquiry(self):
        print("You have $123,456 left in your account")

atm1 = Atm(12, 123456)
atm1.cashWithdrawl()
atm1.balanceEnquiry()
print(atm1.card_num)