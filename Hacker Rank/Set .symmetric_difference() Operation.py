if __name__ == '__main__':

    n_A = int(input())
    set_A = set(map(int, input().split()))
    
    n_B = int(input())
    set_B = set(map(int, input().split()))
    
    symmetric_difference_set = set_A.symmetric_difference(set_B)

    print(len(symmetric_difference_set))
