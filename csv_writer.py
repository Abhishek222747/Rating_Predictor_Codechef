import csv

filename = 'data.csv'


def put_data(data):
    with open(filename, 'a') as cook_off_csv:
        write = csv.writer(cook_off_csv)
        write.writerows(data)
