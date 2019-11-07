def max_cap(s):
    max_cap = None
    for i in s:
        if(i.isupper()):
            if(max_cap == None):
                max_cap = i
            elif(i > max_cap):
                max_cap = i
    print(max_cap)
    return max_cap

max_cap('belAjaR PyThon DengaN geMBirA')