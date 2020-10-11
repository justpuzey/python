class Point:
    """
    docstring - this allows us to add documentation to any classes that are created
    """
    #all methods created within a class should have at least one variable. The first variable is "self" by convention

    #init is a special Constructor Method that allows you to initialize any new object with devault values/settings
    default_color = "red"#class-level attributes can be set to provide all objects with same attributes

    def __init__(self,x ,y):
        self.x = x
        self.y = y


    def print_values(self):
        print(f"first value is: {self.x}, second value is: {self.y}")

point = Point('justin',2)
print(isinstance(point,Point))
point.print_values()
point.z = "puzey" #Python Objects are dynamic. Not all attributes must be defined within the object itself, they can be defined later

print(f"{point.z}, {point.x}")


another_point = Point(5,6)
print(another_point.default_color) #creating another instance of an object picks up the same default attributes

Point.default_color = "Yellow"
print(another_point.default_color) #modifying the class-level attributes affects all object instances through inheretance

