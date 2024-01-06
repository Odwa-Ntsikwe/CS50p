amount_due = 50
coins_allowed = [25, 10, 5]

while amount_due > 0:
    print("Amount Due:", amount_due)
    coin = int(input("Insert Coin: "))
    if coin in coins_allowed:
        amount_due -= coin
change_owed = abs(amount_due)
print("Change Owed:", change_owed)
