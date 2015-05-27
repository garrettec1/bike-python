from math import pi

class Gear():
    def __init__(self, chainring, cog, wheel):
        self.chainring = chainring
        self.cog = cog
        self.wheel = wheel

    def ratio(self):
        return(self.chainring / self.cog)

    def gear_inches(self):
        return(self.ratio() *(wheel.diameter())


class Wheel():
    def __init__(self, rim, tire):
        self.rim = rim
        self.tire = tire

    def diameter(self):
        return(self.rim +(self.tire * 2))

    def circumference(self):
        return(self.rim * math.pi)

#main
#args 52 11 26 1.5
wheel = Wheel(26,1.5)
bike = Gear(52,11,wheel)
print(bike.ratio())
print(bike.gear_inches())
