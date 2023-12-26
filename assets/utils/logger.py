from colorama import Fore, Back, Style, init

init()


def print_yellow(text: str):
    print(Fore.BLACK + Back.YELLOW + Style.BRIGHT +
          text + Fore.RESET + Back.RESET + Style.RESET_ALL)


def print_cyan(text: str):
    print(Fore.BLACK + Back.CYAN + Style.BRIGHT +
          text + Fore.RESET + Back.RESET + Style.RESET_ALL)


def print_green(text: str):
    print(Fore.BLACK + Back.GREEN + Style.BRIGHT +
          text + Fore.RESET + Back.RESET + Style.RESET_ALL)


def print_magenta(text: str):
    print(Fore.BLACK + Back.MAGENTA + Style.BRIGHT +
          text + Fore.RESET + Back.RESET + Style.RESET_ALL)
