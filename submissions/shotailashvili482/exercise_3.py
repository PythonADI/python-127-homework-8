prices = {'bread': 2.5,
          'milk': 3.0,
          'cheese': 9.0,
          }

def print_menu(prices):
    for food,price in prices.items():
        print(f'{food}: {price}')

def cart_total(prices, cart):
    total = 0
    for food,quantity in cart.items():
        if food not in prices:
            continue
        else:
            total += quantity * prices[food]
    return total

def cheapest(prices):
    cheapest = ''
    for food, price in prices.items():
        if cheapest == '' or price < prices[cheapest]:
            cheapest = food
    return cheapest
                

print_menu(prices)
cart = {'bread': 2, 'cheese': 1, 'apples': 3,}
print(cart_total(prices, cart))
print(cart_total(prices, {}))
print(cheapest(prices))
print(cheapest({'tea': 4.0, 'coffee': 4.0,}))
