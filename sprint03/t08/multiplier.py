import functools

def multiplier(data):
    if all([type(x) is int or type(x) is float for x in data]) and type(data) == list:
        return functools.reduce(lambda x,y: x*y, data)
    else:
        raise ValueError('The given data is invalid.')


# print(multiplier([2.72,43,4]))
# print(multiplier([22,3.04,26]))
# print(multiplier({"1":6,"2": 7, "3":5}))


