from sys import exit
def main():
    val = (input("Fraction: ").split("/"))
    percentage = convert(val)
    print(gauge(percentage))
def convert(str):
    while True:
        try:
            
            x = int(str[0])
            y = int(str[1])
            frac = round((x/y)*100)
            if frac > 100:
                raise ValueError
        except(ValueError, ZeroDivisionError) as e:
            raise e
        else:
            return frac
def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"

if __name__ == "__main__":
    main()