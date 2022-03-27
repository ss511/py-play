"""
Unbounded Knapsack (Repetition of items allowed)
Given a knapsack weight W and a set of n items with certain value val[i] and weight wt[i],
we need to calculate the maximum amount that could make up this quantity exactly.
This is different from classical Knapsack problem, here we are allowed to use unlimited number of instances of an item.
Examples

Input : W = 100
       val[]  = {1, 30}
       wt[] = {1, 50}
Output : 100
There are many ways to fill knapsack.
1) 2 instances of 50 unit weight item.
2) 100 instances of 1 unit weight item.
3) 1 instance of 50 unit weight item and 50
   instances of 1 unit weight items.
We get maximum value with option 2.

Input : W = 8
       val[] = {10, 40, 50, 70}
       wt[]  = {1, 3, 4, 5}
Output : 110
We get maximum value with one unit of
weight 5 and one unit of weight 3.
"""


def unbounded_knapsack(w, n, val, wt):
    dp = [0 for i in range(w+1)]

    for i in range(1, w+1):
        for j in range(n):
            if wt[j] <= i:
                dp[i] = max(dp[i], dp[i-wt[j]] + val[j])
    return dp[w]


if __name__ == "__main__":
    print(unbounded_knapsack(100, 2, [1, 30], [1, 50]))
    print(unbounded_knapsack(8, 4, [10, 40, 50, 70], [1, 3, 4, 5]))
