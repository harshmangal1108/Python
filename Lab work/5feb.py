## list
x=[4,1,2,3,4]
print(type(x))
### access item using index
print(x[3])
print(x[-1])
### List slicing
print(x[1:]) ## 1 to all
print(x[:3]) ##upto index 2
print(x)
x[2]="HII"
print(x[2])
#### loop
for i in range(1,8):
    print("*"*i)
####check if item
if "HII" in x[4:]:
    print("yes")
else:
    print("no")
print("Enter value to search")
#y=int(input())
"""if y in x:
    print("yes %d is present"%y)
else :
    print("no")"""
#### length of list
print(len(x))
#### adding item in list
x.append("harsh")
print(x)
x.remove(4) ### 4 is value
print(x)
x.pop(4) ### 4 is index
del x[1]
print(x)
z=list(x)
### copying a list
y=list(x)
print(y)
### 2nd method
y=x.copy()
###join 2 list

#### 2nd method
for n in y:
    x.append(y)
print(x)
#### sorting in list
print(z.sort())