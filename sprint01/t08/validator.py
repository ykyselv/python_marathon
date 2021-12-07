def validator(argv_str):
    argv = argv_str.split(' ')
    try:
        argv[0] = float(argv[0])
        argv[2] = float(argv[2])
    except ValueError:
        return False
    except IndexError:
        return False

    if argv[1] == '>':
        if argv[0]>argv[2]:
            return True
        elif argv[0]<argv[2]:
            return f"{argv[0]} < {argv[2]}"
        elif argv[0] == argv[2]:
            return f"{argv[0]} == {argv[2]}"
    elif argv[1] == '<':
        if argv[0]<argv[2]:
            return True
        elif argv[0]>argv[2]:
            return f"{argv[0]} > {argv[2]}"
        elif argv[0] == argv[2]:
            return f"{argv[0]} == {argv[2]}"
    elif argv[1] == '>=':
        if argv[0]>=argv[2]:
            return True
        elif argv[0]<=argv[2]:
            return f"{argv[0]} <= {argv[2]}"
        elif argv[0] == argv[2]:
            return f"{argv[0]} == {argv[2]}"
        
    elif argv[1] == '<=': 
        if argv[0]<=argv[2]:
            return True
        elif argv[0]>=argv[2]:
            return f"{argv[0]} >= {argv[2]}"
        elif argv[0] == argv[2]:
            return f"{argv[0]} == {argv[2]}"
    
    elif argv[1] == '==':
        if argv[0]==argv[2]:
            return True
        elif argv[0]>=argv[2]:
            return f"{argv[0]} >= {argv[2]}"
        elif argv[0] <= argv[2]:
            return f"{argv[0]} <= {argv[2]}"
    else:
        return False

# print(validator("4 < 6"))
# print(validator('4 > 6'))
# print(validator('4 > 4'))
# print(validator('6 < 6'))
# print(validator('4 > '))
# print(validator('4 6'))
# print(validator('4 . 6'))
# print(validator('4 == 6'))
# print(validator('4 >= 6'))

