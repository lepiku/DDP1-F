import turtle
import math

# meminta input-input
print('Selamat datang dit TurtleTRON-3999 v2!')
bentuk = input('Masukkan bentuk yang ingin digambar (lingkaran/segitiga): ')
panjang = int(input('Masukkan panjang keliling gambar: '))
warna = input('Masukkan warna gambar: ')
isi = input('Apakah Anda ingin mengisi warna ke dalam gambar? ')

# menentukan warna garis
if warna == 'merah':
    warna = 'red'
elif warna == 'hijau':
    warna = 'green'
elif warna == 'kuning':
    warna = 'yellow'
elif warna == 'oranye':
    warna = 'orange'
elif warna == 'hitam':
    warna = 'black'
elif warna == 'biru':
    warna = 'blue'
turtle.color(warna)

# mulai mengisi warna
if isi == 'ya':
    turtle.begin_fill()

# menggambar bentuk
if bentuk == 'lingkaran':
    turtle.circle(panjang / math.pi / 2)
elif bentuk == 'segitiga':
    turtle.forward(panjang / 3)
    turtle.left(120)
    turtle.forward(panjang / 3)
    turtle.left(120)
    turtle.forward(panjang / 3)
    turtle.left(120)
else:
    print('Bentuk tidak dikenal')

# akhir dari mengisi warna
if isi == 'ya':
    turtle.end_fill()

# menulis branding dan copyright
turtle.color('black')
turtle.penup()
turtle.goto(0, 200)
turtle.write('TurtleTRON-3999 v2', font=('Arial', 12, 'normal'))
turtle.goto(-200, -200)
turtle.write('Copyright Asdos DDP1-F', font=('Arial', 12, 'normal'))
turtle.pendown()

# menyembunyikan panah
turtle.hideturtle()

turtle.mainloop()
