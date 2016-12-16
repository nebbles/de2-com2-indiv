import os
import settings
from terminaltables import *


class colour:  # defines a variable grouping for formatting print outputs
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


def clear_screen():  # Defines how to clear screen based on platform OS
    if settings.platform_current == 'Windows':
        os.system('cls')
    elif settings.platform_current == 'Darwin':
        os.system('clear')
    else:
        print("\n" * 100)


def debug_screen():  # Debug window giving information about the program and user state
    clear_screen()
    print colour.bold + colour.yellow + "DEBUG MODE" + colour.end
    print ""
    print colour.cyan + "Author " + colour.end + "Benedict Greenberg"
    print colour.cyan + "Course " + colour.end + "Design Engineering MEng, Imperial College London"
    print colour.cyan + "Module " + colour.end + "DE2 Computing 2: Individual Assignment"
    print colour.cyan + "Topic " + colour.end + "Flights to the ISS"
    print ""
    print colour.cyan + "Operating system " + colour.end + settings.platform_current
    print colour.cyan + "Default file name " + colour.end + settings.default_filename
    print ""
    print colour.cyan + "Import preview " + colour.end + str(settings.import_preview)
    print ""
    raw_input(colour.green+"[Press ENTER to continue]"+colour.end)


def print_table(data):  # print a table to the console using terminaltables
    table = SingleTable(data)
    print table.table


def debug_print_all(data):  # dump print all data - for debugging before terminaltables
    for line in data:
        print line


