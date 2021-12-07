def crystal_ball(courage, intelligence):
    if courage > 50 and intelligence > 50:
        print ("I see great success in your future.")
    elif courage >= 100 or intelligence <=10:
        print ("Your life is in danger!")
    else:
        print ("Your future is a mystery...")


def print_result(courage, intelligence):
    print(f"Reading the future for an adventurer with {courage} courage"
        f"and {intelligence} intelligence...")
    crystal_ball(courage, intelligence)
    print('***')

# if __name__ == '__main__':
#     print_result(19, 0)
#     print_result(57, 60)
#     print_result(200, 79)
#     print_result(150, 15)
#     print_result(30, 100)
#     print_result(100, 25)
#     print_result(50, 55)
#     print_result(50, 9)
