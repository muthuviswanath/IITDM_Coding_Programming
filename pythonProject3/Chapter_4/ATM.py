class ATM:
    def dispense(self,card,pin,amount):
        m = Money()
        print(m)
        return m
class Money:
    pass
class Card:
    pass

a = ATM()
c = Card()
cash = a.dispense(c,1221,3000)
print(cash)
