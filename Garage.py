class garage:
    def __init__(self, capacity):
        self.capacity = 0

    def garage_capacity(self,capacity):
        if self.capacity < 4:
            return f"You have too many cars in the garage!"
        else:
            return f"You have enough cars!"