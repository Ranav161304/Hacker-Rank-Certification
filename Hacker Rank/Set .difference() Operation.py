if __name__ == '__main__':
    n_A = int(input())
    set_A = set(map(int, input().split()))
    
    n_B = int(input())
    set_B = set(map(int, input().split()))
    
    difference_set = set_A.difference(set_B)
    
    print(len(difference_set))
