t = int(input())

for _ in range(t):
    a = list(map(str,input().split()))
    result = float(a[0])
    for i in range(len(a)):
        if a[i] == '@':
            result *= 3
        elif a[i] == '%':
            result += 5
        elif a[i] == '#':
            result -= 7

    print("{:.2f}".format(result))