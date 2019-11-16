def max_nested_tuple(tuple):
    max = None
    if(len(tuple) == 0):
        return max
    for i in tuple:
        if(type(i) == type(())):
            max_temp = max_nested_tuple(i)
            if(max_temp != None):
                if(max == None):
                    max=max_temp
                elif(max < max_temp):
                    max = max_temp
        elif(max != None):
            if(i > max):
                max = i
        elif(max == None):
            max = i
    return max

print(max_nested_tuple(()))