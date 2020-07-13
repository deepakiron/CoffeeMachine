# Write your code here
class coffee_machine:
    def __init__(self,water,milk,beans,cups,money):
        self.water=water
        self.milk=milk
        self.beans=beans
        self.cups=cups
        self.money=money
    def status(self):
        print("The coffee machine has:")
        print(self.water,"of water")
        print(self.milk,"of milk")
        print(self.beans,"of coffee beans")
        print(self.cups,"of disposable cups")
        print(self.money,"of money")
    def make_coffee(self,water=0,beans=0,milk=0,money=0):
        if self.water<water:
            print("Sorry, not enough water!")
        elif self.milk<milk:
             print("Sorry, not enough milk!")
        elif self.beans<beans:
            print("Sorry, not enough coffee beans!")
        elif self.cups<1:
            print("Sorry, not enough cups!")
        else:
            self.water-=water
            self.milk-=milk
            self.beans-=beans
            self.money+=money
            self.cups-=1
    def buy(self,coffee):
        if coffee==1:
            self.make_coffee(water=250,beans=16,money=4)
        elif coffee==2:
            self.make_coffee(water=350,milk=75,beans=20,money=7)
        else:
            self.make_coffee(water=200,milk=100,beans=12,money=6)
    def fill(self):
        print("Write how many ml of water do you want to add:")
        self.water+=int(input())
        print("Write how many ml of milk do you want to add:")
        self.milk+=int(input())
        print("Write how many grams of coffee beans do you want to add:")
        self.beans+=int(input())
        print("Write how many disposable cups of coffee do you want to add:")
        self.cups+=int(input())
    def start(self):
        exit=False
        while not exit:
            print("Write action (buy, fill, take, remaining, exit):")
            action=input()
            if action=="buy":
                print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
                coffee=input()
                if coffee=="back":
                    continue
                coffee=int(coffee)
                self.buy(coffee)
            elif action=="fill":
                self.fill()
            elif action=="take":
                print("I gave you $",self.money,sep="")
                self.money=0
            elif action=="remaining":
                self.status()
            else:
                exit=True
water=400
milk=540
beans=120
cups=9
money=550
machine=coffee_machine(water,milk,beans,cups,money)
machine.start()
