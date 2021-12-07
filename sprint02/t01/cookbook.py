def search_cookbook(cookbook, recipe, section):
    if recipe in cookbook:
        incert_dict = cookbook.get(recipe)
        if section in incert_dict:
            sec_dict = incert_dict.get(section)
            if sec_dict:
                return sec_dict
        else: 
            return (f'There is no section "{section}" in the "{recipe}" recipe.')
    else:
        return (f'There is no "{recipe}" recipe in the cookbook.')


def test_cookbook(target_cookbook, target_recipe, target_section):
    print(f'Searching for section "{target_section}" '
    f'in recipe "{target_recipe}":')
    print(search_cookbook(target_cookbook, target_recipe, target_section))
    print('---')

# if __name__ == '__main__':
#     cookbook = {
#     'Salmon salad': {
#     'ingredients': ['salmon', 'tomatoes', 'spinach'],
#     'prep time': 15,
#     'directions': 'Cut tomatoes. Mix all ingredients together.'
#     },
#     'Fried eggs': {
#     'ingredients': ['eggs', 'salt', 'black pepper'],
#     'prep time': 5
#     },
#     'Banana smoothie': {
#     'prep time': 10,
#     'nutrition per serving': ['Calories 122', 'Protein 5 g']
#     }
#     }
#     test_cookbook(cookbook, 'Salmon salad', 'directions')
#     test_cookbook(cookbook, 'Fried eggs', 'ingredients')
#     test_cookbook(cookbook, 'Salmon salad', 'nutrition per serving')
#     test_cookbook(cookbook, 'Apple pie', 'prep time')
#     # empty cookbook dict
#     test_cookbook(dict(), 'Tiramisu', 'ingredients')
#     # other data types as keys
#     cookbook = {15: {('1', '0'): 'ten', 'a': 'something'}}
#     test_cookbook(cookbook, 15, ('1', '0'))
#     test_cookbook(cookbook, 7, 'a')