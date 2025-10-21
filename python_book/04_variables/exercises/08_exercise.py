balance            = 1000.00
compound_interest  = 1.05
years              = 5

year_one   = 1000 * compound_interest
# print(year_one)
year_two   = year_one * compound_interest
# print(year_two)
year_three = year_two * compound_interest
# print(year_three)
year_four  = year_three * compound_interest
# print(year_four)
balance    = year_four * compound_interest
print(balance)

# balance += (1.05 * 5)
# print(balance)
# balance = ((1000 * 1.05) * 5) / 1000
balance = 1000.00 * 1.05 * 1.05 * 1.05 * 1.05 * 1.05
print( balance )