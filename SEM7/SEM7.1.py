class Vector():
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z
    def __add__(self,other):
        if isinstance(other,Vector):
            return Vector(self.x+other.x,self.y+other.y,self.z+other.z)
        if isinstance(other,int) or isinstance(other,float):
            return Vector(self.x+other,self.y+other,self.z+other)
    def __sub__(self, other):
        if isinstance(other,Vector):
            return Vector(self.x-other.x,self.y-other.y,self.z-other.z)
        if isinstance(other,int) or isinstance(other,float):
            return Vector(self.x-other,self.y-other,self.z-other)
    def __mul__(self, other):
        if isinstance(other,Vector):
            return Vector(self.x*other.x,self.y*other.y,self.z*other.z)
        if isinstance(other,int) or isinstance(other,float):
            return Vector(self.x*other,self.y*other,self.z*other)

V1=list(map(float, input().split()))
V2=list(map(float, input().split()))
n = float(input())

v1 = Vector(V1[0],V1[1],V1[2])
v2 = Vector(V2[0],V2[1],V2[2])

v3 = v1-v2
v4 = v1+v2
v5 = v1*v2
v6 = v1*n

print("вычитание +",v3.x,v3.y,v3.z)
print("сложение -",v4.x,v4.y,v4.z)
print("скалярное произведение ",v5.x+v5.y+v5.z)
print("умножение на число",v6.x,v6.y,v6.z)