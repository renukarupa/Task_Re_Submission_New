class Circle:
    __pi = 3.141  # Class-level private variable

    def __init__(self, radius_list):
        self.radius_list = radius_list

    @classmethod
    def area(cls, radius):
        return cls.__pi * radius ** 2

    @classmethod
    def perimeter(cls, radius):
        return 2 * cls.__pi * radius

    def calculate_areas(self):
        return [self.area(r) for r in self.radius_list]

    def calculate_perimeters(self):
        return [self.perimeter(r) for r in self.radius_list]

# Example usage
radius_values = [10, 501, 22, 37, 100, 999, 87, 351]
circle = Circle(radius_values)

# prints the attribute of the circle object.
print("Radius values:", circle.radius_list)
print("Areas:", circle.calculate_areas())
print("Perimeters:", circle.calculate_perimeters())
