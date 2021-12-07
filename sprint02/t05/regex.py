import re

def check_address(dict):
    res = []
    exp = r'^Ukraine,\s\D+\d{1,6},\s\d{5}'
    for key in dict:
        result = re.search(exp, dict[key])
        if result:
            res.append(f"The address of {key} is valid")
        else:
            res.append((f"The address of {key} is invalid"))
    return (res)



# dictionary = {
#     'Dmitry Chaykin': ' Ukraine , Kyiv , Dorohozhytska 3, 04119 ',
#     'Andrey Myskin': 'Ukraine, Lviv, volodymyra velykoho 52, 79053',
#     'Tatyana Tsareva': 'Ukraine, Kyiv , Mykola Grinchenko 4, 03038',
#     'Zhanna Akopyan': 'Ukraine, Kharkiv, 23 August 33, 61000',
#     'Viktor Vasilyev': 'Ukraine, 5 Pasternaka Street Lviv 79000',
#     'Andrey Sharov': '271 Akademika Pavlova Street, Kharkiv, Ukraine',
# }

# if __name__ == '__main__':
#     print(*check_address(dictionary), sep='\n')
# run_random_tests()
