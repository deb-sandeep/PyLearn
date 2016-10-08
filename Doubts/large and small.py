def sample_loops():
    largest = None
    smallest = None
    sum = 0
    count = 0
    nos = [1,2,3,4,5]
    for i in nos:
        count = count + 1
        sum = sum + i
        if largest is None or i > largest:  # if largest is None ? what is the need to write that
            largest = i
        if smallest is None or i < smallest:    # same as above
            smallest = i
    print ("Elements: ", count)
    print ("Sum: ", sum)
    print ("Largest: ", largest)
    print ("Smallest: ", smallest)


# how can i take a list as user input?
