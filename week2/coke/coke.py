can = 50
coins = { 25, 10, 5}
while can >0:
    print(f"Amount Due: {can}")
    if can ==0:
        break
    coin = int(input("Insert Coin: "))
    if coin in coins:
        can -= coin
if can < 0:
    print(f"Change Owed: {can * -1}")
else:
    print(f"Change Owed: 0")