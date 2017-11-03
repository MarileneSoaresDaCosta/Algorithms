def maxProfit(prices):
    n = len(prices)
    sell = prices[n-1]
    sell_ind = n-1
    buy = prices[0]
    buy_ind = 0
    
   
    for i in range(1, n-1):
        # price went up
        if prices[i] > prices[i-1] and sell_ind > buy_ind:  
            sell = prices[i]
            print 'prices[i]' , prices[i], 'prices[i-1]' , prices[i-1]
           
            

            # price came down
            
        elif prices[i] < prices[i-1] and sell_ind > buy_ind: 
            buy = prices[i]
            print 'buy', buy
    maxp = sell - buy
    print 'sell at: ', sell, 'buy at: ', buy, 'profit: '
    return {'sell at: ': sell, 'buy at: ': buy, 'max profit: ': maxp }    
    


#Testing

print maxProfit([10, 7, 5, 8, 11, 9])

print maxProfit([10, 9, 8, 7, 6, 5])

print maxProfit([10, 19, 28, 37, 46, 55])