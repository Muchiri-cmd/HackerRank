def rack_em_up(side):
    stacked_cube_l=float("inf")#ground-zone for any cube
    left_runner=0 #blicker
    right_runner=len(sides_ls)-1 #blicker
    
    #loop till opps cross
    while left_runner<=right_runner:
        left_hollow=sides_ls[left_runner]
        right_hollow=sides_ls[right_runner]
        
        #if both large,impossible
        if left_hollow>stacked_cube_l and right_hollow>stacked_cube_l:
            print("Noooooo")
            return
        else:
            #determine largest
            
            if left_hollow>=right_hollow and left_hollow <=stacked_cube_l:
                stacked_cube_l=left_hollow
                left_runner+=1
            elif right_hollow > left_hollow and right_hollow <= stacked_cube_l:
                stacked_cube_l=right_hollow
                right_runner-=1
            else:#largest side too large
                print("Nooooo")
                return
    print("Hell Yeah! Ts wat im talkin bout'")
                
#input shi*
no_of_tests=int(input())
for _ in range(no_of_tests):
    n=int(input())
    sides_ls=[int(num) for num in input().split()]
    rack_em_up(sides_ls)
