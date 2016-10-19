def tupules():
    #import string
    handle = open('abc.txt')
    file = handle.read()
    wordcount = file.split()    
    counts = dict()
    for word in wordcount:
        if word not in counts:
            counts[word] = 1
        else:
            counts[word] += 1
    
        list1 = list()
        for key,val in counts.items():
            list1.append((val,key))
            
        list1.sort(reverse=True)
        
        for key,val in list1[:10]:
            print(key,val)
