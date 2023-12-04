import sys
from decorator import *


def main():
    print(grey('Grey color'))
    print(red('Red color'))
    print(green('Green color'))
    print(yellow('Yellow color'))
    print(blue('Blue color'))
    print(purple('Purple color'))
    print(cyan('Cyan color'))
    print(white('White color'))
    print()
    print(debug('Debug message'))
    print(info('Info message'))
    print(warning('Warning message'))
    print(error('Error message'))
    print()
    print(bold('Bold font'))
    print(underline('Underline font'))


if __name__ == '__main__':
    sys.exit(main())
