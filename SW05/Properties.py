class Point:

    def __init__(self, xPos, yPos):
        self._xPos = xPos # attribute name self._yPos = yPos

    @property # ’getter’ of the property 
    def xPos(self):
        return self._xPos
    
    @xPos.setter # ’setter’ of the property 
    def xPos(self, value):
        if not 0<=value<1000:
            print(f"Value out of range: {value}.") 
        self._xPos = value


p1 = Point(2, 5) 
print(p1.xPos) # calls ’getter’ 
p1.xPos = 125 # calls ’setter’
p1.xPos = p1.xPos + 125 # first calls ’getter’, then ’setter’