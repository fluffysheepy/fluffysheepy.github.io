def big_fibonacci(n):
    a=1
    b=1
    c=a+b
    if n<1:
        return("Error")
    if n==1:
        return 1
    while len(str(c))<n:
        a=b
        b=c
        c=a+b
    return c
