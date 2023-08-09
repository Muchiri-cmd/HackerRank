def split_and_join(line):
    # write your code here
    
    split=line.split(" ")#splits input using the space delimiter
    return '-'.join(split)#joins split input 2 form a string
  
    

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)