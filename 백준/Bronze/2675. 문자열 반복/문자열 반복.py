t = int(input())

for i in range(0, t):
    r, str = input().split()
    for i in range(len(str)):
        print(int(r) * str[i], end='')
    print()