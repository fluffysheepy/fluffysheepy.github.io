import math

class Triangle():
    def __init__(self, a, b, c):
        self.a=a
        self.b=b
        self.c=c
    
    def perimeter(self):
        return self.a + self.b + self.c
    
    def area(self):
        p=(self.a + self.b + self.c)/2
        return math.sqrt(p*(p-self.a)*(p-self.b)*(p-self.c))
    
    def scale(self, scale_factor):
        return Triangle(scale_factor * self.a, scale_factor * self.b,  scale_factor * self.c)

    def is_valid(self):
        if self.a + self.b > self.c:
            return(True)
        else:
            return(False)
    
    def is_right(self):
        if self.c**2 == self.a**2 + self.b**2:
            return(True)
        else:
            return(False)

t = Triangle(3,4,5)
print("Area = %d" % t.area())
print("Perimeter = %d" % t.perimeter())

print("Is it a valid triangle? %s" % t.is_valid())
print("Is it a right triangle? %s" % t.is_right())

q=t.scale(3)
print("Scaled triangle = %d" % q.a, q.b, q.c)
