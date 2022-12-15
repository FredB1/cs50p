import random
from sys import exit

def main():
    score = 0
    level = get_level()
    for x in range(10):
        intx = generate_integer(level)
        inty = generate_integer(level)
        count = 0
        while True:
            try:
                attempt = int(input(f"{str(intx).zfill(level)} + {str(inty).zfill(level)} ="))
                if (attempt == intx+inty) and count<1:
                    score+=1
                if (attempt == intx+inty):
                    break
                if attempt != intx+inty:
                    raise ValueError
            except ValueError:
                count +=1
                if count >=3:
                    print(intx+inty)
                    exit()
                print("EEE")         
    print(score)
def get_level():
    while True:
        try:
            thing= int(input("Level: "))
            if thing <1 or thing>3:
                raise ValueError
        except:
            pass
        else:
            return thing
def generate_integer(level):
    if level ==1:
        return random.randint(0,9)
    else:
        return random.randint(int(.1*pow(10,level)),int(9.9*pow(10,level-1)))
if __name__ == "__main__":
    main()
