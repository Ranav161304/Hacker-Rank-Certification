from collections import deque

def can_stack(cubes):
    left = 0
    right = len(cubes) - 1
    last = float('inf')
    while left <= right:
        if cubes[left] >= cubes[right]:
            if cubes[left] > last:
                return "No"
            last = cubes[left]
            left += 1
        else:
            if cubes[right] > last:
                return "No"
            last = cubes[right]
            right -= 1
    return "Yes"

T = int(input())
for _ in range(T):
    n = int(input())
    cubes = list(map(int, input().split()))
    print(can_stack(cubes))
