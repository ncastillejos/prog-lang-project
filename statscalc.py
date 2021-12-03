import csv


def filereader(file_path):
    #open csv file in read mode
    with open(file_path, 'r') as csv_obj: 
        # DictReader returns iterator
        dict_reader = csv.DictReader(csv_obj)  

        # iterator gets passed to list() & returns a list of dictionaries
        list_of_dict = list(dict_reader)
    return list_of_dict

#def cleanup():
def non_num(list):

    # create a new list
    # create a dictionary variable - this will be updated then appended to list 

    new_list = []
    new_dict = {}
    #iterate over current list
    for dict in list:
        for key in dict:
            #only append columns w numerical values
            if(dict[key].isnumeric()):
                new_dict.update({key:dict[key]})
        #append dictionary as row in list                
        new_list.append(new_dict.copy())
        new_dict.clear()
    return new_list

                
            
    #print (list)
d_list = filereader('MOCK_DATA.csv')

#print(*d_list, sep="\n")
#print("# of list items: ", len(d_list))

upd_list = non_num(d_list)
print(*upd_list, sep="\n")