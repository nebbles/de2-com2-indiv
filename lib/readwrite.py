import csv
import settings


def import_data(filename=settings.default_filename):
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


def export_data(data):
    with open('test.csv', 'a') as csvout:
        wr = csv.writer(csvout, delimiter=',', quotechar='"')
        for row in data:
            wr.writerow(row)

    csvout.close()






