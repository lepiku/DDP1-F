self_LP=1000 #Self life point
enemy_LP=1000 #Enemy life point
while True:
    print("----------------------------------------")
    print("LP Anda:",self_LP)
    print("LP Musuh:",enemy_LP)
    print("----------------------------------------")
    print("Apa yang ingin Anda lakukan?")
    print("1. Serangan dengan scratch (100 LP)")
    print("2. Serangan dengan throw (300 LP)")
    print("3. Serangan dengan flamethrower (500 LP)")
    print("4. Tangkap musuh Anda")
    type_attack = int(input("Masukkan nomor pilihan: ")) #Input type attack  

    #check the attack type
    if(type_attack == 1):
        enemy_LP -= 100
        print("Anda menggunakan scratch dan mengurangi LP musuh sebanyak 100 poin.")
    elif(type_attack == 2):
        enemy_LP -= 300
        print("Anda menggunakan throw dan mengurangi LP musuh sebanyak 300 poin.")
    elif(type_attack == 3):
        enemy_LP -= 500
        print("Anda menggunakan flamethrower dan mengurangi LP musuh sebanyak 500 poin.")

    elif(type_attack == 4):
        if(enemy_LP <= 500):
            print("Anda berhasil menangkap musuh Anda!")
            break
        else:
            print("Anda mencoba menangkap musuh Anda, namun gagal!")
    else:
        continue
    
    #check enemy lp
    if(enemy_LP <= 0):
        print("Anda menang!")
        break

    print("LP musuh yang tersisa sebanyak",enemy_LP,"poin")
    
    #enemy attack
    self_LP -= 200
    print("Musuh Anda menggunakan slap dan mengurangi LP anda sebnayak 200 poin")

    #check self lp
    if(self_LP <= 0):
        print("Anda kalah!")
        break
    
    print("LP Anda yang tersisa sebanyak",self_LP,"poin.")
    