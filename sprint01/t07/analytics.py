def print_str_analytics(str):
    printable = 0
    alphanumeric = 0 
    alphabetic = 0
    decimal = 0
    lowercase = 0 
    uppercase = 0
    whitespace = 0

    for elem in str:
        if elem.isprintable() == True:
            printable+= 1
        if elem.isalnum() == True:
            alphanumeric+= 1
        if elem.isalpha() == True:
            alphabetic+= 1
        if elem.isdecimal() == True:
            decimal+= 1
        if elem.islower() == True:
            lowercase+= 1
        if elem.isupper() == True:
            uppercase+= 1
        if elem.isspace() == True:
            whitespace+= 1

#     print(f"|------------------------------------------------|\n\
# |               String analytics                 |\n\
# |------------------------------------------------|\n\
# | '{str}'\n\
# |------------------------------------------------|\n\
# | Number of printable characters is: {printable}\n\
# | Number of alphanumeric characters is: {alphanumeric}\n\
# | Number of alphabetic characters is: {alphabetic}\n\
# | Number of decimal characters is: {decimal}\n\
# | Number of lowercase letters is: {lowercase}\n\
# | Number of uppercase letters is: {uppercase}\n\
# | Number of whitespace characters is: {whitespace}\n\
# |------------------------------------------------|")
#     # print(printable, alphanumeric, alphabetic, decimal, lowercase, uppercase, whitespace)



# print_str_analytics('NI')
