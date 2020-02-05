## list
x=[1,2,3,4]
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