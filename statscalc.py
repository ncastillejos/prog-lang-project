import csv


def filereader(file_path):
    #open csv file in read mode
    with open(file_path, 'r') as csv_obj: 
        # DictReader returns iterator
        dict_reader = csv.DictReader(csv_obj)  

        # iterator gets passed to list() & returns a list of dictionaries
        list_of_dict = list(dict_reader)
    return list_of_dict

d_list = filereader('MOCK_DATA.csv')

print(*d_list, sep="\n")
print("# of list items: ", len(d_list))
