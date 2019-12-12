n = 100000

L = []
for i in range(n):
    L.append(2 * i + 1)

O = [2 * i + 1 for i in range(n)]

print(L)
print(O)
print(O == L)




'''
After swap1, numList: [1, 2, 5, 4, 3]
After swap2, numList: [1, 2, 3, 4, 5]
'''




lst = [2.1, 4, "string", 8, 1]
a = 0
for i in lst:
    try:
        a += i
    except TypeError:
        print('Type Error')
        break
    except:
        print('Error')
        pass
    finally:
        print("i: " + str(i))
print("a: " + str(a))





import string

def hitung(kalimat):
    for char in string.punctuation:
        kalimat = kalimat.replace(char, ' ')

    print(kalimat) # contoh setelah di replace
    kalimat = kalimat.split()

    # hitung cou
    counter = {}
    for kata in kalimat:
        if kata not in counter:
            counter[kata] = 1
        else:
            counter[kata] += 1

    # untuk sort dari kecil ke besar
    output = list(counter.items())
    output.sort(key=lambda x: x[1])
    return(output)

print(hitung('Saya jalan-jalan ke pinggir jalan,.'))





def sumAll(filename):
    infile = open(filename, 'r')
    sums = 0

    isi_file = infile.read()
    for char in isi_file:

        if char.isnumeric():
            sums += int(char)

        # bisa juga pake try

        try:
            sums += int(char)
        except:
            pass


    infile.close()
    return sums

print("sumall input.txt =", sumAll('input.txt'))




import math

class Elips:
    def __init__(self, a, b):
        self.__a = a
        self.__b = b

    def getLuas(self):
        return math.pi * self.__a * self.__b

class Lingkaran(Elips):
    def __init__(self, a):
        super().__init__(a, a)

    def getRadius(self):
        return self._Elips__a

c1 = Lingkaran(7)
print(c1.getRadius())
print(c1.getLuas())




class A:
    def __init__(self, i = 10):
        print("calling init in class A")
        self.i = i

    def m(self):
        print("calling m in A")
        self.i //= 2

class B(A):
    def __init__(self, j = 100, i = 50):
        print("calling init in class B")
        A.__init__(self)
        self.j = j

    def m(self):
        super().m()
        print("calling m in B")
        self.j *= 5

def main():
    b = B() #Line 1 j=500 i=5
    b.m() #Line 2
    print(b.i) #Line 3
    print(b.j) #Line 4
    print(isinstance(b,object)) #Line 5

main()
