A, B = map(int, input().split())
C = int(input())

C_A = C // 60
C_B = C % 60

A += C_A
B += C_B

if B >= 60:
    A += 1
    B -= 60

if A >= 24:
    A -= 24

print(A, B)