from Shape import Shape


class Triangle(Shape):

    def show_area(self):
        area = (self.width*self.height)/2
        return area

