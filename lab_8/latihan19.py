tgl = input("Masukkan tanggal undian: ").split(",")

def cibonacci(x,y,n):
    if(n == 0):
        return 0
    elif(n == 1):
        return x
    elif(n==2):
        return y
    else:
       return cibonacci(x,y,n-1) + cibonacci(x,y,n-2)

print("Angka pemenang:",tgl[2][2:],cibonacci(int(tgl[0]),int(tgl[1]),int(tgl[2][2:4])),tgl[2][:2])