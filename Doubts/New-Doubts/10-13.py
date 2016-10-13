import string
fhand = open('10-13.py') 
counts = dict()
for line in fhand:
    line = line.translate(None, string.punctuation) 
    # Why is the string function used?
    # [Sandy] 
    # https://www.tutorialspoint.com/python/string_translate.htm
    # https://docs.python.org/3/library/string.html
    # The translate function returns a copy of the string (in this case 'line')
    # in which the characters are translated based on a supplied translation table.
    # In this case, since None is specified, no translation takes place. However
    # The translate function's optional second parameter specifies the string of 
    # characters which should be removed from the input. In this case you have
    # specified string.punctuation - this implies that all punctuation characters
    # will be removed. So essentially we are removing all punctuation characters
    # from the input lines.
    line = line.lower() 
    words = line.split() 
    for word in words:
        if word not in counts: 
            counts[word] = 1
        else:
            counts[word] += 1

# Sort the dictionary by value 
lst = list()
for key, val in counts.items():
    lst.append( (val, key) )
    
lst.sort(reverse=True) 
# What does reverse=True mean and why is it used?
# [Sandy]
# reverse=True implies the values in the list are sorted in descending order
# In this case the values in the list are tuples and hence the sorting will
# happen in the descending order of the value or count of words. Essentially
# you are sorting the list so that the most frequently used words are at the
# start of the list.

for key, val in lst[:10] : 
# What does this do?
# [Sandy] 
# Prints only the first 10 items in the list. i.e. the top 10 most used words
    print (key, val)

# We had written a code to find the most frequent and least frequent word. 
# Can we convert that code to find the same to display frequency of all words?
# [Sandy] 
# Yes absolutely, just that you will have to take care of removing punctuations

#--------------------------------------------------------------------------------#

# Could you suggest some practice codes in list?
# I'm weak at dictionaries, what are some good basic codes to understand the concept thoroughly?
# I have started reading about tupules. How can we go about that?

# [Sandy]
# http://sthurlow.com/python/lesson06/
# https://docs.python.org/2/tutorial/datastructures.html
# Go through the above links - they are the best. I will think of some examples
# and we can talk more next Monday.

#--------------------------------------------------------------------------------#