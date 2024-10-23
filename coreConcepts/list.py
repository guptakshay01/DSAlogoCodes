#   THIS FILE IS CREATED BY AKSHAY GUPTA
#   HERE I DEMONSTRATE LISTS


sampleList = [2, 4, 6, 1, 7, 33, 14, 80, 32, 114]

####    Python program to interchange first and last elements in a list     ####
sampleList[0], sampleList[-1] = sampleList[-1], sampleList[0]                       # O(1)
print(sampleList)


####    Python Program to Swap elements in String list     ####
orgList = ['Gfg', 'is', 'best', 'for', 'Geeks']
updatedList = [str.replace('G', 'z').replace('s', 'd') for str in orgList]          # O(n)
print(updatedList)


####    Python Program to Check if element exists in list     ####
print(80 in sampleList)                                                             # O(n)
print(69 in sampleList)
print(sampleList.count(33))                                                         # O(n)


####    Python Program to Reversing a List     ####
print(sampleList[-1:])