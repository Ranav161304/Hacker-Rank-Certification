T = int(input())

for _ in range(T):
    input()  
    A = set(map(int, input().split()))
    input()  
    B = set(map(int, input().split()))
    
    print(A.issubset(B))
