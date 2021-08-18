# This function will return the multiplicative persistence of the input positive number
# Make a number, multiply its digits, repeat until you hit a 1-digit number. 
# The amount of steps it took to reach the 1-digit number is the Multiplicative Persistence of that number.

def persistence(num):
    
    # inputs under 10 will yield 0 automatically 
    if num < 10:
        return 0
    else:
    
        n = 0 # this stores the number of steps
    
        # converting the input to list
        a = [int(x) for x in str(num)]
    
        # while loop 
        while len(a)>1:
        
            # multiplying the elements
            p = 1
            for x in a:
                p *= x
    
            # incrementing n to count the steps
            n += 1
    
            # p has now the product, time to turn p back into the list we're checking
            a.clear()
            a = [int(x) for x in str(p)]
 
        # returning the number of steps
        return n
