menu = dict()
while True:
    try:
        val = input("").strip().upper()
        temp =menu[val]
        menu.update({val:temp+1})
        
    except KeyError:
        menu.update({val:1})
        sorted(menu.items())
        
    except EOFError:
       for item in menu:
           print(menu[item], item)
       break  