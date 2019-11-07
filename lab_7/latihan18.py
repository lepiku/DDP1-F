print("Masukkan data:")

# dict kosong
bukan_penyusup = dict()
penyusup = dict()
# counter
jumlah_bukan_penyusup = 0
jumlah_penyusup = 0

while(True):
    inp = input()
    if inp == "":
        break

    splitted_inp = inp.split(",")
    nama = splitted_inp[0]
    angkatan = splitted_inp[1]
    ada_nametag = eval(splitted_inp[2])
    if ada_nametag:
        if angkatan in bukan_penyusup:
            bukan_penyusup[angkatan].append(nama)
        else:
            bukan_penyusup[angkatan] = [nama]

        jumlah_bukan_penyusup += 1
    else:
        if angkatan in penyusup:
            penyusup[angkatan].append(nama)
        else:
            penyusup[angkatan] = [nama]
    
        jumlah_penyusup += 1

print("Peserta:")
print("Jumlah: " + str(jumlah_bukan_penyusup))

for angkatan in bukan_penyusup:
    print(angkatan + " : " + str(len(bukan_penyusup[angkatan])))
    for nama in bukan_penyusup[angkatan]:
        print("- " + nama)

print("\nPenyusup:")
print("Jumlah: " + str(jumlah_penyusup))

for angkatan in penyusup:
    print(angkatan + " : " + str(len(penyusup[angkatan])))
    for nama in penyusup[angkatan]:
        print("- " + nama)
