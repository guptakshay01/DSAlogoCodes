#   This file is created by Akshay Gupta


# Write a function that calculates the sum and product of all elements in a tuple of numbers.
input_tuple = (1, 2, 3, 4)

def sum_product(in_tuple):
    sum_result = 0
    product_result = 1
    
    for item in in_tuple:
        sum_result += item
        product_result *= item

    return sum_result, product_result


sum_result, product_result = sum_product(input_tuple)
print(sum_result, product_result)


# Create a function that takes two tuples and returns a tuple containing the element-wise sum of the input tuples.
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)

def tuple_elementwise_sum(tup1, tup2):
    output_tuple = []

    for item1, item2 in zip(tup1, tup2):
        output_tuple.append(item1+item2)

    return tuple(output_tuple)


def tuple_elementwise_sum2(tup1, tup2):
    return tuple(map(sum, zip(tup1, tup2)))

def tuple_elementwise_sum3(tup1, tup2):
    output_tuple = tuple(item1+ item2 for item1, item2 in zip(tup1, tup2))

    return output_tuple

output_tuple = tuple_elementwise_sum(tuple1, tuple2)
print(output_tuple)  # Expected output: (5, 7, 9)

output_tuple2 = tuple_elementwise_sum2(tuple1, tuple2)
print(output_tuple2)  # Expected output: (5, 7, 9)

output_tuple3 = tuple_elementwise_sum3(tuple1, tuple2)
print(output_tuple2)  # Expected output: (5, 7, 9)


# Write a function that takes a tuple and a value, and returns a new tuple with the value inserted at the beginning of the original tuple.
input_tuple = (2, 3, 4)
value_to_insert = 1

def insert_value_front(tup, val):
    output_tuple = list(tup)
    output_tuple.insert(0, val)

    return tuple(output_tuple)


output_tuple = insert_value_front(input_tuple, value_to_insert)
print(output_tuple)  # Expected output: (1, 2, 3, 4)


def insert_value_front2(tup, val):
    return (val, ) + tup


output_tuple2 = insert_value_front2(input_tuple, value_to_insert)
print(output_tuple2)  # Expected output: (1, 2, 3, 4)


# Write a function that takes a tuple of strings and concatenates them, separating each string with a space.
input_tuple = ('Hello', 'World', 'from', 'Python')

def concatenate_strings(input_tuple):
    return ' '.join(input_tuple)

output_string = concatenate_strings(input_tuple)
print(output_string)  # Expected output: 'Hello World from Python'


# Create a function that takes a tuple of tuples and returns a tuple containing the diagonal elements of the input.
input_tuple = (
        (1, 2, 3),
        (4, 5, 6),
        (7, 8, 9)
    )

def get_diagonal(input_tuple):
    output_tuple = tuple(input_tuple[i][i] for i in range(len(input_tuple)))
    return output_tuple

output_tuple = get_diagonal(input_tuple)
print(output_tuple)  # Expected output: (1, 5, 9)