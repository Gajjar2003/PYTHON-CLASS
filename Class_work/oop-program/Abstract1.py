from abc import ABC,abstractmethod

class Account(ABC):
    
    balance = 0

    @abstractmethod
    def deposite(self,amount):
        pass

    @abstractmethod
    def withdrow(self,amount):
        pass

    def getbalance(self):
        print("You are currrent balance is : ",self.balance)


print("---------------------saving acccount-----------------------------")

class saving(Account):

    def deposite(self,amount):
        self.balance += amount

    def withdrow(self, amount):
        if amount > self.balance:
            print("Insufficeinet balance ... ")
        else:
            self.balance -= amount


print("---------------------loan acccount-----------------------------")


class Loan(Account):
    def deposite(self, amt):
        self.balance-=amt
    
    def withdrow(self, amt):
        self.balance+=amt

s = saving()
s.getbalance()
s.deposite(125000)
s.getbalance()
s.withdrow(120000)
s.getbalance()

print("------------loan account---------------")

l = Loan()
l.getbalance()
l.withdrow(100000)
l.getbalance()
l.deposite(500000)
l.getbalance()