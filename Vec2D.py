import math

class Vec2D(tuple):
    def __new__(cls, x, y):
        return tuple.__new__(cls, (x, y))
    
    def __add__(self, other):
        return Vec2D(self[0]+other[0], self[1]+other[1])
    
    def __mul__(self, other):
        if isinstance(other, Vec2D):
            return self[0]*other[0]+self[1]*other[1]
        return Vec2D(self[0]*other, self[1]*other)
    
    def __rmul__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return Vec2D(self[0]*other, self[1]*other)
        
    def __sub__(self, other):
        return Vec2D(self[0]-other[0], self[1]-other[1])
    
    def __neg__(self):
        return Vec2D(-self[0], -self[1])
    
    def __abs__(self):
        return (self[0]**2 + self[1]**2)**0.5

    def __getnewargs__(self):
        return (self[0], self[1])
    
    def __repr__(self):

        return "Vec2D(%.2f,%.2f)" % (self[0],self[1])

    def moveAwayFromPoint(self,vec,distance):
        a = math.radians(self.angle(vec))
        return self+Vec2D(math.sin(a)*distance,math.cos(a)*distance)
    
    def rotate(self,angle):
        perp = Vec2D(-self[1], self[0])
        angle = angle * math.pi / 180.0
        c, s = math.cos(angle), math.sin(angle)
        return Vec2D(self[0]*c+perp[0]*s, self[1]*c+perp[1]*s)
    
    def distance(self,vec):
        return abs(complex(self[0]-vec[0],self[1]-vec[1]))

    def angle(self,vec):
        a = math.degrees(math.atan2(-(self[0]-vec[0]),-(self[1]-vec[1])))
        return a%360
    
    def rotateAroundPoint(self,vec,angle):
        x,y = vec
        a = self[0] - x
        b = self[1] - y

        return Vec2D(a,b).rotate(angle) + Vec2D(x,y)

    def getPointBetween(self,vec,d=0.5):
        return Vec2D(self[0]-(self[0]-vec[0])*d,self[1]-(self[1]-vec[1])*d)