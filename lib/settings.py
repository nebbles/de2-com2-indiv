import platform
import database


def init():
    # Create global variables for use throughout program
    global platform_current
    global data
    global default_filename
    global import_preview

    platform_current = platform.system()  # get platform information
    default_filename = 'default_data.csv'  # set a default file name
    import_preview = True  # set whether import preview shows or not

    import readwrite  # import can only happen after default filename
    # has been assigned since readwrite module refers to this module

    data = readwrite.import_data()  # import the default data into the program (saved state from last time)

    rebuild_trees()  # initialise program with all trees constructed once


def rebuild_trees():  # function can be called when trees need to be rebuilt
    global trees  # sets a global variable that can be referenced anywhere from program
    trees = []
    trees = database.bst_construct_all()  # overwrites trees list with latest data


def data_append(item):  # append an item to the global data variable
    global data
    data.append(item)
