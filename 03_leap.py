def leap(year):
    if (year % 4 == 0) and (year % 100 != 0):
        return True

    elif (year % 4 == 0) and (year % 100 == 0) and (year % 400 == 0):
        return True

    else:
        return False


year = int(input("Enter the number : "))
a = leap(year)
print(a)
