initial_investment = 1000
profit_per_day = 3
number_of_days = 150

final_money = initial_investment

for i in range(number_of_days):
	final_money = final_money + (final_money*profit_per_day/100.)

# final_money = final_money + (final_money*profit_per_day/100.)
print(final_money)