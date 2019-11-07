file = open(input(),'r')
r1 = int(input("r1 "))
r2 = int(input("r2 "))
c1 = int(input("c1 "))
c2 = int(input("c2 "))

matrix = file.read().split("\n")
matrix.remove("")

for i in range(len(matrix)):
    matrix[i] = matrix[i].split(" ")

if(1<=r1<=r2<=len(matrix) and 1<=c1<=c2<=len(matrix[0])):
    for i in range(r1-1,r2):
        for j in range(c1-1,c2):
            print(matrix[i][j],end=" ")
        print()
else:
    print("Not Valid")

file.close()