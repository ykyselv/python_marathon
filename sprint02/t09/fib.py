def fib(num):
    if num < 2:
        return num
    else:
        return fib(num-1)+fib(num-2)

def fib_generator(num):
    for i in range(num):
        yield fib(i)


# if __name__ == '__main__':
#     n = 20
#     print(f'The number under the index {n} is {fib(20)}')
#     print('***')
#     n = 5
#     print(f'The number under the index {n} is {fib(5)}')
#     print('***')
#     for i, n in enumerate(fib_generator(5)):
#         print(f'Fibonacci number for {i} is {n}')
#     print('***')
#     for i, n in enumerate(fib_generator(10)):
#         print(f'Fibonacci number for {i} is {n}')
#     print('***')
