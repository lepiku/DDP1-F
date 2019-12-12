def decipher(kalimat, list_kotoran):
    if len(kalimat) == 0:
        return ''
    if kalimat[0] in list_kotoran:
        return decipher(kalimat[1:], list_kotoran)
    return kalimat[0] + decipher(kalimat[1:], list_kotoran)

if __name__ == '__main__':
    input_str = input("lul: ")
    list_kotoran = input("Kotoran: ").split(',')

    print(decipher(input_str, list_kotoran))
