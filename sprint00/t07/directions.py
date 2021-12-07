a = input('There are 3 signs in front of you. Which one would you like to read? ')

if (a == 'right'):
    print('The right sign says: "DEAD PEOPLE ONLY"')
elif a == 'left':
    print('The left sign says: "BEWARE!"')
elif a == 'middle':
    print('The middle sign says: "CERTAIN DEATH"')
else:
    print('There is no', a, 'sign')