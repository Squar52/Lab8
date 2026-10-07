import random

M = int(input("Введіть M: "))
N = int(input("Введіть N: "))

Q = max(M, N)

A = []

for i in range(M):
    row = []
    for j in range(N):
        row.append(random.randint(1, 30))
    A.append(row)

print("Масив A:")
for row in A:
    print(row)

B = []

for i in range(Q):
    row = []
    for j in range(Q):
        if i < M and j < N:
            row.append(A[i][j])
        else:
            row.append(3 ** len(row))
    B.append(row)

print("Масив B:")
for row in B:
    print(row)