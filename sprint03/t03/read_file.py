import os

def read_file(filename):
    if os.access(filename,os.R_OK):
        res = open(filename, 'r')
        if res:
            # res = open(filename, 'r')
            res1 = res.read()
            print(f'File "{filename}" has the following message:\n{res1}')
            res.close()
    else: 
        print(f'Failed to read file "{filename}".')



# if __name__ == '__main__':
#     strings = ['sample.txt', 'sample1.txt', 'no_permission.txt']
#     # remove read permissions from one file to check error handling
#     os.chmod('no_permission.txt', 000)
#     for string in strings:
#         read_file(string)
#         print('***')