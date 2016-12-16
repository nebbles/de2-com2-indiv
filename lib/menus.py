# Import standard modules
import sys
import os
import time

# Import private modules
import settings
import print_to_console
from print_to_console import colour
import readwrite
import database


def get_window_width():  # Get the width of the terminal window, this is for centering text
    rows, columns = os.popen('stty size', 'r').read().split()
    format_code = '{:^' + columns + '}'
    return format_code, columns


def main_menu():  # main menu is opening page for program
    while True:
        print_to_console.clear_screen()  # clear screen
        format_code, columns = get_window_width()  # get centre point of window

        print colour.blue  # formatting tags
        print format_code.format("ISS Flights")  # title
        print colour.end

        percentage = 0.46  # push over a left aligned string from left side
        print " " * int(percentage * float(columns)) + "1. [D] Database" + "\n"
        print " " * int(percentage * float(columns)) + "2. [I] Import" + "\n"
        print " " * int(percentage * float(columns)) + "3. [E] Export" + "\n"
        print " " * int(percentage * float(columns)) + "4. [A] Add new entries" + "\n"
        print " " * int(percentage * float(columns)) + "   [Q] Quit" + "\n"

        while True:
            choice = raw_input(colour.darkcyan + "\nPlease type in a menu option (name/ID/number): " + colour.end)
            invalid_choice = colour.red+colour.bold+choice+colour.end+colour.red+" is an invalid input. " \
                                                                                 "Please use the menu number, " \
                                                                                 "ID letter, or option name as an " \
                                                                                 "input."+colour.end

            if choice == '': break  # if enter key is pressed without input then refresh screen
            choice = choice.lower()  # remove case sensitivity by converting input to lower case

            # launch different menu based on input
            if choice == '1' or choice == 'd' or choice == 'database':
                interactive_data()
                break
            elif choice == '2' or choice == 'i' or choice == 'import':
                import_menu()
                break
            elif choice == '3' or choice == 'e' or choice == 'export':
                export_menu()
                break
            elif choice == '4' or choice == 'a' or choice == 'add new entries':
                readwrite.add_data()
                break
            elif choice == 'q' or choice == 'quit':
                quit_menu()
                break
            else:
                print invalid_choice


## THIS IS AN OUTDATED DATABASE MENU
# def database_menu():
#     while True:
#         print_to_console.clear_screen()
#         format_code, columns = get_window_width()
#
#         print colour.green
#         print format_code.format("Database")
#         print colour.end
#
#         print format_code.format("Type '..' or 'back' to return to previous menu." + "\n")
#         percentage = 0.46
#         print " " * int(percentage * float(columns)) + "1. [A] All data" + "\n"
#         print " " * int(percentage * float(columns)) + "2. [I] Interactive data" + "\n"
#         print " " * int(percentage * float(columns)) + "3. [S] Search data" + "\n"
#         print " " * int(percentage * float(columns)) + "   [Q] Quit" + "\n"
#
#         while True:
#             choice = raw_input(colour.darkcyan + "\nPlease type in a menu option (name/ID/number): " + colour.end)
#
#             invalid_choice = colour.red + colour.bold + choice + colour.end + \
#                 colour.red + " is an invalid input. Please use the menu number, " \
#                 "ID letter, or option name as an input." + colour.end
#             if choice == '':
#                 break
#             choice = choice.lower()
#             if choice == 'back' or choice == '..':
#                 return
#             elif choice == 'q' or choice == 'quit':
#                 quit_menu()
#                 break
#
#             elif choice == '1' or choice == 'a' or choice == 'all data':
#                 print_to_console.clear_screen()
#                 print_to_console.print_table(settings.data)
#                 raw_input(colour.green+"[Press ENTER to go back to the menu]"+colour.end)
#                 break
#             elif choice == '2' or choice == 'i' or choice == 'interactive data':
#                 # print colour.bold + "INTERACT" + colour.end + " is currently not available"
#                 interactive_data()
#                 break
#
#             elif choice == '3' or choice == 's' or choice == 'search data':
#                 print colour.bold + "SEARCH" + colour.end + " is currently not available"
#                 # break
#
#             else:
#                 print invalid_choice


def interactive_data():
    while True:
        print_to_console.clear_screen()
        format_code, columns = get_window_width()

        print colour.green
        print format_code.format("Interactive database")
        print colour.end
        print format_code.format("Type '..' or 'back' to return to previous menu." + "\n")
        print ""

        print colour.purple + colour.bold + "Database fields"
        print "=" * len("Database fields") + colour.end

        field_number = 1
        for title in settings.data[0]:  # print out a column field list for reference
            print colour.purple + str(field_number) + "  " + title + colour.end
            field_number += 1

        while True:
            choice = raw_input(colour.darkcyan + "\nPlease type in an interaction command (or 'help'): " + colour.end)

            invalid_choice = colour.red + colour.bold + choice + colour.end + \
                colour.red + " is an invalid input. Type " + colour.bold + "help" + colour.end + colour.red \
                             + " for more information." + colour.end

            if choice == '': break  # refresh if no input
            choice_original = choice  # save a back up of original input
            choice = choice.lower()  # remove case sensitivity
            if choice == 'back' or choice == '..': return  # return to previous menu
            elif choice == 'q' or choice == 'quit':  # jump to quit sequence function
                quit_menu()
                break
            elif choice == 'h' or choice == 'help':  # provide a help widget
                interactive_data_help()

            elif choice.startswith('all'):
                print_to_console.print_table(settings.data)  # use print_table to print all from global data variable

            elif choice.startswith('sort by'):  # if interactive command starts with sort by
                sort_parameters = choice[len('sort by '):]  # extract everything after sort by
                sort_parameters = sort_parameters.split()  # split extraction into individual words

                if len(sort_parameters) == 1:  # only 1 parameter was input (a column number)
                    columns = range(1, len(settings.data[0]) + 1)  # list of column numbers
                    try:
                        cnum = int(sort_parameters[0])  # get column number
                        if cnum in columns:  # if column number is in possible column numbers
                            sorted_data = database.sort_data(cnum)  # sort the data by column
                            print_to_console.print_table(sorted_data)  # print the sorted data in table
                        else:
                            print invalid_choice  # catch invalid inputs
                    except ValueError:
                        print invalid_choice

                elif len(sort_parameters) == 2:  # two parameters passed in
                    order = sort_parameters[1]  # second parameter should be 'reversed'
                    columns = range(1, len(settings.data[0])+1)
                    try:
                        cnum = int(sort_parameters[0])
                        if cnum in columns and order == 'reversed':
                            sorted_data = database.sort_data(cnum, 'reversed')  # sort data in reversed format
                            print_to_console.print_table(sorted_data)  # print data in a table
                        else:
                            print invalid_choice  # catch invalid inputs
                    except ValueError:
                        print invalid_choice

                else:
                    print invalid_choice

            elif choice.startswith('average'):  # if average command is called
                average, duration = database.average_duration()  # get the average and then print
                print colour.green + "\nThe average duration of mission from this database is " + colour.bold \
                      + str(average) + " minutes" + colour.end
                print colour.green + "That's an average mission time of " + colour.bold + str(duration) + colour.end

            elif choice.startswith('min'):  # if min command is called
                sort_parameters = choice[len('min '):]  # get parameters of command
                if len(sort_parameters) == 1:  # as long as only parameter was passed in
                    try:
                        cnum = int(sort_parameters[0])
                        payload = database.stat_data(cnum, 'min')  # get the min of the data based on column input

                        print_info = [settings.data[0], payload]  # combine the headers to the collected data
                        print_to_console.print_table(print_info)  # print into a table
                    except ValueError:
                        print invalid_choice  # catch errors
                else:
                    print invalid_choiceb

            elif choice.startswith('max'):  # same as min but for max
                sort_parameters = choice[len('max '):]
                if len(sort_parameters) == 1:
                    try:
                        cnum = int(sort_parameters[0])
                        payload = database.stat_data(cnum, 'max')

                        print_info = [settings.data[0], payload]
                        print_to_console.print_table(print_info)
                    except ValueError:
                        print invalid_choice
                else:
                    print invalid_choice

            elif choice.startswith('filter'):
                parameters = choice[len('filter '):]  # extract parameters from command
                parameters = parameters.split()  # split parameters into words

                if parameters[1] == 'from':  # if first parameter correctly is from
                    first_p = []
                    second_p = []
                    index1 = parameters.index('from')
                    index2 = parameters.index('to')
                    for p in range(index1+1, index2):
                        first_p.append(parameters[p])
                    for p in parameters[index2+1:]:
                        second_p.append(p)
                    first_p = " ".join(first_p)  # get the words in between 'from' and 'to' and then combine into one
                    second_p = " ".join(second_p)  # get the words after 'to' and then combine into one

                    try:
                        column_key = int(parameters[0])
                        minkey = expand_digits(first_p)  # ensure that the keys are correctly formatted as 3 digit str
                        maxkey = expand_digits(second_p)

                        print_info = database.get_interval(column_key, minkey, maxkey)  # get interval using keys
                        print_to_console.print_table(print_info)
                    except:
                        print invalid_choice
                else:
                    print invalid_choice

            elif choice.startswith('search'):  # same as filter
                parameters = choice_original[len('search '):]
                parameters = parameters.split()

                if parameters[1].lower() == 'for':
                    first_p = []
                    index1 = parameters.index('for')
                    for p in parameters[index1 + 1:]:
                        first_p.append(p)
                    first_p = " ".join(first_p)  # get words after the for keyword and combine into one parameter
                    print first_p

                    try:
                        column_key = int(parameters[0])
                        minkey = expand_digits(first_p)
                        maxkey = minkey  # make the min key the same as the max key

                        print_info = database.get_interval(column_key, minkey, maxkey)  # returns values with same key
                        print_to_console.print_table(print_info)
                    except:
                        print invalid_choice
                else:
                    print invalid_choice

            else:
                print invalid_choice


def interactive_data_help():  # print a help widget for guiding the user
    print ""
    title1 = colour.yellow + colour.bold + "Command" + colour.end
    title2 = colour.green + colour.bold + "Description" + colour.end
    title3 = colour.purple + colour.bold + "Compatible fields" + colour.end

    a1 = colour.yellow + "all" + colour.end
    a2 = colour.green + " -- this will print all data sorted by No." + colour.end
    a3 = colour.purple + "-" + colour.end

    b1 = colour.yellow + "sort by 'x' [reversed]" + colour.end
    b2 = colour.green + " -- this will produce the database sorted by X ['reversed' keyword will reverse sort]" + colour.end
    b3 = colour.purple + "*Any" + colour.end

    c1 = colour.yellow + "average" + colour.end
    c2 = colour.green + " -- this will return the average of the duration column" + colour.end
    c3 = colour.purple + "Duration" + colour.end

    d1 = colour.yellow + "max 'x'" + colour.end
    d2 = colour.green + " -- this will return the maximum of column X (if valid)" + colour.end
    d3 = colour.purple + "*Any" + colour.end

    e1 = colour.yellow + "min 'x'" + colour.end
    e2 = colour.green + " -- this will return the minimum of column X (if valid)" + colour.end
    e3 = colour.purple + "*Any" + colour.end

    f1 = colour.yellow + "filter 'x' from 'y' to 'z'" + colour.end
    f2 = colour.green + " -- this will filter column X with a range from Y to Z" + colour.end
    f3 = colour.purple + "*Any" + colour.end

    g1 = colour.yellow + "search 'x' for 'y'" + colour.end
    g2 = colour.green + " -- this will filter column X with a range from Y to Z" + colour.end
    g3 = colour.purple + "*Any" + colour.end

    help_table = [[title1, title2, title3], [a1, a2, a3], [b1, b2, b3], [c1, c2, c3],
                                            [d1, d2, d3], [e1, e2, e3], [f1, f2, f3], [g1, g2, g3]]
    print_to_console.print_table(help_table)

    title1 = colour.yellow + colour.bold + "Command parameter" + colour.end
    title2 = colour.green + colour.bold + "Format" + colour.end

    a1 = colour.yellow + "x" + colour.end
    a2 = colour.green + "Must be column number as seen in purple" + colour.end

    b1 = colour.yellow + "y / z" + colour.end
    b2 = colour.green + "Be recognised entry for x field, e.g. a number for column 1" + colour.end

    help_table = [[title1, title2], [a1, a2], [b1, b2]]
    print_to_console.print_table(help_table)


def import_menu():
    while True:
        print_to_console.clear_screen()
        format_code, columns = get_window_width()

        print colour.green
        print format_code.format("Import")
        print colour.end

        print format_code.format("Type '..' or 'back' to return to previous menu." + "\n")
        print format_code.format("[Q] Quit" + "\n")

        print colour.darkcyan+"Please input the file name (including extension .csv) of the data you would like to import."
        print "If the file is not in the same working directory as run.py, please provide the full path."+colour.end

        while True:
            filename = raw_input("\nFile name: ")  # ask for filename

            invalid_filename = colour.red + colour.bold + filename + colour.end + \
                colour.red + " is an invalid filename." + colour.end
            if filename == '':
                break
            elif filename == 'back' or filename == '..':
                return
            elif filename == 'q' or filename == 'quit':
                quit_menu()
                break

            new_data = readwrite.import_data(filename)  # attempt to import new data
            if new_data is None: print invalid_filename  # if import fails then filename was invalid
            else:
                print colour.green + "Data was successfully imported." + colour.end
                if settings.import_preview: print_to_console.print_table(new_data)  # if preview is enabled then it will show
                while True:
                    final = raw_input(colour.yellow+"\nAre you sure you want to overwrite the existing data with "
                                                    "the data from " + colour.bold+filename+" [Y/N] ? "+colour.end)
                    final = final.lower()
                    if final == 'y' or final == 'yes':  # final confirmation of the imported file
                        settings.data = new_data
                        print colour.green + "Data has been overwritten." + colour.end
                        for i in xrange(0, 3):
                            pstring = colour.green + "Returning you to the MAIN MENU in " + str(3 - i) + colour.end
                            sys.stdout.write(pstring)
                            sys.stdout.flush()
                            time.sleep(1)
                            sys.stdout.write('\r')
                        return
                    elif final == 'n' or final == 'no': break
                    else: print colour.red + "Answer must be yes/no" + colour.end
                break


def export_menu():
    while True:
        print_to_console.clear_screen()
        format_code, columns = get_window_width()

        print colour.green
        print format_code.format("Export")
        print colour.end

        print format_code.format("Type '..' or 'back' to return to previous menu." + "\n")
        print format_code.format("[Q] Quit" + "\n")

        print colour.darkcyan+"Please input the file name (including extension .csv) you would like to export to."
        print "The file will save to the same directory as run.py."+colour.end

        while True:
            filename = raw_input("\nFile name: ")

            invalid_filename = colour.red + colour.bold + filename + colour.end + \
                colour.red + " is an invalid filename." + colour.end
            if filename == '':
                break
            elif filename == 'back' or filename == '..':
                return
            elif filename == 'q' or filename == 'quit':
                quit_menu()
                break

            if filename.endswith('.csv'):
                confirmation = raw_input(colour.yellow+"\nAre you sure you want to export the existing data to "
                                                    + colour.bold + filename + " [Y/N] ? " + colour.end)
                confirmation = confirmation.lower()
                if confirmation == 'y' or confirmation == 'yes':
                    readwrite.export_data(filename)
                    print colour.green + "Data has been exported." + colour.end
                    for i in xrange(0, 3):
                        pstring = colour.green + "Returning you to the MAIN MENU in " + str(3 - i) + colour.end
                        sys.stdout.write(pstring)
                        sys.stdout.flush()
                        time.sleep(1)
                        sys.stdout.write('\r')
                    return
                elif confirmation == 'n' or confirmation == 'no':
                    break
                else:
                    print colour.red + "Answer must be yes/no" + colour.end

            else:
                filename = filename + ".csv"
                confirmation = raw_input(colour.yellow + "\nAre you sure you want to export the existing data to "
                                         + colour.bold + filename + " [Y/N] ? " + colour.end)
                confirmation = confirmation.lower()
                if confirmation == 'y' or confirmation == 'yes':
                    readwrite.export_data(filename)
                    print colour.green + "Data has been exported." + colour.end
                    for i in xrange(0, 3):
                        pstring = colour.green + "Returning you to the MAIN MENU in " + str(3 - i) + colour.end
                        sys.stdout.write(pstring)
                        sys.stdout.flush()
                        time.sleep(1)
                        sys.stdout.write('\r')
                    return
                elif confirmation == 'n' or confirmation == 'no':
                    break
                else:
                    print colour.red + "Answer must be yes/no" + colour.end



def quit_menu():
    while True:
        print colour.yellow + "\nAre you sure you want to exit?"
        print "\t[N]\t No, do not exit."
        print "\t[Y]\t Yes, exit without saving."
        print "\t[S]\t Yes, exit "+colour.bold+"and save changes."+colour.end
        yesno = raw_input()
        yesno = yesno.lower()

        if yesno == '':
            pass
        elif yesno == 'n' or yesno == 'no':
            return
        elif yesno == 'y' or yesno == 'yes':
            sys.exit()
        elif yesno == 's' or yesno == 'save':
            readwrite.export_data(settings.data)  # export the data in program to default file, will load on run
            print colour.green + "Data has been saved." + colour.end
            sys.exit()


def expand_digits(string):  # simply ensures that a digit string is formatted with the correct zeroes in front
    while len(string) < 3:
        string = '0'+string
    return string
