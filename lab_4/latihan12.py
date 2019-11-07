N = int(input())

tinggi = (N//2)-1
cnt = 1
for i in range(1,tinggi+1):
    print("|", end="")
    for j in range(i-1):
        print(cnt % 10, end="")
        cnt+= 1
    print("\\", end="")
    for j in range(N-(2*(i+1))):
        print(" ",end="")
    print("/",end="")
    for j in range(i-1):
        print(cnt % 10, end="")
        cnt+=1
    print("|")

for i in range(tinggi,0,-1):
    print("|", end="")
    for j in range(i-1):
        print(cnt%10, end="")
        cnt += 1
    print("/", end="")
    for j in range(N-(2*(i+1))):
        print(" ",end="")
    print("\\",end="")
    for j in range(i-1):
        print(cnt % 10, end="")
        cnt += 1
    print("|")
