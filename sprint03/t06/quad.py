import json
import math


def quad(a, b, c):
    result = dict()

    if isinstance(a, (int,float)) and isinstance(b, (int,float)) and isinstance(c, (int,float)) and a!=0:
        discriminant = b**2 - 4*a*c 
        if discriminant < 0:
            x1 = None
            x2 = None
        else:
            x1 = (-b + math.sqrt(discriminant))/(2*a)
            x2 = (-b - math.sqrt(discriminant))/(2*a)
        if x1 == -0:
            x1 = 0.0
        if x2 == -0:
            x2 = 0.0


        if x1 == x2:
            fin_x = x1
        else:
            fin_x = [x1,x2]


        if b == 0 and c != 0 :
            if a == 1:
                pattern = f'x^2+{c}'
            else:    
                pattern = f'{a}x^2+{c}'
        elif c == 0 and b != 0:
            if a == 1:
                pattern = f'x^2+{b}x'
            else:    
                pattern = f'{a}x^2+{b}x'
        elif b == 0 and c == 0:
            if a == 1:
                pattern = f'x^2'
            else:
                pattern = f'{a}x^2'
        else:
            if a == 1:
                pattern = f'x^2+{b}x+{c}'
            else:    
                pattern = f'{a}x^2+{b}x+{c}'


        result["equation"] = pattern
        result["solution"] = dict()
        result["solution"]["discriminant"] = discriminant
        result["solution"]["x"] = fin_x
       
        with open('file.json', 'w') as file:
            json.dump(result, file,indent = 3)
    else:
        print ('Cannot generate a quadratic equation.')
    with open('file.json', 'r') as f:
        rrrr = f.read()
    return rrrr

from quad import quad
from random import seed, randint

def run_test(a, b, c):
        print(f'---\n{a}, {b}, {c}')
        print(quad(a, b, c))
# if __name__ == '__main__':
#     run_test(1, 0, 0)
#     run_test(-7.5, 0, 0)
#     run_test(120, -1, 0)
#     run_test(15, 1.8, 1)
#     run_test(1, 4, 4)
#     run_test(1, 5, 6)
#     run_test('a', 5, 6)
#     run_test(0, 1, 2)
#     seed(5)
# for _ in range(3):
    # run_test(randint(-20, 20), randint(-20, 20), randint(-20, 20))