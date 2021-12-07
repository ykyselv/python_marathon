def write_file(filename, message = 'None'):
    if filename.endswith('.txt'):
        with open(filename,'w') as file:
            file.write(message)
    else:
        print(f'Please enter the filename in the format "filename.txt".\nFailed to write to file "{filename}".')
        return

    with open(filename,'r') as res:
            result = res.read()
            if result != message:
                print('Something went wrong...')
                return
            else:
                print(f'Your message has been written to file "{filename}".\nFile "{filename}" now contains the following text:\n{message}')


# if __name__ == '__main__':
#     write_file('file')
#     print('***')
#     write_file('file.txt')
#     print('***')
#     write_file('file', 'Hello there')
#     print('***')
#     write_file('new_file.txt', 'Hello there')
#     print('***')
#     # check with a non-empty file
#     write_file('example.txt', 'A new message')
#     print('***')

