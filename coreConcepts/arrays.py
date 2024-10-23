#   THIS FILE IS CREATED BY AKSHAY GUPTA
#   HERE I DEMONSTRATE ARRAYS

from array import *

# 1. Create an array and traverse.
arr = array('i', [1,2,3,4,5])
print(arr)

for i in arr:
    print(i)
# 2. Access individual elements through indexes
print(arr[3])

# 3. Append any value to the array using append() method
arr.append(10)
print(arr)

# 4. Insert value in an array using insert() method
arr.insert(2, 11)
print(arr)

# 5. Extend python array using extend() method
arr.extend(array('i',[10,12]))
print(arr)

# 6. Add items from list into array using fromlist() method
arr.fromlist([21,22])
print(arr)

# 7. Remove any array element using remove() method
arr.remove(11)

# 8. Remove last array element using pop() method
arr.pop()
print(arr)

# 9. Fetch any element through its index using index() method
print(arr.index(4))

# 10. Reverse a python array using reverse() method
arr.reverse()
print(arr)

# 11. Get array buffer information through buffer_info() method
print(arr.buffer_info())

# 12. Check for number of occurrences of an element using count() method
print(arr.count(21))

# 13. Convert array to string using tostring() method
temp_arr_str = ''.join(str(i) for i in arr)
print(temp_arr_str)

# 14. Convert array to a python list with same elements using tolist() method
temp_arr_ls = arr.tolist()
print(temp_arr_ls)

# 16. Slice Elements from an array
print(arr[3:7])