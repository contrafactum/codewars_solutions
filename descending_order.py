def descending_order(num):

    # 1. converting the input to a string
    # 2. sorting the string's characters into a list
    # 3. reconverting the list to a string
    # 4. reversing by array slicing
    # 5. converting it back to an integer
    
    return int(''.join(sorted(str(num)))[::-1])
