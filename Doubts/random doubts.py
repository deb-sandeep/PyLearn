import string
fhand = open('romeo-full.txt') counts = dict()
for line in fhand:
line = line.translate(None, string.punctuation)
