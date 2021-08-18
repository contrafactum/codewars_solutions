def array_diff(a, b):
    #testing base cases
    if not b:
        return a
    if not a:
        return a
    else:  
        for i in b:
            while i in a:
                a.remove(i)
        return a
