n = 5

#top half
for i in range(n):
    for j in range(n-i-1):
        print(' ', end=' ')
    print('*', end=' ')

    if(i>0):
        for j in range(2*i-1):
                print(' ', end=' ')
        print('*')
    else:
         print()

#bottom half
for i in range(n - 2 , -1, -1):
    for j in range(n-i-1):
        print(' ', end=' ')
    print('*', end=' ')

    if(i > 0):
        for j in range(2*i-1):
            print(' ', end=' ')
        print('*')
    else:
         print()