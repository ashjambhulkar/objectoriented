def knapsack(profits, weights, capacity):
  
  dp = [[0 for _ in range(capacity+1)] for _  in range(len(weights)+1)]

  for i in range(1, len(weights)+1):
    for j in range(1, capacity+1):
      if weights[i-1] <= j:
        dp[i][j] = max(dp[i-1][j], dp[i-1][j-weights[i-1]]+profits[i-1])
      else:
        dp[i][j] = dp[i-1][j]
  
  return dp[-1][-1]

  


profits = [1, 6, 10, 16]
weights = [1, 2, 3, 5]
capacity = 7

print(knapsack(profits, weights, capacity))
