def knapsack(weights, profits, capacity):
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(profits[i - 1] + dp[i - 1][w - weights[i - 1]], dp[i - 1][w])
            else:
                dp[i][w] = dp[i - 1][w]
    
    selected_items = []
    w = capacity
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            selected_items.append(i - 1)
            w -= weights[i - 1]
    
    return dp[n][capacity], selected_items[::-1]

def main():
    with open('BAG.INP', 'r') as file:
        lines = file.readlines()
        capacity = int(lines[0].split()[1])
        weights = []
        profits = []
        for line in lines[1:]:
            w, p = map(int, line.split())
            weights.append(w)
            profits.append(p)
    
    max_profit, selected_items = knapsack(weights, profits, capacity)
    
    print(max_profit)
    print(" ".join(str(x + 1) for x in selected_items))  # Adding 1 to indices to match 1-based indexing

if __name__ == "__main__":
    main()
