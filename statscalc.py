import csv
from collections import OrderedDict
from typing import OrderedDict
from random import randint


def filereader(file_path):
    # open csv file in read mode
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


def quickSort(list, length):
    listlen = length
    print("length of list: ", listlen, '\n')
    if(listlen < 2):
        print("returning list", *list, sep="\n")
        return list
    low = []
    same = []
    high = []

    # generate random value in range of list length
    randrow = randint(0, listlen - 1)
    print("randrow: ", randrow)
    # unpack row/dictionary
    randdict = list[randrow]
    randc = randdict[1]
    # convert col c data to float
    pivot = float(randc[1])
    print('randrow', randrow, ': ', randdict, '\n')
    # print('randc', pivot, '\n')

    for dict in list:
        for key in dict:
            if(key[0] == 'colC'):
                # print(key, '\n')    #col name
                # print(key[1], '\n')     #col data
                val = float(key[1])
                print("comparing val: ", val, " with pivot: ", pivot, '\n')

                if(val < pivot):
                    # print("dict added to low: ", dict)
                    low.append(dict)
                elif (val == pivot):
                    # print("dict added to same: ", dict)
                    same.append(dict)
                elif (val > pivot):
                    # print("dict added to high: ", dict)
                    high.append(dict)
    llength = len(low)
    slength = len(same)
    hlength = len(high)
    return (quickSort(low, llength) + same + quickSort(high, hlength))


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
