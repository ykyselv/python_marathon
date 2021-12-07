import math

def buy_milk(money = None):
    if not money:
        money = 0
        return None
    product = '[milk]'
    price = 25
    multiplicator = math.floor(money/price) 
    if multiplicator == 0:
        return None
    return (multiplicator*product)


def buy_bread(money = None):
    if not money:
        money = 0
        return None
    product = '[bread]' 
    price = 19
    multiplicator = math.floor(money/price)
    if multiplicator == 0:
        return None
    if multiplicator > 3:
        multiplicator = 3
    return (multiplicator*product)


# if __name__ == '__main__':
# # money = price of 1 item
#     print(f'Buy milk with $25, result: {buy_milk(25)}')
#     print(f'Buy bread with $19, result: {buy_bread(19)}')
#     # no money
#     print(f'Buy milk with nothing, result: {buy_milk()}')
#     print(f'Buy bread with nothing, result: {buy_bread()}')
#     # a lot of money
#     print(f'Buy milk with $200, result: {buy_milk(200)}')
#     print(f'Buy bread with $200, result: {buy_bread(200)}')
#     # money < price of item   
#     print(f'Buy milk with $10, result: {buy_milk(10)}')
#     print(f'Buy bread with $10, result: {buy_bread(10)}')
#     # more tests
#     print(f'Buy milk with $53, result: {buy_milk(53)}')
#     print(f'Buy bread with $53, result: {buy_bread(53)}')
#     print(f'Buy milk with $100, result: {buy_milk(100)}')
#     print(f'Buy bread with $100, result: {buy_bread(100)}')
