from vehicle import vehicle
class car(vehicle):
    def __init__(self, make, name, speed, price, year, color,autopilot):
        super().__init__(make,name,price,year,color)
        self.speed = speed
        self.autopilot = bool(autopilot)

    def Maxspeed(self):
        if self.speed > 160:
            print('Wow this is too fast for me')
        else:
            print('This is just perfect speed for me')
        
    def Autopilot(self):
        if self.autopilot == False:
            print('Ok no autopilot its fine')
        else:
            print('Wow it has auto pilot nap time!')

