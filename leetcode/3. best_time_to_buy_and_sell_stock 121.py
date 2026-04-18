# BEST TIME TO BUY AND SELL STOCK:

#Algorithm:

"""
1.start
2.set min_price to a very large number (infinity)
3. set maxprofit to 0
4.loop through each price in the list:
    *if current price is less than min price:
        update minprice to current price(this means we found a better day to buy)
    *else:
        calculate profit=current price -minprice (this means we sell today)
    *if profit > maxprofit:
        update maxprofit to current profit
5.after the loop ends:
  return maxprofit

"""

def maxProfit(prices):
    min_price = float('inf')
    max_profit = 0
    for price in prices:
        if price < min_price:
            min_price = price
        else:
            profit = price - min_price
            max_profit = max(max_profit, profit)
    return max_profit
print(maxProfit([7,1,5,3,6,4]))
print(maxProfit([7,6,4,3,1]))



"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

Example 1:
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

Example 2:
Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.

"""