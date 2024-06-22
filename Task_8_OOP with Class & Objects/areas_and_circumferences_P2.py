class Circle:
    __pi = 3.141  # Class-level private variable

    #__init__ method, which is the constructor.
    def __init__(self, radius_list):
        #self.radius_list was assigned the radius_values list in the constructor
        self.radius_list = radius_list

    #calculate_areas Method compute the area for each radius in the list using the formula
    def calculate_areas(self):
        return [self.__pi * r ** 2 for r in self.radius_list]

    # calculate_circumferences Method compute the circumference for each radius in the list using the formula  
    def calculate_circumferences(self):
        return [2 * self.__pi * r for r in self.radius_list]

# Example usage
#a list of integers named radius_values. Each integer in this list represents a radius value for a circle.
radius_values = [10, 501, 22, 37, 100, 999, 87, 351]

#The radius_values list is passed as an argument to the constructor (__init__ method) of the Circle class.
circle = Circle(radius_values)

# prints the attribute of the circle object.
print("Radius values:", circle.radius_list)
print("Areas:", circle.calculate_areas())
print("Circumferences:", circle.calculate_circumferences())
