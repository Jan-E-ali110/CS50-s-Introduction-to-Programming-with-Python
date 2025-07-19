Amount_Due = 50
print(f"Amount Due: {Amount_Due}")
change_owed = []


while True:
    user = int(input("Insert Coin (or 0 to exit loop): "))
    if user == 0:
        break

    if user == 25 or user == 10 or user == 5:
        Amount_Due -= user
        print(f"Amount Due: {Amount_Due}")


        if not change_owed:
            change_owed.append(user)
        else:
            change_owed[0] += user

        if change_owed[0] >= 50:
            result =change_owed[0] - 50
            print(f"Change Owed: {result}")
            break


    else:
        print(f"Amount Due: {Amount_Due}")
        break

