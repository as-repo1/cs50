def total(galleons, sickle, knuts):
    return (galleons * 17 + sickle) * 29 + knuts


coins = [100, 50, 25]

# print(total(coins[0],coins[1],coins[2]), "knuts")#before packing

print(total(*coins), "knuts")  # after packing
