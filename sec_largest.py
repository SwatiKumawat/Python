if __name__ == '__main__':
    n = int(input())
    array=list(map(int, input().split()))

    largest=0
    sec_largest=0
    for i in array:
        if(int(i)>largest):
            sec_largest=largest
            largest=int(i)
        elif (int(i)>sec_largest and int(i)!=largest):
                sec_largest=int(i)
    print(sec_largest)
    
    '''
    METHOD2:
    
    array1=set(array)
    array1.remove(max(array1))
    print(max(array1))
    #print(array)
    
    '''
