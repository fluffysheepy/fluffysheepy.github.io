def my_reverse(n):
    l=[]
    nlength=len(n)
    while nlength>0:
        print(l)
        print(nlength-1)
        l.append(n[nlength-1])
        nlength-=1
    return l
print(my_reverse([1,2,3,4,5]))