#class is defined
class Circle:
    #__init__ method, which is the constructor.
    def __init__(self, radius_list):
        #self.radius_list was assigned the radius_values list in the constructor
        self.radius_list = radius_list

# Example usage
#a list of integers named radius_values. Each integer in this list represents a radius value for a circle.
radius_values = [10, 501, 22, 37, 100, 999, 87, 351]

#The radius_values list is passed as an argument to the constructor (__init__ method) of the Circle class.
circle = Circle(radius_values)

# prints the radius_list attribute of the circle object.
print(circle.radius_list)
