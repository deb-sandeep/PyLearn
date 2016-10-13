import string
fhand = open('abc.txt') 
counts = dict()
for line in fhand:
    line = line.translate(None, string.punctuation) #### Why is the string function used?
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
    
lst.sort(reverse=True) ##### What does reverse=True mean and why is it used?
for key, val in lst[:10] : #### What does this do?
    print (key, val)

# We had written a code to find the most frequent and least frequent word. 
# Can we convert that code to find the same to display frequency of all words?

#--------------------------------------------------------------------------------#

# Could you suggest some practice codes in list?
# I'm weak at dictionaries, what are some good basic codes to understand the concept thoroughly?
# I have started reading about tupules. How can we go about that?

#--------------------------------------------------------------------------------#




      
