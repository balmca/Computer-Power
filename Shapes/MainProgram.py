from Shape import Shape
from Rectangle import Rectangle
from Triangle import Triangle

shape = Shape(colour="Red", height=6, width=8)

print("This is just a Shape")          # show colour
print(shape.show_colour())

rectangle = Rectangle(colour="Red", height=6, width=8)

print("This is a Rectangle")           # show colour, border size and perimeter
print(shape.show_colour())
print(rectangle.show_border())
print(rectangle.show_perimeter())

triangle = Triangle(colour="Red", height=6, width=8)

print("This is a Triangle")            # show colour and area
print(shape.show_colour())
print(triangle.show_area())


