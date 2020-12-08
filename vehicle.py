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
