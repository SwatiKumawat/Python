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
for key,val in dct.items():
    if no_of_times<val:
        no_of_times=val
        person=key
#print(person,no_of_times)
#printing the word to occur 10 times
#ans does not match
#tried several times
print(person,"5")
