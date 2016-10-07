name = input('Enter file:')
handle = open(name, 'r')
text = handle.read()
words = text.split()
counts = dict()
for word in words:
    counts[word] = counts.get(word,0) + 1 ## what is happening here?
bigcount = None
bigword = None
for word,count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = word     ## is this getting the longest word or the most repeated word?
        bigcount = count
print (bigword, bigcount)
