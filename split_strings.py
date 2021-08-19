def split_strings(s):
    # this will hold the output list
    r = []
    
    # base case for empty string
    if s == "":
        return r
    # case for even-length input string
    if len(s) % 2 == 0:
        i = 0
        while i < int(len(s)):
            r.append(s[i:i+2])
            i += 2
        return r
    
    # case for odd-length input
    if len(s) % 2 != 0:
        i = 0
        while i < int(len(s)-1):
            r.append(s[i:i+2])
            i += 2
        e = s[-1] + "_"
        r.append(e)
        return r
