def bintang(n):
    for i in range(n,0,-1):
        print(" "*(n-i),end="")
        print('*',end="")
        print(" "*((i*2)-3),end="")

        if(i != 1):
            print("*",end="")
        print()
        
n = input('bintang: ')
while n != '':
    bintang(int(n))
    n = input('bintang: ')