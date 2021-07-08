from cs50 import get_float
# Getting input from the user
while True:
    dollars = get_float("Change owed: ")
    if dollars > 0:
        break
    
# Converts dollars to cents
cents = dollars * 100
# Counts the number of coins
numberOfCoins = 0

while cents >= 25:
    numberOfCoins = numberOfCoins + 1
    cents = cents - 25
while cents >= 10:
    numberOfCoins = numberOfCoins + 1
    cents = cents - 10
while cents >= 5:
    numberOfCoins = numberOfCoins + 1
    cents = cents - 5
while cents >= 1:
    numberOfCoins = numberOfCoins + 1
    cents = cents - 1
print(numberOfCoins)