
def extractor(ext, value_type):
    a = filter(lambda x: isinstance(list(x)[1], value_type),ext.items())
    return dict(a)


# brian = {
#     'name': 'Brian',
#     'email': 'very_naughty_boy@gmail.com',
#     'age': 33,
#     'star_sign': 'Capricorn',
#     'legs': 2,
#     'arms': 2.5
# }


# print(f'***\nbrian, str: {extractor(brian, int)}')





