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
        self.temperature = {'sauna':90, 'room':30, 'out':10}
        
        # Butler for buss time table search
        self.butler = ["Next 102 -> 11:00 am", "Next 102 -> 12:00 am","Next 102 -> 13:00 am"]              

        #security
        self.alarm = False
        self.doorsLocked = False

    def getButler(self):
        randomInt = randint(0,2)
        return self.butler[randomInt]

    def onOff(self, option):
        if (option == 1):
            self.sauna = not self.sauna;
        if (option == 2):
            self.stove = not self.stove
        if (option == 3):
            self.lights = not self.lights
    
    def getSwitch(self, option):
        if (option == 1):
            return self.sauna;
        if (option == 2):
            return  self.stove
        if (option == 3):
            return self.lights
        return False
    
    
    def getTemperature(self, option):
        randomSauna = randint(30,80)
        randomRoom =  randint(0,26)
        randomOut = randint(-30,30)
        if (option == 0):
            self.temperature['sauna'] = randomSauna
            return self.temperature['sauna']
        elif option == 1: 
            self.temperature['room'] = randomRoom 
            return self.temperature['room']  
        else:
            self.temperature['out'] = randomOut
            return self.temperature['out']
    
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
        
    def flipCoin(self):
        randomInt =  randint(0,1)
        if randomInt == 0:
            return True
        else:
            return False

    def isThere(self, item):
        result = self.flipCoin()
        if result == True:
            return True
        else:
            return False

    def switchAlarmState(self, password):
        if (self.account.password == password):
            if self.alarm == False:
                self.alarm = True
                return 'Alarm is now on'
            else:
                self.alarm = False
                return 'Alarm is now off'
        else:
            return 'Incorrect password'

    def switchDoorState(self):
         if (self.doorsLocked == False):
            self.doorsLocked = True
            return 'Doors are now locked'
         else:
            self.doorsLocked = False
            return 'Doors are now unlocked'

    def getWeather(self):
        return 'Its raining'

    def getJoke(self):
        return 'I told my dad to embrace his mistakes.\nHe cried. Then he hugged my sister and me.'


#account = Account('Teemu','salasana')
#house = House(account)
#print house.getPeople()
#print house.getTemperature(1)
#print house.getButler()
#print house.AccountInHouse()
#print house.getJoke()

