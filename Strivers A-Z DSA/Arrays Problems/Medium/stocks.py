def stocks(price):
    min_val = 0
    max_prof = 0

    for i in range(1,len(price)):
        for j in range(i):
            if price[i] > price[j] and price[i] - price[j] > max_prof:
                max_prof = price[i] - price[j]
                # min_val = price[j]

    return max_prof

# Time - O(n^2) & Space - O(1)

def stocks_opt(price):
    min_price = float('inf')
    max_prof = 0

    for p in price:
        if p < min_price:
            min_price = p
        elif max_prof < p - min_price:
            max_prof = p - min_price

    return max_prof

# Time - O(n) & Space - O(1)

price_by_day = [7,1,5,3,6,4]
print(stocks_opt(price_by_day))