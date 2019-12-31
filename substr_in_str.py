def count_substring(string, sub_string):
    lst_string=list(string)
    lst_sub_string=list(sub_string)
    count=0
    for i in range(len(string)):
        if(lst_sub_string[0]==lst_string[i]):
            if(lst_string[i:i+len(lst_sub_string)]==lst_sub_string):
                count=count+1
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
