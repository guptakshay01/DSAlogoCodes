#   This file is created by Akshay Gupta
#   Define a function to count the frequency of words in a given list of words.

words = ['apple', 'orange', 'banana', 'apple', 'orange', 'apple']


# My solution --> O(n)
def count_word_frequency(words):
    countDict = {}
    for item in words:
        if item in countDict:
            countDict[item] += 1
        else:
            countDict[item] = 1
    return countDict


print(count_word_frequency(words))


# Referred solution --> O(n)
def count_word_frequency(words):
    countDict = {}
    for item in words:
        countDict[item] = countDict.get(item, 0) + 1
    return(countDict)

print(count_word_frequency(words))