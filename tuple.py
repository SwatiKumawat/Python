name = input("Enter file:")
handle = open(name)
lst=list()
count=dict()
lst1=list()

for lines in handle:
    if lines.startswith("From "): 
       line=lines.split()
       #print(lines)
       #print(line)
       time=line[5]
       #print(time)
       t=time.split(":")
       hour=t[0]
       #print(hour)
       lst.append(hour)
#print(lst)
for word in lst:
    count[word]=count.get(word,0)+1
for key,value in count.items():
    tup=(key,value)    
    lst1.append(tup)
lst1=sorted(lst1)
for key,value in lst1:
    print(key,value)
