if __name__ == '__main__':
    n = int(input())
    try:
        if 1<=n<=20:
            for i in range(0,n):
                print(i**2)
        else:
            print("Please enter a number between 1 and 20 inclusive")
    except ValueError:
        print("Invalid input.Kindly enter a value between 1 and 20")
                    