def count_bits(n):
    #converting the input to binary and then converting it to a string
    a = str(bin(n))
    
    #removing the first two characters as they are 0b
    b = str(a[2:])
    
    #returning the count of 1s in the string
    return b.count("1")
