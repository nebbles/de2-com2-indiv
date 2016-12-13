# Import standard python modules
import sys
import webbrowser

# Import custom modules from private library
from lib import settings
from lib import print_to_console
from lib.print_to_console import colour
from lib import menus

# Do a module check to ensure that the correct modules are installed
try:
    import terminaltables  # try to import specifically required module
except ImportError:
    print colour.red + "There was a problem importing the "\
          + colour.bold + "'terminaltables'"\
          + colour.end + colour.red+" module."

    print "\nPlease ensure you have 'terminaltables' installed. " \
          "For more information visit " + colour.blue + \
          "https://robpol86.github.io/terminaltables/install.html" + colour.end

    raw_input("\nPress "+colour.green+"ENTER"+colour.end+" to be taken to website or "
              + colour.red+"CTRL+C"+colour.end+" to exit")

    webbrowser.open_new_tab('https://robpol86.github.io/terminaltables/install.html')  # take user to web page
    sys.exit()  # program cannot run without module so exit now

# Run the program
try:
    settings.init()  # set up program defaults and global variables
    try:
        if sys.argv[1] == 'debug':  # if commandline argument 'debug' was passed in
            print_to_console.debug_screen()  # then display the debug screen before continuing
    except IndexError:
        pass

    menus.main_menu()  # display the main menu

# except KeyboardInterrupt:
#     print "\n"
finally:
    print colour.green + "\nExiting program..." + colour.end
    # print_to_console.clear_screen()
