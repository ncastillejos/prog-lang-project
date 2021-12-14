import csv
from collections import OrderedDict 
from typing import OrderedDict
from random import randint



def filereader(file_path):
    #open csv file in read mode
    with open(file_path, 'r') as csv_obj: 
        # DictReader returns iterator
        dict_reader = csv.DictReader(csv_obj)  

        # iterator gets passed to list() & returns a list of dictionaries
        list_of_dict = list(dict_reader)
    return list_of_dict

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

def rem_empty(list):
    curr = 0
    for dict in list:
        lod = int(len(dict.keys()))
        if lod > curr:
           curr = lod
    lim = range(len(list))

    for index, item in enumerate(list):
        #print(index, '\t', item, '\n')
        lod = len(item.keys())
        #print(lod)
        
        if curr > lod:
            # print("pop: ", item, "\n")
            list.pop(index)
        
    return list

def rem_dups(list):
    seen = set()
    newlist = []
    for dict in list:
        d = tuple(dict.items())
        # print(d, '\n')
        if d not in seen:
            seen.add(d)
            newlist.append(d)

    return newlist


def quickSort(list, length, scol, sindex):
    listlen = length
    if(listlen < 2):
        return list
    low = [] 
    same = [] 
    high = []
    
    #generate random value in range of list length
    randrow = randint(0, listlen - 1)

    #unpack row/dictionary
    randdict = list[randrow]
    randc = randdict[sindex]

    #convert col c data to float, (col, data)
    pivot = float(randc[1])

    #print('randrow', randrow, ': ', randdict, '\n')
    print(sindex, ': randc:', randc, '\n')
    
    for dict in list:
        for set in dict:
            #check key value (key, data)
            if(set[0] == scol):
                val = float(set[1])

                if(val < pivot):
                    low.append(dict)
                elif (val == pivot):
                    same.append(dict)
                elif (val > pivot):
                    high.append(dict)
    
    #update length of of low and high
    llength = len(low)
    hlength = len(high)

    return (quickSort(low, llength, scol, sindex) + same + quickSort(high, hlength, scol, sindex))

def findKey(list, k):
    kval = -1
    
    for dic in list:
        for j, key in enumerate(dic):
            if key[0] == k:
                return j
    return kval


def main():
    d_list = filereader('MOCK_DATA.csv')
    # d_list = filereader('Boston_Lyft_Uber_Data.csv')

    #print(*d_list, sep="\n")
    #print("# of list items: ", len(d_list))

    #update list with numerical vals in each col only
    upd_list = non_num(d_list)
    #remove rows w empty 
    upd_list2 = rem_empty(upd_list)

    # print("\nnew list after cleanup: \n")
    upd_list3 = rem_dups(upd_list2)

    len3 = len(upd_list3)
    search = 'colC'
    keyIndex = findKey(upd_list3, search)

    if(keyIndex > -1):
        print("key index found at ", keyIndex, '\n')
    else:
        (search, " not found within key values\n")
    templist = quickSort(upd_list3, len3, search, keyIndex)
    #show updated, sorted list
    print(*templist, sep="\n")


    #menu of options...

main()