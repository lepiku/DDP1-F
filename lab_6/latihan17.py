def baca_matriks(baris,kolom):
    return sum([input().split(" ") for i in range(baris)],[])
    '''
    sum(  [[1, 2], [3, 4]]  , []) = [1, 2, 3, 4]
    '''
def bandingkan_matriks(matriks_1,matriks_2):
    matriks_1.sort()
    matriks_2.sort()
    return matriks_1 == matriks_2

print("Masukkan matriks pertama:")
ukuran_1 = input("Masukkan dimensi (baris dan kolom, dipisah oleh spasi): ").split(" ")
matriks_1 = baca_matriks(int(ukuran_1[0]),int(ukuran_1[1]))
print("Masukkan matriks kedua:")
ukuran_2 = input("Masukkan dimensi (baris dan kolom, dipisah oleh spasi): ").split(" ")
matriks_2 = baca_matriks(int(ukuran_2[0]),int(ukuran_2[1]))

if bandingkan_matriks(matriks_1,matriks_2):
    print("Isi matriks sama!")
else :
    print("Isi matriks berbeda!")