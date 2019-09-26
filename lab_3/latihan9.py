max_number = input()
counter = 1
while counter <= 25:
    if(counter % 21 == 0):
        print("BingBung!")
    elif(counter % 3 == 0):
        print("Bing!")
    elif(counter % 7 == 0):
        print("Bung!")
    else:
        print(counter)
    counter += 1