#Printing the items with appropriate distance using string methods

def printPicnic(itemsDict, leftwidth, rightwidth):
    print("PICKNIC ITEMS".center( leftwidth+rightwidth, "-"))
    for k,v in itemsDict.items():
        print(k.ljust(leftwidth , ".") + str(v).rjust(rightwidth))

picnicItems = {'Apples': 12, "Sandwiches": 4, "Cups": 4, "Cookies": 100}

printPicnic(picnicItems,20,6)

'''

#-------------------------------------

#program to print picnic items

def printPicnicItems(itemsDict, leftwidth, rightwidth):
    print("Picnic Items".center(leftwidth+rightwidth))
    for k,v in itemsDict.items():
        print(k.ljust(leftwidth,"-"), str(v).rjust(rightwidth))

picnicItems = {"Cups" : 10, "Apples": 10, "Sandwiches:": 20}
printPicnicItems(picnicItems, 20, 6)
'''
