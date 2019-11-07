sisi = int(input('Masukkan panjang sisi persegi: '))
kotak_x = int(input('Masukkan komponen X dari kiri bawah persegi: '))
kotak_y = int(input('Masukkan komponen Y dari kiri bawah persegi: '))
titik_x = int(input('Masukkan komponen X dari yang ingin di cek: '))
titik_y = int(input('Masukkan komponen Y dari yang ingin di cek: '))

msg_tepi = 'Di tepi'
msg_dalam = 'Di dalam'
msg_luar = 'Di luar'

if (titik_x == kotak_x or titik_x == kotak_x + sisi):
    if (titik_y >= kotak_y and titik_y <= kotak_y + sisi):
        print(msg_tepi)
    else:
        print(msg_luar)

elif (titik_x > kotak_x and titik_x < kotak_x + sisi):
    if (titik_y == kotak_y or titik_y == kotak_y + sisi):
        print(msg_tepi)
    elif (titik_y > kotak_y and titik_y < kotak_y + sisi):
        print(msg_dalam)
    else:
        print(msg_luar)

else:
    print(msg_luar)



