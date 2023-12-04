class Colors:
    GREY = '\033[90m'
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'

    DEBUG = WHITE
    INFO = BLUE
    WARNING = YELLOW
    ERROR = RED

    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

    RESET = '\033[0m'


def complete(func):
    def wrapper(*args, **kwargs) -> str:
        return func(*args, **kwargs) + args[0] + Colors.RESET
    return wrapper


@complete
def grey(s: str):
    return Colors.GREY


@complete
def red(s: str):
    return Colors.RED


@complete
def green(s: str):
    return Colors.GREEN


@complete
def yellow(s: str):
    return Colors.YELLOW


@complete
def blue(s: str):
    return Colors.BLUE


@complete
def purple(s: str):
    return Colors.PURPLE


@complete
def cyan(s: str):
    return Colors.CYAN


@complete
def white(s: str):
    return Colors.WHITE


@complete
def debug(s: str):
    return Colors.DEBUG


@complete
def info(s: str):
    return Colors.INFO


@complete
def warning(s: str):
    return Colors.WARNING


@complete
def error(s: str):
    return Colors.ERROR


@complete
def bold(s: str):
    return Colors.BOLD


@complete
def underline(s: str):
    return Colors.UNDERLINE
