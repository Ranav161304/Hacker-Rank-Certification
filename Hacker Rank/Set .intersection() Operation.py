if __name__ == '__main__':
    # Read the number of elements in set A
    n_A = int(input())
    # Read the elements of set A
    set_A = set(map(int, input().split()))
    
    # Read the number of elements in set B
    n_B = int(input())
    # Read the elements of set B
    set_B = set(map(int, input().split()))
    
    # Compute the intersection of set A and set B
    intersection_set = set_A.intersection(set_B)
    
    # Output the number of elements in the intersection set
    print(len(intersection_set))
