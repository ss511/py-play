"""
Find the maximum profit one can have from buying and selling the stock from a list,
where the item denotes the value of the stock. And the buying and selling is allowed only once.
"""


def get_max_profit(stocks):
    n = len(stocks)
    if n == 0:
        return 'Stocks cannot be empty'
    profit = -1

    min_val = stocks[0]

    for i in range(1, n):
        if stocks[i] > min_val:
            profit = max(stocks[i]-min_val, profit)
        else:
            min_val = stocks[i]
        i += 1

    return profit


if __name__ == "__main__":
    stock = [3, 4, 8, 2, 3, 5, 3, 16]
    print("Max profit from purchasing the stock once and selling it is: ", get_max_profit(stock))
