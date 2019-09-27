name=input('enter file name:')
fh=open(name)
lst=list()
dct=dict()
for lines in fh:
    if lines.startswith("From"):
        words=lines.split()
        lst.append(words[1])
#print(lst)
for element in lst:
    dct[element]=dct.get(element,0)+1
#print(dct)
person=None
no_of_times=None
for key,value in dct.items():
    if no_of_times is None or no_of_times<value:
        no_of_times=value
        person=key
print(person,no_of_times)
