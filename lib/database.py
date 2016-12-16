import settings  # import all globally used variables
import bst  # import the bst to be used in the database


def bst_construct(data, key_column_index):  # construct a bst using LoL data and a index key
    tree = bst.BinarySearchTree()  # create the tree
    for element in data:  # add each element of data to tree
        tree[element[key_column_index]] = element
    return tree


def bst_construct_all():
    trees = []  # create an empty list for all trees
    for col_index in range(0, len(settings.data[0])):  # for each column in database
        trees.append(bst_construct(settings.data[1:], col_index))  # create a tree using the column as the key
    return trees


def sort_data(column, order=None):
    index = column-1  # column is int and offset to readable format so must be converted to index
    sorted_data = settings.trees[index].inorder()  # call the inorder() to return a min to max list
    if order == 'reversed': sorted_data.reverse()  # if list needs to be max to min then reverse the sorted list
    sorted_data.insert(0, settings.data[0])  # insert the headers into the top line of the data
    return sorted_data


def get_interval(col_num, min_key, max_key):
    index = col_num-1  # column is int and offset to readable format so must be converted to index
    sorted_list = settings.trees[index].inorder()  # find interval in relevant tree
    interval = []
    for row in sorted_list:
        # print min_key, row[index], max_key  # DEBUG LINE
        if min_key <= row[index] <= max_key:
            # print 'true'  # DEBUG LINE
            interval.append(row)  # append the row if it sits within the bounds

    if len(interval) == 0: return None  # if interval doesnt exits return None

    interval.insert(0, settings.data[0])  # insert the headers after collecting interval
    return interval


def convert_to_min(duration):  # takes a standard duration phrase and convert it into minutes
    word = duration.split()
    try:
        total_min = int(word[0]) * 1440 + int(word[2]) * 60 + int(word[4])
        if total_min >= 0:
            return int(total_min)
    except ValueError:
        pass


def convert_to_duration(mins):  # takes a mins number and converts to standard duration phrase
    days = mins / 1440
    remainder = mins % 1440
    hours = remainder / 60
    mins = int(remainder % 60)
    duration = str(days) + " days, " + str(hours) + " h, " + str(mins) + " min"
    return duration


def average_duration():  # calculates the average duration
    totals = []
    for line in settings.data:  # gets each duration phrase from database
        total_min = convert_to_min(line[5])
        if total_min is not None:  # as long as the duration phrase existed then type will not be None
            totals.append(int(total_min))
    average = sum(totals) / len(totals)  # Get average
    duration = convert_to_duration(average)  # convert back to duration phrase
    return average, duration


def stat_data(column, mode):
    index = column-1  # column is int and must be converted back to index
    payload = None
    if mode == 'min': payload = settings.trees[index].findMin()  # Use tree method to find min
    elif mode == 'max': payload = settings.trees[index].findMax()  # Use tree method to find max
    return payload  # return min or max based on mode
