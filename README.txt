class vehicle():
    def __init__(self, make, name, price, year, color):
        self.name = name
        self.make = make
        self.year = year
        self.price = price
        self.color = color

# This method returnts the information of the car

    def getInfo(self):
        print(f'Your {self.make} {self.name} {self.color} {self.year} is worth {self.price}')
        return
    # This method is used when you car is getting old and starts losing value
    def priceloss(self):
        if self.year >= 2015:
            self.price -= self.price *.25
        else:
            self.price -= self.price * .15
    # This method just gets the color of the car
    def getcolor(self):
        print(f'your vehicles color is {self.color}')

    from vehicle import vehicle
class car(vehicle):
    def __init__(self, make, name, price, year,color,speed,autopilot):
        super().__init__(make,name,price,year,color)
        self.speed = speed
        self.autopilot = bool(autopilot)
# This method gets the max speed and checks if its too fast
    def Maxspeed(self):
        if self.speed > 160:
            print('Wow this is too fast for me')
        else:
            print('This is just perfect speed for me')
# This method checks if the vehicle has auto pilot      
    def Autopilot(self):
        if self.autopilot == False:
            print('Ok no autopilot its fine')
        else:
            print('Wow it has auto pilot nap time!')



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


from vehicle import vehicle
from car import car
from supercar import supercar

class mechanicgarage():
    def __init__(self,ownername, avgcost, amount):
        self.__ownername = ownername
        self.agcost = avgcost
        self.amount = 0
# This method changes color of vehicle and adds cost
    def changeColor(self, vehicle, cost):
        self.color = input('The price for color change is 2500 what color would u like: ')
        self.amount = self.amount + cost
        cost = "{:.2f}".format(self.amount)
        print(f'You changed your color to {self.color}')
# This method changes new tires and adds to the cost
    def newTires(self, vehicle, tires):
        if vehicle.price < 250000:
            self.amount = tires * 250
        else:
            self.amount = tires * 1000
        print(f'Your total cost is {self.amount} remeber to come back after a 100,000 miles!')
# This method checls the total cost of the work          
    def Totalcost(self, vehicle):
        print(f'Your cost for the total work is {self.amount}')

