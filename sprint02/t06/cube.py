def cube(num):
    while num>0:
        yield num**3
        num -= 1


# if __name__ == '__main__':
#     val = cube(8)
#     for i in range(8):
#         print(next(val))
