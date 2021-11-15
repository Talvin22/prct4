for dig in range(1, 100):
    for i in range(2, dig):
        if dig % i == 0:
            break
        else:
            print(dig, end = ' _|_ ')
            break