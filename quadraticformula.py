def solve_quadratic(a,b,c):
   root=b**2-4*a*c
   if root<0:
       return("None")
   elif root==0:
       return(-b/2*a)
   else:
       value1=(-b + root**0.5)/2*a
       value2=(-b - root**0.5)/2*a
       return(value1, value2)