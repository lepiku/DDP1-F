def baca_list():
    return input().split(" ")
def list_sama(list_1,list_2):
    list_1.sort()
    list_2.sort()
    return list_1 == list_2
print("masukkan list pertama (angka dipisah oleh spasi): ")
list_1 = baca_list()
print("masukkan list kedua (angka dipisah oleh spasi): ")
list_2 = baca_list()

if list_sama(list_1,list_2):
    print("Isi list sama!")
else:
    print("Isi list berbeda!")