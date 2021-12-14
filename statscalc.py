import csv
from collections import OrderedDict
from typing import OrderedDict
from random import randint


def filereader(file_path):
    # open csv file in read mode
    try:
        with open(file_path, 'r') as csv_obj:
            # DictReader returns iterator
            dict_reader = csv.DictReader(csv_obj)

            # iterator gets passed to list() & returns a list of dictionaries
            list_of_dict = list(dict_reader)
        return list_of_dict

    except FileNotFoundError:
        msg = "Sorry, the file "+ file_path + "does not exist."
        print(msg)


def non_num(list):
    # create a new list
    # create a dictionary variable - this will be updated then appended to list

    new_list = []
    new_dict = {}
    # iterate over current list
    for dict in list:
        for key in dict:
            # only append columns w numerical values
            if(dict[key].isnumeric()):
                new_dict.update({key: dict[key]})
        # append dictionary as row in list
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
        # print(lod)

        if curr > lod:
            # print("pop: ", item, "\n")
            list.pop(index)

    return list


def rem_dups(list):
    seen = set()
    newlist = []
    for dict in list:
        d = tuple(dict.items())
        print(d, '\n')
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
    #print(sindex, ': randc:', randc, '\n')
    
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

def statsOps(list):
    print("stats operation function")
    
def searchData(list, searchcol, searchval):
    length = len(list)
    print("entered search func\nsearchcol: ", searchcol)
    keyIndex = findKey(list, searchcol)
    if keyIndex <= -1:
        return (searchcol, " column not found")

  
    templist = quickSort(list, length, searchcol, keyIndex)
    cols = []
    for dict in list:
        for set in dict:
        #check key value (key, data)
            if(set[0] == searchcol):
                cols.append(set)
    
    # print(cols, sep="\n")
    foundindex = []
    for i in range(len(cols)):
        if cols[i][1] == searchval:
            foundindex.append(i)
    print(foundindex, "\n")
    
    for i in foundindex:
        ind = int(foundindex[i])
        print(searchval, " found in", searchcol, " at position ", foundindex[i], ": ", list[ind] ,"\n")

    
    # foundindex = []
    # foundindex = BinarySearch(cols, searchval)



    #show updated, sorted list
    #print(*templist, sep="\n")


def main():
    while True:
        print("Commands\n")
        print("----------------------------")
        print("1 - Load a File\n")
        print("2 - Print Contents of File\n")
        print("3 - Clean a File\n")
        print("4 - Search an element in a Column\n")
        print("0 - Exit\n")

        command = input("Enter a Command Number: ").lower()
        if command == '1':
            fileInput = input("Name of file: ")
            file = open(fileInput, newline='')
            file.close()
            d_list = filereader(fileInput)
            print("{} has been read\n\n".format(fileInput))
            new_list = []
            upd_list = non_num(d_list)
            upd_list2 = rem_empty(upd_list)
            clean_list = rem_dups(upd_list2)

            while(True):
                print("Commands\n")
                print("----------------------------")
                print("1 - Print Contents of File\n")
                print("2 - Search an element in a Column\n")
                print("3 - Statistical Operations\n")
                print("0 - Exit\n")

                fcommand = input("Enter a Command Number: ").lower()
                if fcommand == '1':
                    print("Contents of File\n")
                    print("----------------")
                    print(*d_list, sep="\n")
                elif fcommand == '2':
                    #search function call
                    #print("Please enter a value to search for: \n")
                    sval = input("Please enter a value to search for:" )
                    #print("Search dataset or specific column?\n")
                    scope = input("Search dataset (d) or specific column (c)? ").lower()
                    if scope == 'c':
                        print('scope: c')
                        col = input("Enter column to search in: ")
                        searchData(clean_list, col, sval)
                    elif scope == 'd':
                        print('')
                        searchData(clean_list, col, 'dataset')
                    else:
                        print("invalid input\n")


                elif fcommand == '3':
                    #stats operation call
                    statsOps(clean_list)
                    print("stats operations\n")
                elif fcommand == '0':
                    print("Exiting Program")
                    break
            # d_list = filereader('MOCK_DATA.csv')
            # d_list = filereader('Boston_Lyft_Uber_Data.csv')

            #print(*d_list, sep="\n")
            # print("# of list items: ", len(d_list))

        elif command == '2':
            print("Contents of File\n")
            print("----------------")
            print(*d_list, sep="\n")

        elif command == '3':
            # update list with numerical vals in each col only
            upd_list = non_num(d_list)
            # print("# of list1 items: ", len(upd_list))
            #print(*upd_list, sep="\n")

            # remove rows w empty
            upd_list2 = rem_empty(upd_list)
            # print("new list after cleanup: \n")
            # print(*upd_list2, sep="\n")
            # print("# of list2 items: ", len(upd_list2))

            print("\nnew list after cleanup: \n")
            upd_list3 = rem_dups(upd_list2)
            # print("# of list3 items: ", len(upd_list3))
            # print(*upd_list3, sep="\n")

        elif command == '4':
            templist = quickSort(upd_list3, len(upd_list3))

        elif command == '0':
            print("Exiting Program")
            break

        else:
            print("Command does not exist")


main()
