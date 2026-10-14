age = 0
try:
    age = int(input("Age: "))
    xfactor = 10 / age
#except ValueError as ex:
#    print("not valid age")
#except ZeroDivisionError :
#    print("cannot be 0")


except (ValueError, ZeroDivisionError):
    print("not working")
else:
    print("only when no exception")

print(age)