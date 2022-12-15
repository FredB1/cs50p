mess = "Adieu, adieu, to "
list = []
while True:
    try:
        list.append(input("Name: ").title())
    except EOFError:
        print("")
        break
if len(list) == 1:
    mess += list[0]
elif len(list) == 2:
    mess += " and ".join(list)
elif len(list) >2:
    list[-1]= "and "+ list[-1]
    mess += ", ".join(list)
print(mess)