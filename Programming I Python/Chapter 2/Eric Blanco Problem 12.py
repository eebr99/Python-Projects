#write a program that displays money paid for stock and paid to broker,
#the amount the stock sold for and amount of commission paid after sell
#and the amount of money left after stock was sold and dues were paid

#Buying the stock

shares_bought = int(2000)
buy_price = float(40.00)
buy_commission = (shares_bought * buy_price) * .03
print('Joe paid $', shares_bought * buy_price, 'for the stock.')
print('Joe paid his broker $', buy_commission, 'when he bought the stock.')


#Selling the stock

shares_sold = int(2000)
sell_price = float(42.75)
sell_commission = (shares_sold * sell_price) * .03
print('Joe sold the stock for $', shares_sold * sell_price)
print('Joe paid his broker $ ', sell_commission, 'when he sold the stock.')

#Profit or not?

money_left = ((shares_sold * sell_price) - (buy_commission + sell_commission)) - (shares_bought * buy_price)
print('After buying and selling his stock and paying his broker both times, Joe made $', money_left)
      

