from random import randint
from account import Account

class House:
    def __init__(self, account):
        
        #Account
        self.account = account
        
        #Switchers
        self.sauna = False
        self.stove = False
        self.lights = False
      
        #who is at home?
        self.people = ['Matti','Tappo','Kalle']  
        
        #temperature monitoring     
        self.temp = {'sauna':90, 'room':30, 'out':10}
        
        # Butler for buss time table search
        self.butler = ["Next 102 -> 11:00 am", "Next 102 -> 12:00 am","Next 102 -> 13:00 am"]              
        
    def getButler(self):
        randomInt = randint(0,2)
        return self.butler[randomInt]
    
    
    
    def getTemp(self):
        randomSauna = randint(30,80)
        randomRoom =  randint(0,26)
        randomOut = randint(-30,30)
        
        self.temp['sauna'] = randomSauna
        self.temp['room'] = randomRoom
        self.temp['out'] = randomOut
        return self.temp
    
    def getPeople(self):
        randomPeople = randint(1,3)
        return self.people[0:randomPeople]
        
    def leaveHouse(self):
        self.account.inHouse = False
        return  self.account.remove(self.account.name)
    
    def enterHouse(self):
        self.poeple.append(self.account.name)
        self.account.inHouse = True
        return self.people
    
    def AccountInHouse(self):    
        return self.account.inHouse
        
    
    
    
    
account = Account('Teemu','salasana')
house = House(account)
print house.getPeople()
print house.getTemp()
print house.getButler()
print house.AccountInHouse()

