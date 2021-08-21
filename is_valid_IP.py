# returns true if the given IP address as a string is valid
def is_valid_IP(strng):
    if strng == "":
        return False
    else:
        x = strng.split(".")
        if len(x) == 4:
            y = []
            for i in x:
                if i.isnumeric():
                    if 0 <= int(i) <= 255:
                        if int(i) < 100 and 0 < int(i) and i.startswith('0'):
                            y.append(False)
                        elif int(i) < 100 and not i.startswith('0'):
                            y.append(True)
                    else:
                        y.append(False)
                else:
                    y.append(False)
            return all(y)
        else:
            return False
