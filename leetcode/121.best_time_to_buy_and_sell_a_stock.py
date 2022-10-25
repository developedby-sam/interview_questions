def maxProfit(prices):
    left, right = 0, 1
    max_profit = 0

    # Loop unitl the end of the price list
    while right < len(prices):

        # If next day price is greater than today, it is a profitable option
        if prices[right] > prices[left]:

            # get the maximum profit
            profit = prices[right] - prices[left]
            max_profit = max(max_profit, profit)

        # If nexd day price is lower than today's price
        else:
            left = right

        right += 1

    return max_profit