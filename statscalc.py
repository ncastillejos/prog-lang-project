# course: cmps3500
# CLASS Project
# PYTHON IMPLEMENTATION OF A CUSTOM STATISTICS SUMMARY CALCULATOR
# date: 12/13/21
# Student 1: Michaelted Acosta
# Student 2: Nancy Castillejos
# Student 3: Jesus Rojas
# description: Implementation of a statistics summary Calculator


import csv
from collections import OrderedDict
from typing import OrderedDict
from random import randint


def printMenu():
    print("Commands")
    print("----------------------------")
    print("1 - Print Contents of Original File\n")
    print("2 - Clean the File\n")
    print("3 - Search an element in a Column\n")
    print("4 - Statistical Operations\n")
    print("0 - Exit\n")


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
        # print(index, '\t', item, '\n')
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

    # generate random value in range of list length
    randrow = randint(0, listlen - 1)

    # unpack row/dictionary
    randdict = list[randrow]
    randc = randdict[sindex]

    # convert col c data to float, (col, data)
    pivot = float(randc[1])

    #print('randrow', randrow, ': ', randdict, '\n')
    #print(sindex, ': randc:', randc, '\n')

    for dict in list:
        for set in dict:
            # check key value (key, data)
            if(set[0] == scol):
                val = float(set[1])

                if(val < pivot):
                    low.append(dict)
                elif (val == pivot):
                    same.append(dict)
                elif (val > pivot):
                    high.append(dict)

    # update length of of low and high
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
            # check key value (key, data)
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
        print(searchval, " found in", searchcol, " at position ",
              foundindex[i], ": ", list[ind], "\n")

    # foundindex = []
    # foundindex = BinarySearch(cols, searchval)

    # show updated, sorted list
    #print(*templist, sep="\n")


def BinarySearch(lys, val):
    indeces = []
    first = 0
    last = len(lys)-1
    index = -1

    while (first <= last) and (index == -1):
        mid = (first+last)//2
        if lys[mid] == val:
            index = mid
        else:
            if val < lys[mid]:
                last = mid - 1
            else:
                first = mid + 1
    indeces.append(index)
    return index


def mean(mean_list):
    mean = 0.0  # hold mean variable
    count = 0  # hold number of values present

    print("Enter the column that you would like to calculate the MEAN for: ")
    columnChoice = input()  # hold the specific column of mean value

    print("Calculating Mean...")
    for dict in mean_list:
        for key in dict:
            if(key[0] == columnChoice):
                mean = mean + int(key[1])  # add each value to mean
                count = count + 1  # keep number count

    mean = mean / count  # calculate actual mean value

    return mean


def countNum(mean_list):
    count = 0  # hold count for values

    print("Enter the column that you would like to find the Count for: ")
    columnChoice = input()  # hold the specific column for min value

    print("Calculating the count for the chosen column...")
    for dict in mean_list:
        for key in dict:
            if(key[0] == columnChoice):
                count = count + 1  # calculate actual mean value

    return count


def main():
    clean_list = []

    try:
        fileInput = input("What CSV file would you like to open? \t")
        file = open(fileInput, newline='')
        file.close()
        d_list = filereader(fileInput)
        print("{} has been read\n".format(fileInput))

    except FileNotFoundError:
        print("\nCould not find the file. Exiting Program.")
        return

        # d_list = filereader('MOCK_DATA.csv')
        # d_list = filereader('Boston_Lyft_Uber_Data.csv')

        # print(*d_list, sep="\n")
        # print("# of list items: ", len(d_list))

    while True:
        printMenu()

        command = input("Enter a Command Number: ").lower()
        if command == '1':
            print("Contents of File\n")
            print("----------------")
            print(*d_list, sep="\n")
            print("\n\n")

        elif command == '2':
            print("Cleaning {}\n\n".format(fileInput))
            upd_list = non_num(d_list)
            upd_list2 = rem_empty(upd_list)
            clean_list = rem_dups(upd_list2)
            print("\n\n")

        elif command == '3':
            # search function call
            #print("Please enter a value to search for: \n")
            sval = input("Please enter a value to search for:")
            #print("Search dataset or specific column?\n")
            scope = input(
                "Search dataset (d) or specific column (c)? ").lower()
            if scope == 'c':
                print('scope: c')
                col = input("Enter column to search in: ")
                searchData(clean_list, col, sval)
            elif scope == 'd':
                print('')
                searchData(clean_list, col, 'dataset')
            else:
                print("invalid input\n")

        elif command == '4':
            if bool(clean_list) == False:
                print("Please clean the file first\n\n")
            else:
                while True:
                    print("\n\nWhat would you like to do?\n")
                    print("1 - Find the Mean\n")
                    print("2 - Find the Count\n")
                    print("0 - Go Back")

                    sCommand = input("Enter a Number: ").lower()
                    if sCommand == '1':
                        sMean = mean(clean_list)
                        print("The mean is ")
                        print(sMean)

                    elif sCommand == '2':
                        sCount = countNum(clean_list)
                        print("The count is ")
                        print(sCount)

                    elif sCommand == '0':
                        print("\n\n")
                        break

                    else:
                        print("Command does not exist")

        elif command == '0':
            print("Exiting Program")
            break

        else:
            print("Command does not exist")


main()
