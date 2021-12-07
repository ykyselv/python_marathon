import sys
from string import ascii_uppercase

class Redirect:
    def __init__(self, path, stream):
        self.path = path
        self.stream = stream
        self.o = sys.stdout
        self.e = sys.stderr

    def __enter__(self):
        self.file = open(self.path,'a')
        if self.stream == 'o':
            sys.stdout = self.file
        if self.stream == 'e':
            sys.stderr = self.file
        if self.stream == 'oe':
            sys.stdout = self.file
            sys.stderr = self.file
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_value:
            print('exit exception text: %s' % exc_value)
            return True
        sys.stdout = self.o
        sys.stderr = self.e

        self.file.close()


# if __name__ == '__main__':
#     path = 'test.txt'
#     letter = iter(ascii_uppercase)
#     print(next(letter), '[out]')
#     print(next(letter), '[err]', file=sys.stderr)
#     with Redirect(path, 'o'):
#         print(next(letter), '[out]', 'in Redirect')
#     print(next(letter), '[err]', 'in Redirect', file=sys.stderr)
#     print(next(letter), '[out]')
#     print(next(letter), '[err]', file=sys.stderr)
#     with Redirect(path, 'e'):
#         print(next(letter), '[out]', 'in Redirect')
#     print(next(letter), '[err]', 'in Redirect', file=sys.stderr)
#     print(next(letter), '[out]')
#     print(next(letter), '[err]', file=sys.stderr)
#     with Redirect(path, 'oe'):
#         print(next(letter), '[out]', 'in Redirect')
#     print(next(letter), '[err]', 'in Redirect', file=sys.stderr)
#     print(next(letter), '[out]')
#     print(next(letter), '[err]', file=sys.stderr)