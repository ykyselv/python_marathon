def make_unique(dictionary):
    for key in dictionary:
        unique = sorted(list(set(dictionary[key])))
        dictionary[key]= unique
    return dictionary



# test_case_1 = {
#     "city": ['Kharkiv', 'Kyiv', 'Lviv', 'Dnipro', 'Kyiv', 'Kyiv', 'Kharkiv',
#     'Kharkiv', 'Lviv'],
#     "age": [16, 16, 17, 18, 19, 19, 19, 18, 20],
# }

# test_case_2 = {
#     "hobby": ['drawing', 'basketball', 'drawing', 'drawing', 'basketball',
#     'dancing', 'dancing', 'dancing', 'dancing'],
#     "format": ['individually', 'individually', 'group', 'individually', 'group',
#     'individually', 'group', 'group', 'group'],
# }

# print(make_unique(test_case_1))
# print(make_unique(test_case_2))
