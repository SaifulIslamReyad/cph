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

# **Algorithm** FractionalKnapsack(W, profits, weights, n)

# // Solves the fractional knapsack problem by greedy selection
# // Returns:
# //   - total_profit: Maximum profit achievable
# //   - items_taken: List of selected items with their fractions

# {
#     // Calculate profit-to-weight ratio for each item
#     ratio := empty list;
#     for i from 0 to n-1 do:
#         Append (profits[i]/weights[i], weights[i], profits[i]) to ratio;

#     // Sort items by ratio in descending order
#     Sort ratio by ratio[0] (profit-to-weight) in non-increasing order;

#     total_profit := 0.0;
#     items_taken := empty list;

#     // Select items greedily
#     for each (r, wt, pr) in ratio do:
#         if W = 0 then:
#             break;
#         if wt ≤ W then:
#             // Take the entire item
#             total_profit := total_profit + pr;
#             W := W - wt;
#             Append (wt, pr, 1.0) to items_taken;  // Full item
#         else:
#             // Take a fraction of the item
#             fraction := W / wt;
#             total_profit := total_profit + (pr * fraction);
#             Append (wt, pr, fraction) to items_taken;
#             W := 0;

#     return (total_profit, items_taken);
# }

# Example input
max_weight = 50
profits = [60, 100, 120]
weights = [10, 20, 30]
n = len(profits)

# Function call
max_profit, items_selected = fractional_knapsack(max_weight, profits, weights, n)

# Output
print(f"Maximum profit: {max_profit:.2f}")
for item in items_selected:
    print(item)
