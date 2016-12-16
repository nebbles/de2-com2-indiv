import sys
import time
import csv
import settings
import menus
import print_to_console
from print_to_console import colour


def import_data(filename=settings.default_filename):  # import function using standard csv importing
    try:
        data = []

        with open(filename, 'r') as csvfile:
            reader = csv.reader(csvfile, delimiter=',', quotechar='"')
            for row in reader:
                data.append(row)
                # print row

        csvfile.close()
        return data

    except IOError:
        return None


def export_data(filename):  # export data function based on standard csv exporting
    data_out = settings.data
    with open(filename, 'wb') as csvout:
        wr = csv.writer(csvout, delimiter=',', quotechar='"')
        for row in data_out:
            wr.writerow(row)
    csvout.close()


def add_data():  # special menu item for adding item to database
    while True:
        print_to_console.clear_screen()
        format_code, columns = menus.get_window_width()

        print colour.green
        print format_code.format("Add a new data entry")
        print colour.end

        print format_code.format("Type '..' or 'back' to return to previous menu." + "\n")
        print format_code.format("[Q] Quit" + "\n")

        print colour.darkcyan+"Example:" + colour.end

        example = [settings.data[0], settings.data[5]]  # get an example entry
        print_to_console.print_table(example)  # print an example into a table for reference

        print colour.darkcyan+"New data entry:" + colour.end

        fields = settings.data[0]  # get possible fields names
        new_entry = []

        # Add element number automatically
        item_number = str(len(settings.data))
        item_number = menus.expand_digits(item_number)
        new_entry.append(str(item_number))

        # Add spacecraft
        element = add_data_string(fields[1])
        if element is None: return
        new_entry.append(element)

        # Add the country name
        element = add_data_string(fields[2])
        if element is None: return
        new_entry.append(element)

        # Add the launch date
        element = add_data_date(fields[3])
        if element is None: return
        new_entry.append(element)

        # Add launch time
        element = add_data_time(fields[4])
        if element is None: return
        new_entry.append(element)

        # Add duration
        element = add_data_duration(fields[5])
        if element is None: return
        new_entry.append(element)

        # Add Deorbit date
        element = add_data_date(fields[6])
        if element is None: return
        new_entry.append(element)

        settings.data_append(new_entry)  # now add new entry to global data
        print colour.green + "Entry has been added to database." + colour.end
        settings.rebuild_trees()  # refresh global trees for interactive database
        print colour.green + "Trees have been rebuilt." + colour.end

        for i in xrange(0, 3):  # returning print loop
            pstring = colour.green + "Returning you to the MAIN MENU in " + str(3-i) + colour.end
            sys.stdout.write(pstring)
            sys.stdout.flush()
            time.sleep(1)
            sys.stdout.write('\r')

        return  # exit to main menu



def add_data_string(field):  # standard checks for adding a string type
    while True:
        user_input = raw_input(colour.darkcyan + "\nPlease enter a valid input for: " + colour.bold + field + colour.end + "\n")
        invalid_input = colour.red + colour.bold + user_input + colour.end + \
                           colour.red + " is an invalid input." + colour.end
        user_input = user_input.lower()
        if user_input == '':
            print invalid_input
            continue
        elif user_input == 'back' or user_input == '..':
            return None
        elif user_input == 'q' or user_input == 'quit':
            menus.quit_menu()
            continue

        user_input = user_input.capitalize()  # capitalise the first letter of input
        return user_input


def add_data_date(field):
    while True:
        user_input = raw_input(colour.darkcyan + "\nPlease enter a valid input for: " + colour.bold + field + colour.end + "\n")
        invalid_input = colour.red + colour.bold + user_input + colour.end + \
                           colour.red + " is an invalid input." + colour.end
        user_input = user_input.lower()
        if user_input == '':
            print invalid_input
            continue
        elif user_input == 'back' or user_input == '..':
            return None
        elif user_input == 'q' or user_input == 'quit':
            menus.quit_menu()
            continue

        string = user_input.split()  # split the input and do checks to ensure they are valid
        if len(user_input) == 10 and numbercheck(string[0], 'year') and numbercheck(string[1], 'month') and numbercheck(string[2], 'day'):
            user_input = user_input.capitalize()
            return user_input
        else:
            print invalid_input
            continue


def add_data_time(field):
    while True:
        user_input = raw_input(colour.darkcyan + "\nPlease enter a valid input for: " + colour.bold + field + colour.end + "\n")
        invalid_input = colour.red + colour.bold + user_input + colour.end + \
                           colour.red + " is an invalid input." + colour.end
        user_input = user_input.lower()
        if user_input == '':
            print invalid_input
            continue
        elif user_input == 'back' or user_input == '..':
            return None
        elif user_input == 'q' or user_input == 'quit':
            menus.quit_menu()
            continue

        string = user_input.split(':')  # split by colon and get the time components
        if numbercheck(string[0], 'hh') and numbercheck(string[1], 'mm') and numbercheck(string[2], 'ss') and len(string) == 3:
            user_input = user_input.capitalize()
            return user_input
        else:
            print invalid_input
            continue


def add_data_duration(field):
    while True:
        user_input = raw_input(colour.darkcyan + "\nPlease enter a valid input for: " + colour.bold + field + colour.end + "\n")
        invalid_input = colour.red + colour.bold + user_input + colour.end + \
                           colour.red + " is an invalid input." + colour.end
        user_input = user_input.lower()
        if user_input == '':
            print invalid_input
            continue
        elif user_input == 'back' or user_input == '..':
            return None
        elif user_input == 'q' or user_input == 'quit':
            menus.quit_menu()
            continue

        input_words = user_input.split()  # split into input words for data validation
        # validate that the user has input a duration that is formated in the standard phrasing
        if numbercheck(input_words[0], 'days') and input_words[1] == 'days,' \
                and numbercheck(input_words[2], 'h') and input_words[3] == 'h,' \
                and numbercheck(input_words[4], 'min') and input_words[5] == 'min' and len(user_input):
            user_input = user_input.capitalize()
            return user_input
        else:
            print invalid_input
            continue


def numbercheck(string, code):  # check the input based on its type and what is expected
    if string.isdigit():
        try:
            if code == 'year':
                if '1900' <= string <= '2100' and len(string) == 4: return True
                else: return False
            elif code == 'month':
                if '01' <= string <= '12' and len(string) == 2: return True
                else: return False
            elif code == 'day':
                if '01' <= string <= '31' and len(string) == 2: return True
                else: return False
            elif code == 'days':
                if '000' <= string <= '999' and len(string) == 3: return True
                else: return False
            elif code == 'h':
                if '00' <= string <= '23' and len(string) == 2: return True
                else: return False
            elif code == 'min':
                if '00' <= string <= '59' and len(string) == 2: return True
                else: return False
            elif code == 'hh':
                if '00' <= string <= '23' and len(string) == 2: return True
                else: return False
            elif code == 'mm':
                if '00' <= string <= '59' and len(string) == 2: return True
                else: return False
            elif code == 'ss':
                if '00' <= string <= '59' and len(string) == 2: return True
                else: return False
        except:
            return False
    else:
        return False
