name = input('Enter file:')
handle = open(name, 'r')
text = handle.read()
words = text.split()
counts = dict()

# [Sandy] - Loop through all the words in the file and count the number of 
# occurences of each word. A dictionary is created whose key is the word and
# value is the number of occurences of the word. Every time we process a word
# we look up the number of occurences of the word in the map, increment one
# and set it back in the dictionary.
for word in words:
    counts[word] = counts.get(word,0) + 1 ## what is happening here?

bigcount = None
bigword = None
for word,count in counts.items():
    # We go through all the entries in the dictionary and for each key,value
    # pair, determine if we have encountered a word whose repetetion count 
    # is the highest. If so, we recognize it as the most frequently used word
    # till now and carry on eavaluating the other key, value paris in the 
    # dictionary.
    if bigcount is None or count > bigcount:
        bigword = word     ## is this getting the longest word or the most repeated word?
        bigcount = count

# Prints the word which is most frequently used and the number of times it 
# appears in the file.        
print (bigword, bigcount)
