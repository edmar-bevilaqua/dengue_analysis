def print_with_colors(msg: str, color: str, end: str = "\n") -> None:
    """
    Prints a message in the specified color using ANSI escape codes.
    :param msg: The message to print.
    :param color: The color to print the message in. Supported colors are:
                  'black', 'red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white'.
    """
    colors = {
        "black": "\033[30m",
        "red": "\033[31m",
        "green": "\033[32m",
        "yellow": "\033[33m",
        "blue": "\033[34m",
        "magenta": "\033[35m",
        "cyan": "\033[36m",
        "white": "\033[37m",
    }
    reset_color = "\033[0m"

    c_code = colors.get(color.lower())

    if c_code:
        print(f"{c_code}{msg}{reset_color}", end=end)
    else:
        print(f"(Warning: Color '{color}' not found. printing with default color.)")
        print(msg, end=end)