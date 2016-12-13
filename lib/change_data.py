

def add_data(data):
    category_names = data[0]
    new_entry = []
    print "new data entry - press ctrl c to exit data entry at any time"

    try:
        for name in category_names:
            element = raw_input("Please input "+name+": ")
            new_entry.append(element)
        print new_entry

    except KeyboardInterrupt:
        print "\nEntry will not be added."
        while True:
            yesno = raw_input("Do you want to add a new entry? ")
            yesno.lower()
            if yesno == 'yes' or yesno == 'y':
                add_data(data)
                break
            elif yesno == 'no' or yesno == 'n':
                break
            else:
                print "That is an invalid response. Please reply with 'yes' or 'no' "


