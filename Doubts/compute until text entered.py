# Write a program which repeatedly reads numbers until the user en- ters "done". Once "done" is entered, 
# print out the total, count, and average of the numbers. If the user enters anything other than a number, 
# detect their mistake using try and except and print an error message and skip to the next number.
# 
# 
# Enter a number: 4
# Enter a number: 5
# Enter a number: bad data Invalid input
# Enter a number: 7
# Enter a number: done
# 16 3 5.33333333333
# 
# 
# # Is this similar to arrays in java? 
# # Can lists have elements with different datatypes?
# # I'm struggling with customized user input in lists

input_list = []
continue_input = True

while continue_input:
    str = raw_input( "Enter a number:" )
    print str
    if str.lower() == "done":
        continue_input = False
    else:
        try:
            input_list.append( int(str) )
        except:
            print( "Please enter a valid integer." )

print input_list

# I got this! Thank you!
