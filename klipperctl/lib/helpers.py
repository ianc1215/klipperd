from colors import color


def info(message):
    return color(message, fg='blue')


def warn(message):
    return color(message, fg='yellow')


def error(message):
    return color(message, fg='red')
