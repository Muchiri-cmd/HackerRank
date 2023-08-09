if __name__ == '__main__':
    
    try:
        n = int(input())
        arr = list(map(int, input().split()))
        merit=set(arr)#removes duplicate
        merit_list=list(sorted(merit))#returns a sorted list
        print(merit_list[-2])
                
    
    except ValueError:
        print("Enter a valid score")