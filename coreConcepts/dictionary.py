#   This file is created by Akshay Gupta
#   Python Dictionary

# Create dictionary
myDict1 = dict()
print(myDict1)
myDict2 = {}
print(myDict2)

inWords_func= dict(one=1, two=2, three=3, four=4)   # TimeComplexity - O(n), Space Complexity - O(n)
print(inWords_func)

inWords = {"one":1, "two":2, "three":3, "four":4}   # TimeComplexity - O(n), Space Complexity - O(n) 
print(inWords)

inWords_list = [("one", 1), ("two", 2), ("three", 3), ("four", 4)]
inWords_listToDict = dict(inWords_list)
print(inWords_listToDict)

newDict = {}.fromkeys([1,2,3,4,5], 0)
print(newDict)


# Insert/Update in dictionary
personDict = {'name':'Eric', 'age':26}
print(personDict)

personDict['age'] = 27                      # TimeComplexity - O(1), Space Complexity - O(n)
print(personDict)

personDict['email'] = 'eric@freemail.com'   # O(1)
print(personDict)


# Traversal in dictionary
personDict = {'name':'Eric', 'age':26, 'address':'New York'}
print(personDict)

def traversDictionary(dict):                            # O(n)
    for key in dict:
        print(key, dict[key])

traversDictionary(personDict)

def searchElementDictionary(dict, value):                # O(n)
    for key in dict:
        if dict[key] == value:
            return key, value
    return "Value not found!"

print(searchElementDictionary(personDict, 'Eric'))


# Delete from dictionary
personDict = {'name':'Eric', 'age':26, 'address':'New York', 'email':'eric@freemail.com'}
print(personDict)

del personDict['address']                               # O(1)
print(personDict)

removedElement = personDict.pop('age', None)            # pop(key, default value incase of key not found)   O(1)
print(removedElement)
print(personDict)

removedLastElement = personDict.popitem()               # O(1)
print(personDict)

personDict.clear()                                      # O(n)
print(personDict)


# Built-in dictionary methods
personDict = {'name':'Eric', 'age':26, 'address':'New York', 'email':'eric@freemail.com', 'phone':'8978563412'}
print(personDict)

newDict = personDict.copy()
print(newDict)

newDict = {}.fromkeys([1,2,3,4,5], 0)
print(newDict)

newDict = {}.fromkeys([1,2,3,4,5])
print(newDict)

print(personDict.get('age', None))                      # get(key, default value incase of key not found)

print(personDict.items())

print(personDict.keys())

print(personDict.setdefault('sex', None))
print(personDict)

print(personDict.values())

person2 = {'name2':'Eric II', 'age2':5}
personDict.update(person2)
print(personDict)


# Operations in dictionary
numberDict = {3:'three', 4:'four', 0:'zero', 1:'one', 2:'two', 5:'five', 6:'six'}
print(numberDict)

print('four' in numberDict)
print(4 in numberDict)                                  # checks for keys not values

print('four' not in numberDict.values())  
print(len(numberDict))

print(all(numberDict))                                  # checks for all the keys to be True, all key must be true

print(any(numberDict))                                  # checks for any key to be True, any one key can be true'

print(sorted(numberDict))                               # return keys in sorted order


# Dictionary comprehension
# Syntex - newDict = {newKey:newValue for item in list}

import random

cityNames = ['Indore', 'Bhopal', 'Ratlam', 'Jhansi', 'Ujjain']

cityTemperature = {city:random.randint(20, 50) for city in cityNames}
print(cityTemperature)

cityTempAbove35 = { key:val for key,val in cityTemperature.items() if val>35}
print(cityTempAbove35)
