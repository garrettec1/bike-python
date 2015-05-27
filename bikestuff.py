from collections import namedtuple
from math import pi

class Gear:
    def __init__(self, chainring, cog, rim, tire):
        self.chainring = chainring
        self.cog = cog
        self.wheel = Wheel(rim,tire)

    def ratio(self):
        return(chainring / cog)

    def gear_inches(self):
        return(ratio * wheel.diameter)

    Wheel = namedtuple("Wheel", ['rim', 'tire'])
    def diameter():
        return(Wheel.rim + (Wheel.tire *2))

#main
bike = Gear(52,11, 26, 1.5x)
print(bike.ratio)
