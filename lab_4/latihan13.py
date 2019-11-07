lebar = int(input('Lebar dasi (harus genap): '))

tinggi = lebar // 2
counter = 1;

for x in range(tinggi - 1):
    print('|', end='') # garis kiri
    for y in range(x): # angka di kiri
        print(counter, end='')
        counter = (counter + 1) % 10
    print('\\', end='') # miring kiri
    for y in range(lebar - 2 * x - 4): # kosong di tengah
        print(' ', end='')
    print('/', end='') # miring kanan
    for y in range(x): # angka di kanan
        print(counter, end='')
        counter = (counter + 1) % 10
    print('|') # garis kanan

for x in range(tinggi - 1):
    print('|', end='') # garis kiri
    for y in range(tinggi - x - 2): # angka di kiri
        print(counter, end='')
        counter = (counter + 1) % 10
    print('/', end='') # miring kiri
    for y in range(x * 2): # kosong di tengah
        print(' ', end='')
    print('\\', end='') # miring kanan
    for y in range(tinggi - x - 2): # angka di kanan
        print(counter, end='')
        counter = (counter + 1) % 10
    print('|') # garis kanan
