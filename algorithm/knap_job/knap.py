def fractional_knapsack(W, profits, weights, n):
    # Calculate profit to weight ratio for each item
    ratio = [(profits[i] / weights[i], weights[i], profits[i]) for i in range(n)]
    
    # Sort items by ratio in descending order
    ratio.sort(key=lambda x: x[0], reverse=True)

    total_profit = 0.0
    items_taken = []

    for r, wt, pr in ratio:
        if W == 0:
            break
        if wt <= W:
            # Take the full item
            total_profit += pr
            W -= wt
            items_taken.append((wt, pr, 1.0))  # Full item
        else:
            # Take fraction of item
            fraction = W / wt
            total_profit += pr * fraction
            items_taken.append((wt, pr, fraction))
            W = 0

    return total_profit, items_taken

def knap2(M,P,W,n):
    R= [[P[i]/W[i],P[i],W[i]] for i in range(n)]
    R.sort(reverse=True)
    L=[]
    maxi = 0 
    for r,p,w in R:
        if M==0: break
        if w<=M : M-=w; maxi+=p ; L.append((w,p,1))
        else: f = M/w ; maxi += p*f ; M-= f*w ; L.append((w,p,f)) 
    return maxi, L


# Example input
max_weight = 50
profits = [60, 100, 120]
weights = [10, 20, 30]
n = len(profits)

# Function call
max_profit, items_selected = fractional_knapsack(max_weight, profits, weights, n)
max_profit2, items_selected2 = knap2(max_weight, profits, weights, n)

# Output
print(f"Maximum profit: {max_profit:.2f}")
print(f"Maximum profit: {max_profit2:.2f}")
for item in items_selected:
    print(item)
for item in items_selected2:
    print(item)
