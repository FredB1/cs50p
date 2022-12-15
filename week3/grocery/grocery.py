menu = dict()
while True:
    try:
        val = input("").strip().upper()
        temp =menu[val]
        menu.update({val:temp+1})
        
    except KeyError:
        menu.update({val:1})
        
        
    except EOFError:
       for item in sorted(menu.keys()):
           print(menu[item], item)
       break  