# def do_op (a,b,c):
#     if b!="+" and b!="-" and b!="*" and b!="/":
#         return "usage: the operator must be '*' or '+' or '-' or '/'"
#     else:
#         if b == "+":
#             return a+c
#         elif b == "-":
#             return a-c
#         elif b == "*":
#             return a*c
#         elif b == "/":
#             return a/c
# print("---- Simple calculator ----")
# print("Let's add some numbers")
# a = int(input("Input your first value: "))
# b = input("Input your operator: ")
# c = int(input("Input your second value: "))
# print(a,"+",c, "=", do_op(a,b,c))
# print("---- Simple calculator ----")

print("---- Simple calculator ----")
print("Let's add some numbers")
a = int(input("Input your first value: "))
b = input("Input your operator: ")
if  b!="+" and b!="-" and b!="*" and b!="/":
    print("usage: the operator must be '*' or '+' or '-' or '/'")
else:  
    c = int(input("Input your second value: "))
    if b=="+":
        print(f"{a}{b}{c} = {a+c}")
    elif b=="-":
        print(f"{a}{b}{c} = {a-c}")
    elif b=="*":
        print(f"{a}{b}{c} = {a*c}")
    elif b=="/":
        print(f"{a}{b}{c} = {a/c}")
print("---- Simple calculator ----")
