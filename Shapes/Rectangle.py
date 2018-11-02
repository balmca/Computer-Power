from Shape import Shape


class Rectangle(Shape):

    def show_border(self):
        border_size = 2
        return border_size

    def show_perimeter(self):
        return (self.height*2)+(self.width*2)



