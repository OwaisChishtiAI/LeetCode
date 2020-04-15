class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = []
        bs = None
        buy_bool = False
        for i in range(len(prices) - 1):
            if not buy_bool:
                if prices[i + 1] < prices[i]:
                    pass
                else:
#                     if prices[i]:
#                     print("Bought at: ", prices[i])
                    buy_bool = True
                    bs = prices[i]
            else:
                if prices[i + 1] < prices[i]:
                    buy_bool = False
#                     print("Sold at: ", prices[i])
                    bs = prices[i] - bs
                    profit.append(bs)
                else:
                    pass
        if buy_bool:
#             print("if bs: ", bs)
            if bs != None:
                print(prices[-1], bs)
                if prices[-1] > bs:
                    buy_bool = False
#                     print("Sold at: ", prices[-1])
                    profit.append(prices[-1] - bs)
                else:
                    return sum(profit)
        return sum(profit)
