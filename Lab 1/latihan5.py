import turtle
print("Selamat datang di TurtleTRON-3999!")
bentuk = input("Masukkan bentuk yang ingin digambar ('lingkaran' atau 'segitiga'): ")

if(bentuk == "lingkaran"):
    turtle.circle(100)
elif(bentuk == "segitiga"):
    turtle.forward(100)
    turtle.left(120)
    turtle.forward(100)
    turtle.left(120)
    turtle.forward(100)
    turtle.left(120)

turtle.mainloop()