def search_duplicate(list):
    duplicate_number=None
    duplicate_number_counter=0
    for i in list:
        count = list.count(i)
        if(count > duplicate_number_counter):
            duplicate_number = i
            duplicate_number_counter = count
    return duplicate_number

list = input("Masukkan sebuah deret bilangan yang akan dicari duplikatnya: ").split(" ")
print("Bilangan {} duplikat".format(search_duplicate([int(i) for i in list])))