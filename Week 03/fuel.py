while True:
    try:
        #Fraction in strings then splits at "/" sign
        x, y = input("Fraction: ").split("/")
        #Conversion in integer
        x = int(x)
        y = int(y)

        if y == 0:
            raise ZeroDivisionError("")

        if x < 0 or y < 0:
            raise ValueError("")

        #Formula for percentage
        f1 = round(x * 100 / y)

        if x > y:
            raise ValueError("")

        #Booleans to check the ints
        if f1 <= 1:
            print("E")
            break
        elif f1 >= 99:
            print("F")
            break
        else:
            print(f"{f1}%")
            break

    #Exceptions which can be occured
    except ZeroDivisionError:
        pass

    except ValueError:
        pass
