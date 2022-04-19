for i in range(1, 100):
    if i % 3 == 0 and i % 5 == 0:
        print("ThreeFive", end ="")
    elif i % 3 == 0 or i % 5 == 0:
        if i % 5 == 0:
            print("Five", end="")
        else:
            print("Three", end="")
    else:
        print(i, end="")
    print("")