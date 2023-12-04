from .ansi_codes import ANSICode


def complete(func):
    def wrapper(*args, **kwargs) -> str:
        return func(*args, **kwargs) + args[0] + ANSICode.RESET

    return wrapper


@complete
def grey(s: str):
    return ANSICode.GREY


@complete
def red(s: str):
    return ANSICode.RED


@complete
def green(s: str):
    return ANSICode.GREEN


@complete
def yellow(s: str):
    return ANSICode.YELLOW


@complete
def blue(s: str):
    return ANSICode.BLUE


@complete
def purple(s: str):
    return ANSICode.PURPLE


@complete
def cyan(s: str):
    return ANSICode.CYAN


@complete
def white(s: str):
    return ANSICode.WHITE


@complete
def debug(s: str):
    return ANSICode.WHITE


@complete
def info(s: str):
    return ANSICode.BLUE


@complete
def warning(s: str):
    return ANSICode.YELLOW


@complete
def error(s: str):
    return ANSICode.RED


@complete
def bold(s: str):
    return ANSICode.BOLD


@complete
def underline(s: str):
    return ANSICode.UNDERLINE
