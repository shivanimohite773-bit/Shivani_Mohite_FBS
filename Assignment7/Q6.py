for i in range(1,6):
    for j in range(i,6):
        # print(j,end=' ')
        if(j==i or i == 1 or j == 5):
            print(j,end=' ')
        else:
            print(' ',end=' ')
    print()