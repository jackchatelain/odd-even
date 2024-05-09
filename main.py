i = input("Enter the number or range to check.\n")

if "-" in i:
    for i2 in range(int(i.split("-")[0]), int(i.split("-")[1]) + 1):
        if int(i2) % 2 == 0:
            print(f"{i2} is even")
        else:
            print(f"{i2} is odd")
else:
    if int(i) % 2 == 0:
        print(f"{i} is even")
    else:
        print(f"{i} is odd")
