def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    money = True
    if '.' in s:
        money = False
        return money
    if s[0:2].isalpha():
        True
    else: 
        money = False
        return money
    if len(s) <=5 and len(s)>=2:
        money = True
    else: 
        money = False
        return money
    if s.isalnum():
        money =True
    else: 
        money = False
        return money
        
    for c in range(len(s)):
         if s[c].isnumeric():
             if s[c]=="0":
                if c +1 <len(s):
                     money =False
                     return money                
             money = s[c:].isnumeric()
    
    return money


if __name__ == "__main__":
    main()