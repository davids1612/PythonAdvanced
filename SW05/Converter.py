class Converter:
    _INCH_TO_CM = 2.54

    @staticmethod
    def cm_to_inches(cm):
        return cm / Converter._INCH_TO_CM

    @staticmethod
    def inches_to_cm(inches):
        return inches * Converter._INCH_TO_CM

    def __str__(self):
        return "hello world"

    


#print(Converter.inches_to_cm(10)) # Output: 25.4 
#print(Converter.cm_to_inches(25.4)) # Output: 10.0


c1 = Converter()
print(c1)
