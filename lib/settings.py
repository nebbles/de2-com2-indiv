import platform

def init():
    global platform_current
    global data
    global default_filename
    platform_current = platform.system()
    default_filename = 'default_data.csv'

    import readwrite  # import can only happen after default filename
    # has been assigned since readwrite module refers to this module
    data = readwrite.import_data()  # import the default data into the program (saved state from last time)
