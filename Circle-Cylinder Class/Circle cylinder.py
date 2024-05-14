from math import pi


class Circle:

    def __init__(self, radius=1.0):
        """Initialize constructor with default value 1.0"""
        self.radius = radius

    def __str__(self):
        """It gives description of circlr/instance by informal value"""
        return (f"Circle with radius {self.radius}.")

    def __repr__(self):
        """It gives description like __str__ but by formal value"""
        return 'Circle; radius={}'.format(self.radius)

    def get_area(self):
        """it gives area of circle"""
        return pi * self.radius ** 2


class Cylinder(Circle):
    """It is subclass of Circle class"""


    def __init__(self, radius=1.0, height=1.0):
        Circle.__init__(self,radius)
        self.height = height


    def __str__(self):
        """informal description as in Circle class"""
        return "Cylinder; radius ={}, height={}".format(self.radius, self.height)



    def __repr__(self):
        """formal description as in Circle class"""
        return self.__str__()



    def get_area(self):
        """Overriding. surface area of cylinder"""
        return 2 * pi * self.height * self.radius


    def get_volume(self):
        """volume of cylinder. get_area inherited from circle class"""
        return super().get_area() * self.height

circle1 = Circle()
print(circle1.radius)
print(str(circle1))
print(repr(circle1))
print(circle1.get_area())

circle2 = Circle(3.0)
print(circle2.radius)
print(str(circle2))
print(repr(circle2))
print(circle2.get_area())

cylinder1 = Cylinder()
print(cylinder1.radius)
print(cylinder1.height)
print(str(cylinder1))
print(repr(cylinder1))
print(cylinder1.get_area())
print(cylinder1.get_volume())

cylinder2 = Cylinder(1.5,3.0)
print(cylinder2.radius)
print(cylinder2.height)
print(str(cylinder2))
print(repr(cylinder2))
print(cylinder2.get_area())
print(cylinder2.get_volume())



