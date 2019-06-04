
def suit(x, y):
    if(x == 0):
        return True;
    i = 1;
    while(x-i >= 0):
        if(a[x-i] == y or a[x-i]-y == i or a[x-i]-y == -i):
            return False
        i += 1
    return True

def printAll(n):
    for i in range(n):
        j = 0
        while(j < a[i]):
            print('O', end=' ')
            j += 1
        print('X', end=' ')
        j += 1
        while(j < n):
            print('O', end=' ')
            j += 1
        print()
    print('===============')

def start():
    count = 0;
    global a
    n = int(input('Number of queens:'))
    a = [0 for i in range(n)]
    i = 0
    while(i < n):
        j = a[i]
        while(j < n):
            if(suit(i, j)):
                a[i] = j
                i += 1
                break
            j += 1
        if(j == n):
            a[i] = 0
            i -= 1
            if(a[i] == n-1):
                if(i == 0):
                    break
                else:
                    a[i] = 0
                    i -= 1
                    a[i] += 1
            else:
                a[i] += 1
        if(i == n):
            count += 1
            print('Method ', count)
            printAll(n)
            i -= 1
            if(a[i] == n-1):
                a[i] = 0
                i -= 1
                a[i] += 1
            else:
                a[i] += 1
    print('Total method:', count)

if __name__ == '__main__':
    start()