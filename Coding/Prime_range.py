start = 1
end = 10
for i in range(start, end):
    if i > 1:
        for j in range(2, i):
            if(i % j == 0):
                break
        else:
            print(i)

## Sum of sqaures of n
def squaresum(n) : 
    sm=0
    for i in range(0, n+1):
        sm = sm + pow(i, 2)
    return sm
n=4
print(squaresum(n))

print(max(5,4))
