import sys

def sample_loops( nos ):
    largest = None
    smallest = None
    sum = 0
    count = 0
    for i in nos:
        count = count + 1
        sum = sum + i
        if largest is None or i > largest:  # if largest is None ? what is the need to write that
            # largest is None accounts for the first number being processed.
            # The first number we process is the largest number till that point
            # You could also have done it by initializing largest with 
            # -sys.maxint and smallest with sys.minint
            largest = i
        if smallest is None or i < smallest:    # same as above
            smallest = i
    print ("Elements: ", count)
    print ("Sum: ", sum)
    print ("Largest: ", largest)
    print ("Smallest: ", smallest)


# how can i take a list as user input?
# Sandy: There are many ways of doing it - here is one. Take the input (a 
# sequence of integers) as a string. Then use a list comprehension (which we
# have learnt already) to split the string and convert each string to its
# corresponding integer value. 
#
# NOTE: I have chosen this method to show you a practical use of comprehension
#       In reality we would need a more elaborate method to check and filter 
#       out non integer values in the input.
user_input = raw_input( "Enter a sequence of numbers: " )
nos = [ int( item ) for item in user_input.split() ]

sample_loops( nos ) # what does this do?

#This code solves a lot of questions i had. 
