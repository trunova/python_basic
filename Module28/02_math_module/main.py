import math


class MyMath:
    
    @classmethod
    def circle_len(cls, radius=1) -> float:
        return 2 * math.pi * radius

    @classmethod
    def circle_sq(cls, radius) -> float:
        return math.pi * radius * radius

    @classmethod
    def cubeVolume(cls, a: float) -> float:
        return a * a * a

    @classmethod
    def surface_area_of_a_sphere(cls, radius: float) -> float:
        return math.pi * radius * radius


res_1 = MyMath.circle_len(radius=5)
res_2 = MyMath.circle_sq(radius=6)
print(res_1)
print(res_2)
