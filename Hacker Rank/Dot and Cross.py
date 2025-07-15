import numpy

N = int(input())

A = []
for _ in range(N):
    A.append(list(map(int, input().split())))
A = numpy.array(A)

B = []
for _ in range(N):
    B.append(list(map(int, input().split())))
B = numpy.array(B)

result = numpy.dot(A, B)

print(result)
