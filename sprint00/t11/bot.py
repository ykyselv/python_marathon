first_str = input("Enter your first string: ")
sec_str = input("Enter your second string: ")
com_list = ['find','concat','beatbox']

if first_str == "" or sec_str == "":
    print('One of the strings is empty.')

else:
    command = input("Enter your command: ")
    if command not in com_list:
        print("usage: command find | concat | beatbox")
    elif command == "find":
        if sec_str in first_str:
            print("True")
        else:
            print("False")
    elif command == "concat":
        print(f"{first_str} {sec_str}")
    elif command == "beatbox":
        first_num = int(input("Enter your first beatbox number: ")) 
        sec_num = int(input("Enter your second beatbox number: "))
        print(first_num*first_str + sec_num*sec_str)