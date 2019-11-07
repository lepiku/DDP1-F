def isi_list(pengen_isi, baris, kolom):
    namron_punya_cnt = 0
    for i in range(baris):
        if i % 2 == 0:
            for j in range(kolom):
                pengen_isi[i][j] = namron_punya_cnt
                namron_punya_cnt += 1
        else:
            for j in range(kolom - 1, -1, -1):
                pengen_isi[i][j] = namron_punya_cnt
                namron_punya_cnt += 1
 
def cetak_list(pengen_cetak, baris, kolom):
    # disini harusnya tidak fixed 5
    #for i in range(5):
    # menjadi
    for i in range(baris):
        # disini harusnya tidak fixed 7
        #for i in range(7):
        # menjadi
        for j in range(kolom):
            print(namron_punya_list[i][j], end=' ')
        print()

# salah disini, kalau list dikali maka hasilnya merujuk ke list yang sama karena mutable
#namron_punya_list = [[0] * 7] * 5
# menjadi
namron_punya_list = [[0 for x in range(7)] for y in range(5)]
isi_list(namron_punya_list, 5, 7)
cetak_list(namron_punya_list, 5, 7)
