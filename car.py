class car():
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

    def priceloss(self):
        if self.year >= 2015:
            self.price -= self.price *.25
        else:
            self.price -= self.price * .15
