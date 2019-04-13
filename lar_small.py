largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done" :
        break
    try:
        inum=int(num)
    except:
        print("Invalid input")
        continue
    #print(num)
    if largest is None:
        largest=inum
    elif largest<inum :
    	largest=inum
     
    if smallest is None:
        smallest=inum
    elif smallest>inum :
        smallest=inum
        
        
print("Maximum is", largest)
print("Minimum is", smallest)
