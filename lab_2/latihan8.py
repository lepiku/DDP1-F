panjang_persegi = int(input("Masukkan panjang sisi persegi: "))
x_kiri_bawah_pertama = int(input("Masukkan komponen X dari titik kiri bawah persegi pertama: "))
y_kiri_bawah_pertama = int(input("Masukkan komponen Y dari titik kiri bawah persegi pertama: "))
x_kiri_bawah_kedua = int(input("Masukkan komponen X dari titik kiri bawah persegi kedua: "))
y_kiri_bawah_kedua = int(input("Masukkan komponen Y dari titik kiri bawah persegi kedua: "))

y_kanan_atas_pertama = y_kiri_bawah_pertama + panjang_persegi
x_kanan_atas_pertama = x_kiri_bawah_pertama + panjang_persegi
y_kanan_atas_kedua = y_kiri_bawah_kedua + panjang_persegi
x_kanan_atas_kedua = x_kiri_bawah_kedua + panjang_persegi

#cek apakah ada koordinat x kiri bawah di persegi kedua yang berada di range titik x persegi pertama
if (x_kiri_bawah_pertama <= x_kiri_bawah_kedua and 
        x_kanan_atas_pertama >= x_kiri_bawah_kedua) :

    #cek apakah ada koordinat y kiri bawah di persegi kedua berada di range titik y persegi pertama
    if (y_kanan_atas_pertama >= y_kiri_bawah_kedua and 
            y_kiri_bawah_pertama <= y_kiri_bawah_kedua) :

        print("Persegi beririsan")

    #cek apakah ada koordinat y kanan atas di persegi kedua berada di range titik y persegi pertama
    elif (y_kanan_atas_pertama >= y_kanan_atas_kedua and 
            y_kiri_bawah_pertama <= y_kanan_atas_kedua):

        print("Persegi beririsan")

    #kondisi jika tidak memenuhi
    else:

        print("Persegi terpisah")

#cek apakah ada koordinat x kanan atas di persegi kedua yang berada di range titik x persegi pertama
elif (x_kiri_bawah_pertama <= x_kanan_atas_kedua and 
        x_kanan_atas_pertama >= x_kanan_atas_kedua):

    #cek apakah ada koordinat y kiri bawah di persegi kedua berada di range titik y persegi pertama
    if (y_kanan_atas_pertama >= y_kiri_bawah_kedua and 
            y_kiri_bawah_pertama <= y_kiri_bawah_kedua) :

        print("Persegi beririsan")

    #cek apakah ada koordinat y kanan atas di persegi kedua berada di range titik y persegi pertama
    elif (y_kanan_atas_pertama >= y_kanan_atas_kedua and 
            y_kiri_bawah_pertama <= y_kanan_atas_kedua):

        print("Persegi beririsan")

    #kondisi jika tidak memenuhi
    else:

        print("Persegi terpisah")
    
    #kondisi jika tidak memenuhi
else:
    
    print("Persegi terpisah")