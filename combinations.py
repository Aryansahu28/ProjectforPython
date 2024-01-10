def find_combinations(price,denominations,current_combination=[]):
    if price == 0:
        print(current_combination)
        return
    if price<0 or not denominations:
        return
    
    print(current_combination)
    find_combinations(price,denominations[1:],current_combination.copy())
    find_combinations(price-denominations[0],denominations,current_combination+[denominations[0]])


price = 50
denominations = [10, 20, 50]

print(f"Possible combinations for {price} rupees:")
find_combinations(price, denominations)