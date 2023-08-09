if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    
    # Create a tuple from the integer list
    tuple_data = tuple(integer_list)
    
    # Compute and print the hash value of the tuple
    result = hash(tuple_data)
    print(result)
