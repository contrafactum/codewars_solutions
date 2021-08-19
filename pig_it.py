def pig_it(text):
    w = text.split(sep=" ")
    r = [x[1:]+x[0]+"ay" if x.isalpha() else x for x in w]
    return ' '.join(r)
