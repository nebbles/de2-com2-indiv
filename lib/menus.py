import print_to_console
from print_to_console import colour
import change_data
import os
import settings
from terminaltables import *


def get_window_width():
    rows, columns = os.popen('stty size', 'r').read().split()
    format_code = '{:^' + columns + '}'
    return format_code, columns


def main_menu():
    while True:
        print_to_console.clear_screen()
        format_code, columns = get_window_width()

        print colour.blue
        print format_code.format("ISS Flights")
        print colour.end

        percentage = 0.46
        print " " * int(percentage * float(columns)) + "1. [D] Database" + "\n"
        print " " * int(percentage * float(columns)) + "2. [I] Import" + "\n"
        print " " * int(percentage * float(columns)) + "3. [E] Export" + "\n"
        print " " * int(percentage * float(columns)) + "4. [A] Add new entries" + "\n"
        print " " * int(percentage * float(columns)) + "5. [R] Remove entries" + "\n"
        print " " * int(percentage * float(columns)) + "   [Q] Quit" + "\n"

        while True:
            choice = raw_input("\nPlease type in a menu option (name/ID/number): ")

            invalid_choice = colour.red+colour.bold+choice+colour.end+colour.red+" is an invalid input. " \
                                                                                 "Please use the menu number, " \
                                                                                 "ID letter, or option name as an " \
                                                                                 "input."+colour.end
            if choice == '':
                break
            choice.lower()

            if choice == '1' or choice == 'd' or choice == 'database':
                database_menu()
                break
            elif choice == '2' or choice == 'i' or choice == 'import':
                import_menu()
                print colour.bold + "IMPORT" + colour.end + " is currently not available"
                # break
            elif choice == '3' or choice == 'e' or choice == 'export':
                export_menu()
                print colour.bold + "EXPORT" + colour.end + " is currently not available"
                # break
            elif choice == '4' or choice == 'a' or choice == 'add new entries':
                add_data_menu()
                print colour.bold + "ADD DATA" + colour.end + " is currently not available"
                # break
            elif choice == '5' or choice == 'r' or choice == 'remove entries':
                remove_data_menu()
                print colour.bold + "REMOVE DATA" + colour.end + " is currently not available"
                # break
            elif choice == 'q' or choice == 'quit':
                quit_menu()
                break
            else:
                print invalid_choice

def database_menu():
    while True:
        print_to_console.clear_screen()
        format_code, columns = get_window_width()

        print colour.green
        print format_code.format("Database")
        print colour.end

        print format_code.format("Type '..' or 'back' to return to previous menu." + "\n")
        percentage = 0.46
        print " " * int(percentage * float(columns)) + "1. [A] All data" + "\n"
        print " " * int(percentage * float(columns)) + "2. [S] Search data" + "\n"
        print " " * int(percentage * float(columns)) + "   [Q] Quit" + "\n"

        while True:
            choice = raw_input("\nPlease type in a menu option (name/ID/number): ")

            invalid_choice = colour.red + colour.bold + choice + colour.end + \
                             colour.red + " is an invalid input. Please use the menu number, " \
                                          "ID letter, or option name as an input." + colour.end
            if choice == '':
                break
            choice.lower()
            if choice == 'back' or choice == '..':
                return

            if choice == '1' or choice == 'a' or choice == 'all data':
                table = SingleTable(settings.data)
                print table.table
                raw_input(colour.green+"[Press ENTER to go back to the menu]"+colour.end)
                break
            elif choice == '2' or choice == 's' or choice == 'search data':
                print colour.bold + "SEARCH" + colour.end + " is currently not available"
                # break
            elif choice == 'q' or choice == 'quit':
                quit_menu()
                break
            else:
                print invalid_choice

def import_menu():
    while True:
        print_to_console.clear_screen()
        format_code, columns = get_window_width()

        print colour.green
        print format_code.format("Import")
        print colour.end

        print format_code.format("Type '..' or 'back' to return to previous menu." + "\n")
        print "Please input the file name (including extension .csv) of the data you would like to import."
        print "If the file is not in the same working directory as run.py, please provide the full path."

        while True:
            filename = raw_input("\nFile name: ")

            invalid_choice = colour.red + colour.bold + filename + colour.end + \
                             colour.red + " is an invalid input. Please use the menu number, " \
                                          "ID letter, or option name as an input." + colour.end
            if choice == '':
                break
            choice.lower()
            if choice == 'back' or choice == '..':
                return

            if choice == '1' or choice == 'a' or choice == 'all data':
                table = SingleTable(settings.data)
                print table.table
                raw_input(colour.green+"[Press ENTER to go back to the menu]"+colour.end)
                break
            elif choice == '2' or choice == 's' or choice == 'search data':
                print colour.bold + "SEARCH" + colour.end + " is currently not available"
                # break
            elif choice == 'q' or choice == 'quit':
                quit_menu()
                break
            else:
                print invalid_choice

def export_menu():
    pass
    # readwrite.export_data(data)

def add_data_menu():
    pass
    # change_data.add_data(settings.data)

def remove_data_menu():
    pass

def quit_menu():
    while True:
        print colour.yellow + "\nAre you sure you want to exit?"
        print "\t[N]\t No, do not exit."
        print "\t[Y]\t Yes, exit without saving."
        print "\t[S]\t Yes, exit "+colour.bold+"and save changes."+colour.end
        yesno = raw_input()
        yesno.lower()

        if yesno == '':
            pass
        elif yesno == 'n' or yesno == 'no':
            return
        elif yesno == 'y' or yesno == 'yes':
            sys.exit()
        elif yesno == 's' or yesno == 'save':
            print colour.green + "Saving data" + colour.end
            readwrite.export_data(settings.data)
            sys.exit()
