def print_rangoli(size):
    li=list(map(chr,range(97,123)))#ascii range for chars.Here am making a 27 character list for chars a-z
    x=li[size-1::-1]+li[1:size]#generate middle string
    length=len('-'.join(x))#get fixed width size from middle string
    for i in range(1,size):#upper part of rangoli
        print('-'.join(li[size-1:size-i:-1]+li[size-i:size]).center(length,'-'))
    for i in range(size,0,-1):#bottom side of rangoli(reversed) 
        print('-'.join(li[size-1:size-i:-1]+li[size-i:size]).center(length,'-'))
        
if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)