import sys
from variants.class_ import *
from variants.decorator import *


def main():
    print(Yellow(Bold('Class-based variant:')),
          '\n',
          Grey('Grey color'),
          Red('Red color'),
          Green('Green color'),
          Yellow('Yellow color'),
          Blue('Blue color'),
          Purple('Purple color'),
          Cyan('Cyan color'),
          White('White color'),
          '\n',
          Debug('Debug message'),
          Info('Info message'),
          Warn('Warning message'),
          Error('Error message'),
          '\n',
          Bold('Bold font'),
          Underline('Underline font'))

    print()

    print(yellow(bold('Decorator-based variant')),
          '\n',
          grey('Grey color'),
          red('Red color'),
          green('Green color'),
          yellow('Yellow color'),
          blue('Blue color'),
          purple('Purple color'),
          cyan('Cyan color'),
          white('White color'),
          '\n',
          debug('Debug message'),
          info('Info message'),
          warning('Warning message'),
          error('Error message'),
          '\n',
          bold('Bold font'),
          underline('Underline font'))


if __name__ == '__main__':
    sys.exit(main())
