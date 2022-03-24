def is_prime(n):
    if n==2:
        return(True)
    elif n<=1:
        return(False)
    a=2
    while a<(n**0.5)+1:
        if n%a==0:
            return(False)
        a=a+1
    return(True)


l=[]
for i in range(10000,100000):
    if str(i)[::-1]==str(i):
        if is_prime(i):
            l.append(i)
print(l)