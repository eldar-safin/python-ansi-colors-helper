from .ansi_codes import ANSICode


class Color:
    code = ''

    def __init__(self, s):
        self.s = str(s)

    def __str__(self):
        return self.code + self.s + ANSICode.RESET


class Grey(Color):
    code = ANSICode.GREY


class Red(Color):
    code = ANSICode.RED


class Green(Color):
    code = ANSICode.GREEN


class Yellow(Color):
    code = ANSICode.YELLOW


class Blue(Color):
    code = ANSICode.BLUE


class Purple(Color):
    code = ANSICode.PURPLE


class Cyan(Color):
    code = ANSICode.CYAN


class White(Color):
    code = ANSICode.WHITE


class Message(Color):
    pass


class Debug(Message):
    code = ANSICode.WHITE


class Info(Message):
    code = ANSICode.BLUE


class Warn(Message):
    code = ANSICode.YELLOW


class Error(Message):
    code = ANSICode.RED


class Font(Color):
    pass


class Bold(Font):
    code = ANSICode.BOLD


class Underline(Font):
    code = ANSICode.UNDERLINE
