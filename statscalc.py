import csv

with open('MOCK_DATA.csv', 'r') as csv_obj:
    dict_reader = csv.DictReader(csv_obj)
    list_of_dict = list(dict_reader)
#    for row in csv_data:
#        if line_count == 0:
#            print(f'Column names are {", ".join(row)}')
#            line_count += 1
#        else:
#            print(f'\t{row[0]} , {row[1]} ')
#            line_count += 1
print(*list_of_dict, sep="\n")
print("# of list items: ", len(list_of_dict))
