#!/usr/bin/env python3.5
import math

def count_change_function(amount: int, is_reverse=False):
	coins = [25, 10, 5, 1]
	counter = 0
	if(is_reverse):
		coins.reverse()
	for coin in coins:
		number_of_coins_ = int(math.floor(amount/coin)*100)/100
		counter+=number_of_coins_
		amount-=(coin*number_of_coins_)
	return counter
# reversing the list will count the most amount of coins needed for a given total
# normal iteration will yield the least amount of coins
for i in range(0, 100):
	print("amount: {}".format(i))
	print("number of coins: {}".format(count_change_function(i, False)))
