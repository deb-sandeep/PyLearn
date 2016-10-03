# This file contains many examples of list comprehensions.
#
# List comprehensions are an easy way to transform one list into another. The
# source list can be a multi dimensional list as can be the destination list.

def squares():
    "Computes a list of squares of each item in the input list."
    input = [0,1,2,3,4,5]
    squares = [n**2 for n in input]
    print "Squares of ", input, " is \n\t", squares

def squares_of_even( n ):
    "Computes the list of squares for all even numbers within a range 0-n"
    squares = [n**2 for n in range(n) if n % 2 == 0 ]
    print "Squares of even numbers \n\t", squares

def tupule_of_squares_of_even( n ):
    "Computes a list of tupules of even numbers and their associated squares"
    squares = [[n,n**2] for n in range(n) if n % 2 == 0 ]
    print "Tupule of squares of even numbers \n\t", squares

def flat_matrix_rowwise():
    "Flattens a matrix, rowwise"
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    array = [ col for row in matrix for col in row ]
    print "Rowwise flattened matrix \n\t", array

def amalgamate():
    "Amalgamates the two lists"
    first_list = [ 0, 2 ]
    second_list = [ 1, 3 ]
    mixed_list = [ [f, s] for f in first_list for s in second_list ]
    print "Amalgamated list \n\t", mixed_list

def transpose():
    "Creates a transpose of the input matrix"
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    transpose = [ [row[col] for row in matrix] for col in range(len(matrix)) ]
    print "Transpose of matrix \n\t", transpose

# ------------------------------------------------------------------------------
# Exercise questions
def flat_matrix_colwise():
    "Flattens a matrix, colwise"
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    array = [] # <- Populate with appropriate comprehension expression
    # The output should look like
    # [1, 4, 7, 2, 5, 6, 3, 6, 9]
    print "Colwise flattened matrix \n\t", array

def squares_of_multiples_of_3():
    "Computes an array of squares of numbers which are multiple of three. from \
    the input set represented by the array input."
    input = [x for x in range(30)]
    array = [] # <- Populate with appropriate comprehension expression
    # The output should look like
    # [0, 9, 36, 81, 144, 225, 324, 441, 576, 729]
    print "Array of squares of multiples of 3 \n\t", array

squares()
squares_of_even(10)
tupule_of_squares_of_even(10)
flat_matrix_rowwise()
amalgamate()
transpose()

# ------------------------
flat_matrix_colwise()
squares_of_multiples_of_3()