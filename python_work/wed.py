# ex1
t = (1,)
print t[-1]

# ex2
r = range(100,201)
tup = tuple(r)
print tup[0],tup[-1]

# ex3
mylist = [23,"hi",2.4e-10]
for i in mylist:
	print i,"",mylist.index(i)

mylist1 = tuple(mylist)
for a,b in enumerate(mylist1):
	print a,b



