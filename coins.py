
"""
  If we know the last coin added, we can simply subtract the value of the coin to find a previous entry in the table that tells us the last coin we added to make that amount. We can keep tracing back through the table until we get to the beginning.
"""



def dpMakeChange(coinValueList,change,minCoins,coinsUsed):
   for cents in range(change+1):
      coinCount = cents
      newCoin = 1
      for j in [c for c in coinValueList if c <= cents]:
            # print 'j', j
            if minCoins[cents-j] + 1 < coinCount:
               # print 'mincoin cents-j+1 < coinCount'
               coinCount = minCoins[cents-j]+1
               newCoin = j
      minCoins[cents] = coinCount
      coinsUsed[cents] = newCoin
   print 'minCoins: ', minCoins  
   return minCoins[change]


""" printCoins walks backward through the table to print out the value of each coin used."""

def printCoins(coinsUsed,change):
   coin = change
   while coin > 0:
      thisCoin = coinsUsed[coin]
      print(thisCoin)
      coin = coin - thisCoin


"""
The first two lines of main set the amount to be converted and create the list of coins used. The next two lines create the lists we need to store the results: 
   == coinsUsed is a list of the coins used to make change,
   == coinCount is the minimum number of coins used to make change for the amount corresponding to the position in the list.
"""

def main():
    amnt = 16
    clist = [1, 5, 10, 21, 25]
    coinsUsed = [0]*(amnt+1)
    coinCount = [0]*(amnt+1)



    print("Making change for",amnt,"requires")
    print(dpMakeChange(clist,amnt,coinCount,coinsUsed),"coins")
    print("They are:")
    printCoins(coinsUsed,amnt)
    print("The used list is as follows:")
    print(coinsUsed)

main()



