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

    

tesla = car('Tesla', 'Model x', 80000, 2018, 'white', 220, True)

richmond = mechanicgarage('Bob', 1500, 0)
# richmond.newTires(tesla,3)

# richmond.changeColor(tesla, 2000)

# richmond.Totalcost(tesla)

# McLaren = supercar('McLaren', 'F1', 1000000, 1961, "red", 231, 627,4000, False)

# italymechanic = mechanicgarage('Dan', 40000, 0)

# italymechanic.newTires(McLaren, 2)






