import csv

#open csv file in read mode
with open('MOCK_DATA.csv', 'r') as csv_obj: 
    # DictReader returns iterator
    dict_reader = csv.DictReader(csv_obj)  

    # iterator gets passed to list() & returns a list of dictionaries
    list_of_dict = list(dict_reader)
    
print(*list_of_dict, sep="\n")
print("# of list items: ", len(list_of_dict))
