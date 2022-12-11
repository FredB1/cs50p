list = {}
while True:
    try:
        val = input("").upper()
        if val not in list:
            list[val] = 1
        else:
            print(list[val])
        list = sorted(list)
    except EOFError:
        for item in list:
            print(list[item], item )