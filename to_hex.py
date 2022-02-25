a=["0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f"]

def to_hex(n):
    leftdigit=a[n//16]
    rightdigit=a[n%16]
    return(leftdigit+rightdigit)
print(to_hex(188))

def hex_color(n1,n2,n3):
    red=to_hex(n1)
    green=to_hex(n2)
    blue=to_hex(n3)
    return(red+green+blue)
print("#"+hex_color(10,32,255))