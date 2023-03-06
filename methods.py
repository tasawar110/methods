#List methods
a=[1,2,3,4,5]
print(a)
d=a.count(1)
print(d)
e=a.index(2)
print(e)
a.insert(4,5)
print(a)
g=a.pop(0)
print(g)
h=a.remove(3)
print(a)
i=a.reverse()
print(a)
j=a.sort()
print(a)
a.clear()
print(a)
#strings methods

a='tasawar'
c=a.casefold()
print(c)


d=a.format()
print(d)
e=a.isalnum()
print(e)
#Set methods
a={1,2,3,4,5}
b={5,6,7,89,9}
a.add(8)
print(a)
c=a.difference(b)
print(c)
d=a.difference_update(b) 
print(d)
e=a.intersection_update(b)
print(e) 
f=a.isdisjoint(b) 
print(e)
#dictionary methods
a={'hi':[1,2,3],'hlo':[4,5,6]}
b=a.fromkeys([7,8,9])
print(b)

