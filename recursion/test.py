def hammer_profit(cost, prices):
    # Base case: if the prices list is empty, return 0
    if not prices:
        return 0

    # Calculate profit for the first price
    profit = prices[0] - cost

    # If the profit is positive, include it; otherwise, add 0

    return profit + hammer_profit(cost, prices[1:])



# Test cases
print(hammer_profit(15.00, [14.00, 15.00, 17.00]))  # Output: 1.0
print(hammer_profit(20.00, [19.00, 18.00, 23.00, 22.50, 15.00, 25.00]))  # Output: 2.5
