#   This file is created by Akshay Gupta
#   Python Tuples


# Creating Tuples
sampleTup = 1,2,3,4,5
print(sampleTup)

oneTup = (1, )
print(oneTup)

constrtTuple = tuple()
print(constrtTuple)


# Accessing tuples
sampleTup = 1,2,3,4,5
print(sampleTup[2])
print(sampleTup[-2])
print(sampleTup[:-2])


# Traverse tuple
sampleTup = 1,2,3,4,5

for i in sampleTup:                             # O(n)
    print(i)

for i in range(len(sampleTup)):                 # O(n)
    print(i, sampleTup[i])


# Search in tuple
sampleTup = 1,2,3,4,5

print(1 in sampleTup)                           # O(n)
print(sampleTup.index(4))                       # O(n)


# Operations/functions in tuple
sampleTup = 1,2,3,4,5
otherTup = 9,2,5,4,7

# Concatenation
print(sampleTup + otherTup)

# Repeat all elements
print(sampleTup * 2)

# Count an element
print((sampleTup + otherTup).count(2))

# List to tuple
print(tuple(['a', 'b', 'c', 'd']))