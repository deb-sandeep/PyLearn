def list_comprehensions():
    list1 = list()
    n1 = int(input(print("Enter length of list")))
    while len(list1)<n1:
        input1 = input(print("Enter a number"))
        value = int(input1)
        list1.append(value)
    print("Oringinal list: ", list1)
    
    squares_all = [n**2 for n in list1]
    
    squares_even = [[n,n**2] for n in list1 if n%2 == 0]
    
    squares_odd = [[n,n**2] for n in list1 if n%2 != 0]
    
    print("Squared list: ", squares_all)
    print("Squared even list: ", squares_even)
    print("Squared odd list: ", squares_odd)
    
    squares_mul_3 = [[n,n**2] for n in list1 if n%3 == 0]
    print("Squares of multiples of 3: ", squares_mul_3)
    
list_comprehensions()

# still trying to work on columnwise flattening 
