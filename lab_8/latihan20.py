# With forloop
def max_nested_tuple_old(tuple):
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

# Without forloop
def max_nested_tuple(nested_tuple):
    # base case empty tuple
    if nested_tuple == ():
        return None

    # base case single element tuple
    if len(nested_tuple) == 1:
        if type(nested_tuple[0]) == int:
            return nested_tuple[0]
        return max_nested_tuple(nested_tuple[0]) # if tuple inside a tuple

    # tuple with elements > 1, separates the first element (left) and the rest (right)
    left = max_nested_tuple(nested_tuple[:1])
    right = max_nested_tuple(nested_tuple[1:])

    if left == None and right == None: # max(None, None)
        return None
    if left == None: # max(None, int)
        return right
    if right == None: # max(int, None)
        return left
    return max(left, right) # max(int, int)

if __name__ == '__main__':
    tup1 = (1,2,3,4)
    print(tup1, '->', max_nested_tuple(tup1))
    tup2 = (1,(2,5),(1,(((9)))))
    print(tup2, '->', max_nested_tuple(tup2))
    tup3 = ((), (((((()))))), ((), (()), ()))
    print(tup3, '->', max_nested_tuple(tup3))
    tup4 = ()
    print(tup4, '->', max_nested_tuple(tup4))

