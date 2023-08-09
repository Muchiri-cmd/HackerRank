def door_mat(rows,columns):
    pattern='.|.'
    welcome='WELCOME'
    
    #prints the upper part of the mat
    for i in range(1,rows,2):
        print((pattern*i).center(columns,'-'))
    
    #prints the center part with welcome
    print(welcome.center(columns,'-'))
    
    #prints the bottom part of the pattern
    for i in range(rows-2,0,-2):
        print((pattern*i).center(columns,'-'))
    
if __name__=='__main__':
    rows,columns=map(int,input().split())
    door_mat(rows , columns)