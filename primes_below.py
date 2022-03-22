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

def primes_below(n):
    l=[]
    for prime in range(2,n):
        if is_prime(prime):
            l.append(prime)
    return(l)