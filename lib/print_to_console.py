import os
import settings


class colour:
    purple = '\033[95m'
    cyan = '\033[96m'
    darkcyan = '\033[36m'
    blue = '\033[94m'
    green = '\033[92m'
    yellow = '\033[93m'
    red = '\033[91m'
    bold = '\033[1m'
    underline = '\033[4m'
    end = '\033[0m'


def clear_screen():
    if settings.platform_current == 'Windows':
        os.system('cls')
    elif settings.platform_current == 'Darwin':
        os.system('clear')
    else:
        print("\n" * 100)


def debug_screen():
    clear_screen()
    print colour.bold + colour.yellow + "DEBUG MODE" + colour.end
    print colour.cyan + "Author " + colour.end + "Benedict Greenberg"
    print colour.cyan + "Course " + colour.end + "Design Engineering MEng, Imperial College London"
    print colour.cyan + "Topic " + colour.end + "Flights to the ISS"
    print colour.cyan + "Operating system " + colour.end + settings.platform_current
    print colour.cyan + "Default file name " + colour.end + settings.default_filename
    print ""
    raw_input(colour.green+"[Press ENTER to continue]"+colour.end)

def debug_print_all(data):
    for line in data:
        print line


