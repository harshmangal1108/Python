##3 tuple :ordered or unchangable
x=(1,2,3,4,"apple","banana")
print(x)
type(x)
###access elements
print(x[3])
###3 range of index
print(x[1:5])
print(x[-4:-1])
''''### changing value in tuple
x=("apple","banana","mango")
y=list(x)
y[2]="orange"
#### adding item
y.insert(3,"grape")
print(y)
x=tuple(y)
print(x)'''
### loops
for n in x:
    print(n)
#### check if item exists
if 'orange'  in x:
    print("present")
else:
    print("not present")
####tuple length
print(len(x))
### deleting whole tuple
#del(x)
#print(x)
tuple=(5,2)
print(tuple)
print(type(tuple))
###3 joining tuples
z=x+tuple
print(z)
print(type(z))
###count a value
print(z.count(2))
