def is_prime(n):
    if n==2:
        return(True)
    elif n<=1:
        return(False)
    a=2
    while a<n:
        if n%a==0:
            return(False)
        a=a+1
    return(True)