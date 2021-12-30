class car_class():
    """

    |--------------------------------------------------------------------
    |                                                                   |
    |   car Class                                                     |
    |                                                                   |
    |--------------------------------------------------------------------
    |                                                                   |
    |   1 - initial Class with title, time, function, address, price    |
    |                                                                   |
    |   2 - return class property as list                               |
    |                                                                   |
    ---------------------------------------------------------------------

    """

    # ? -> 1 
    def __init__(self, title, time, function, address, price, carLink):
        self.title = title
        self.time = time
        self.function = function
        self.address = address
        self.price = price
        self.carLink = carLink

    # ? -> 2 
    def getPropertyList(self):
        proplist = []
        proplist.append(self.title)
        proplist.append(self.time)
        proplist.append(self.function)
        proplist.append(self.address)
        proplist.append(self.price)
        proplist.append(self.carLink)
        return proplist