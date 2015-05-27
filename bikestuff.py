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


class Wheel:
    def __init__(self, rim, tire):
        self.rim = rim
        self.tire = tire

    #Wheel = namedtuple("Wheel", [rim, tire])
    def diameter(self):
        return(self.rim +(self.tire * 2))
    def circumference(self):
        return(self.rim * math.pi)

#main
bike = Gear(52,11, 26, 1.5x)
print(bike.ratio)
