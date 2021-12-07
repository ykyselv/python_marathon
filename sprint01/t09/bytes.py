def convert_to_bytes(num, bol, str):
    num = int(num)
    if bol == "True":
        bol = True
    else:
        bol = False

    # print(type(bol), bol)

    b_num = bytes(num)
    print(f'-- The int value is "{num}"\nbytes: "{b_num}"')
    b_bol = bytes(bol)
    print(f'-- The bool value is "{bol}"\nbytes: "{b_bol}"')
    b_str = str.encode()
    print(f'-- The string value is "{str}"\nbytes: "{b_str}"')


# if __name__ == '__main__':
#     convert_to_bytes('10', 'False', 'aaa')
#     print('******')
#     convert_to_bytes('5', 'True', 'Are you suggesting that coconuts migrate?')