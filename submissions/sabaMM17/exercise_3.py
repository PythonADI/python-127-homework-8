prices = {"bread": 2.5, "milk": 3.0, "cheese": 9.0}


def print_menu(prices):
    for item, price in prices.items():
        print(f"{item}: {price}")

def cart_total(prices, cart):
    total = 0
    for item, quantity  in cart.items():
        if item in prices:
            total += prices[item] * quantity 
    return total

def cheapest(prices):
    cheapest_item = None
    
    for item, price in prices.items():
        if cheapest_item is None or price < prices[cheapest_item]:
            cheapest_item = item
            
    return cheapest_item

print_menu(prices)
cart = {"bread": 2, "cheese": 1, "apples": 3}
print(cart_total(prices, cart))
print(cart_total(prices, {}))
print(cheapest(prices))
print(cheapest({"tea": 4.0, "coffee": 4.0}))