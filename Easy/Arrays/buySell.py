class BestTimeToBuy():
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        i = 0
        profit = 0
        while i < len(prices) -1 : 
            if prices[i] < prices [i+1] :
               profit = profit +  (prices[i+1] - prices[i])
            i = i + 1

        return profit


bestTimeToBuy = BestTimeToBuy()
maxProfit = bestTimeToBuy.maxProfit(prices=[1,2,3,4,5])

print(maxProfit)