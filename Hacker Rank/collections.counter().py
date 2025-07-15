from collections import Counter

if __name__ == '__main__':
    X = int(input())
    shoe_sizes = list(map(int, input().split()))
    shoe_counter = Counter(shoe_sizes)
    N = int(input())
    total_earnings = 0
    
    for _ in range(N):
        size, price = map(int, input().split())
        if shoe_counter[size] > 0:
            total_earnings += price
            shoe_counter[size] -= 1
    
    print(total_earnings)
