while True:
    try:
        val = input("Fraction: ").split("/")
        x = int(val[0])
        y = int(val[1])
        frac = round((x/y)*100)
        if frac > 100:
            raise ValueError
    except(ValueError, ZeroDivisionError):
        pass
    else:
        if frac <= 1:
            print(f"E")
        elif frac >= 99:
            print(f"F")
        else:
            print(f"{frac}%")
        break