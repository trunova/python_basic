import math

class Circle:

    def __init__(self, x=0, y=0, r=1):
        self.x = x
        self.y = y
        self.r = r

    def S(self):
        return math.pi * self.r * self.r

    def P(self):
        return math.pi * 2 * self.r

    def increase(self, k):
        self.r * k

    def distanceBetweenCenters(self, circle):
        return math.sqrt(math.pow(self.x - circle.x, 2) + math.pow(self.y - circle.y, 2))

    def cross(self, circle):
        d = self.distanceBetweenCenters(circle)
        sumR = self.r + circle.r
        difR = abs(self.r - circle.r)
        if d < sumR and d > difR: return True
        return False

c1 = Circle(0, 0, 2)
c2 = Circle(3, 0, 2)
print(c1.cross(c2))
print(c2.cross(c1))