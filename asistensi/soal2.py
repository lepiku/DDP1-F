def find_modus(a_list):
    modus_number = a_list[0]
    modus_count = a_list.count(modus_number)
    for i in a_list:
        count = a_list.count(i)
        if(count > modus_count):
            modus_number = i
            modus_count = count

    print(modus_number)
    return modus_number

find_modus([8,3,4,5,3,3,1,-1,5,-2])
find_modus([4])