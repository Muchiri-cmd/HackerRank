def count_substring(string, sub_string):
    count=0#keepstrack of number of times substring is in string
    str_len=len(string)
    substr_len=len(sub_string)
    
    #loop through all possible start positions of substring
    for i in range(0,str_len-substr_len+1):
        #slice string and check if it matches substring
        if string[i:i+substr_len]==sub_string:
            count+=1
    
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)