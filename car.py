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

# toyota = car('Toyota','Tocoma',5000, 2005, 'blue', 130, False)
# tesla = car('Tesla', 'Model x', 80000, 2018, 'white', 220, True)

# toyota.Maxspeed()

# tesla.Maxspeed()

# toyota.Autopilot()

# tesla.Autopilot()


