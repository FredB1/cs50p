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
        return
    if s[0:2].isalpha():
        True
    else: money = False
    if len(s) <=6 and len(s)>=2:
        True
    else: money = False
    if s.isalnum():
        True
    else: money = False
    for c in range(len(s)):
         if s[c].isnumeric():
             if s[c]=="0":
                if c +1 <len(s):
                     money =False
                     return                 
             money = s[c:].isnumeric()
    
    return money

main()