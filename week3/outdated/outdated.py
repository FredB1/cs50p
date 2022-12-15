months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
while True:
    try:
        date = input("Date: ")
        if "/" in date:
            date = date.split("/")
        elif " " in date:
            date = date.split(" ")
            date[0]= months.index(date[0])+1
            
            if "," in date[1]:
                
                date[1]= int(date[1].replace(",",""))
            else:
                raise ValueError
        else:
            raise ValueError 
        if int(date[1])>31 or int(date[0])>12:
            raise ValueError
    except Exception as e:
        print(e)
    else:
        print(f"{int(date[2])}-{int(date[0]):02}-{int(date[1]):02}")
        break
    