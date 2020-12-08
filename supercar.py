from vehicle import vehicle 

class supercar(vehicle):
    def __init__(self, make, name, price, year, color,speed,Horsepower,NumbOfUnits,autopilot):
        super().__init__(make,name,price,year,color)
        self.Horsepower = Horsepower
        self.__NumbofUnits = NumbOfUnits
# This method lets you add more horspoer to your supercar!
    def addHorsepower(self,horsepower):
        self.horsepower  = self.horsepower + horsepower
        print(f'Your cars total horspower is {self.horsepower}!')
#This method checks for the number of units that ypur car has been made and evaluates its rarity
    def rarityCheck(self):
        if self.__NumbofUnits in range(5000):
            print('Wow your Car is really rare!')
        else:
            print('Your car is still really cool!')
# This method retrievs info about your car with extra added instances
    def getInfo(self):
        print(f'Your {self.make} {self.name} {self.color} {self.year} with {self.Horsepower}HP with only {self.__NumbofUnits} units in the world is worth {self.price}')
        return


Ferrari = supercar("Ferrari", '250 GT SWB California Spyder', 10000000, 1961, "Red",350,380,9000, False)

# McLaren = supercar('McLaren', 'F1', 1000000, 1961, "red", 231, 627,4000, False  )

# Ferrari.getInfo()

# McLaren.SupercargetInfo()

# McLaren.rarityCheck()

# Ferrari.rarityCheck()

# Ferrari.priceloss()
# McLaren.priceloss()

# Ferrari.SupercargetInfo()

# McLaren.getInfo()

