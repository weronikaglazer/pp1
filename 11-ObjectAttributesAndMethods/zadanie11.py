class Area:
    @staticmethod
    def triangle_area(base,height):
        return base*height/2
    
    @staticmethod
    def rectangle_area(a,b):
        return a*b
    
    @staticmethod
    def circle_area(radius):
        return 3.14*(radius**2)
    
print(Area.circle_area(3))
print(Area.rectangle_area(4,7))
print(Area.triangle_area(6,2))