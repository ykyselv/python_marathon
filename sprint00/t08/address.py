first_var = 1000
second_var = first_var
third_var = 999
fourth_var = third_var + 1


print("first_var =",first_var,end = ","),
print(" address is", id(first_var))
print("second_var =",second_var,end = ",")
print(" address is", id(second_var))
print("third_var =",third_var, end = ",")
print(" address is", id(third_var))
print("fourth_var =",fourth_var, end = ",")
print(" address is", id(fourth_var))
print(first_var, "is", second_var, first_var is second_var)
print(first_var, "is", third_var, first_var is third_var)
print(first_var, "is", fourth_var, first_var is fourth_var)