def patoi(arg):
    try:
        a = int(arg)
    except ValueError:
        return False
    return a


# if __name__ == '__main__':
#     print(patoi(3))
#     print(patoi('Romanes eunt domus'))
#     print(patoi('34b'))
#     print(patoi(-234.59))
#     print(patoi('-234'))