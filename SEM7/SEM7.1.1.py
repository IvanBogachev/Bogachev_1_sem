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
n = int(input())
vvod = []
vectora = []
rez = Vector(0,0,0)
for i in range(n):
    str = input()
    vvod.append(list(str.split()))
for i in range(n):
    v =  Vector(int(vvod[i][0]),int(vvod[i][1]),int(vvod[i][2]))
    vectora.append(v)
for i in range(n):
    rez+=vectora[i]
print((rez.x)/n,(rez.y)/n,(rez.z)/n)




