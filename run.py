# Import standard python modules
import sys
import webbrowser

try:
    # Do a module check to ensure that the correct modules are installed
    try:
        import terminaltables  # try to import specifically required module
    except ImportError:
        print "\nThere was a problem importing the 'terminaltables' module."
        print "\nPlease ensure you have 'terminaltables' installed. For more information visit:"
        print "\nhttps://robpol86.github.io/terminaltables/install.html"
        print "\nYou can install it by running 'pip install terminaltables' in your terminal window"
        raw_input("\nPress ENTER to be taken to website or CTRL+C to exit")

        webbrowser.open_new_tab('https://robpol86.github.io/terminaltables/install.html')  # take user to web page
        sys.exit()  # program cannot run without module so exit now

    # Import custom modules from private library
    from lib import settings
    settings.init()  # set up program defaults and global variables

    # Check if user is on Mac or Linux, if not then exit.
    if settings.platform_current == 'Darwin' or settings.platform_current == 'Linux':
        pass
    else:
        print "You are not running a UNIX based OS (macOS/Linux). This program is not compatible with other OS."
        raw_input("Press ENTER to exit.")
        sys.exit()

    # Check that the user is using a terminal window - not pycharm.
    if not sys.stdout.isatty():
        print "You are not on a UNIX terminal. This program only runs in UNIX (macOS/Linux) terminal windows."
        raw_input("Press ENTER to exit.")
        sys.exit()

    # Import private modules
    from lib import print_to_console
    from lib.print_to_console import colour
    from lib import menus

    # Run the program

    try:
        if sys.argv[1] == 'debug':  # if commandline argument 'debug' was passed in
            print_to_console.debug_screen()  # then display the debug screen before continuing
    except IndexError: pass

    menus.main_menu()  # display the main menu

except KeyboardInterrupt:  # Exit cleanly if CTRL+C is pressed at any time
    print "\n"
finally:
    # print colour.green + "\nExiting program..." + colour.end
    print_to_console.clear_screen()  # Clear screen as last action
