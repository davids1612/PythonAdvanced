class Point:

    def __init__(self, xPos, yPos):
        self._xPos = xPos
        self._yPos = yPos
    def __add__(self, other): 
        return Point(self._xPos + other._xPos, self._yPos + other._yPos)
    def __eq__(self, other):
        if not isinstance(other, Point): return False 
        return self._xPos == other._xPos and self._yPos == other._yPos
    def __str__(self):
        return f"Point({self._xPos}, {self._yPos})"

    
p1 = Point(1, 2); p2 = Point(1, 2) 
p3 = p1 + p2
print(p3) # Output: Point(2, 4) print(p1 == p2) # Output: True (without __eq__: False) 
print(p1 is p2) # Output: False (but p1 == p1) is True