a, b, c = map(int, input().split())
d = int(input()) #초단위

c += d % 60
b += (d // 60) % 60
a += d // 3600

if c >= 60:
    b += 1
    c -= 60
if b >= 60:
    a += 1
    b -= 60

a %= 24

print(a, b, c)