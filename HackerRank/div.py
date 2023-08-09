if __name__ == '__main__':
    a = int(input())
    b = int(input())
    
    try:
        print(a//b)
        print(a/b)
    except ValueError:
        print("Invalid input.Please enter integer values")
