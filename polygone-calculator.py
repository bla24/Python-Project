# Build a Polygon Area Calculator

import math

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height
    
    def get_perimeter(self):
        return 2 * (self.width + self.height)
    
    def get_diagonal(self):
        return math.sqrt((self.width ** 2) + (self.height ** 2))
    
    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        else:
            return ("*" * self.width + "\n") * self.height
    
    def get_amount_inside(self, Rectangle):
        return (self.width // Rectangle.width) * (self.height // Rectangle.height)
    

    def set_width(self, new_width):
        self.width = new_width
        return "Width updated"

    def set_height(self, new_height):
        self.height = new_height
        return "Height updated"

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"

class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)
        
    def set_side(self, new_side):
        self.width = new_side
        self.height = new_side
        return "Side updated"
    
    def set_width(self, new_length):
        self.width = new_length
        self.height = new_length
        return "Width updated"
    
    def set_height(self, new_length):
        self.height = new_length
        self.width = new_length
        return "Height updated"

    def get_perimeter(self):
        return 2 * (self.width + self.height)
    
    def get_area(self):
        return self.width * self.height

    def get_diagonal(self):
        return math.sqrt((self.width ** 2) + (self.height ** 2))
    
    def get_picture(self):
        if self.height > 50:
            return "Too big for picture."
        else:
            return ("*" * self.height + "\n") * self.height
    
    def get_amount_inside(self, Square):
        return (self.side // Square.width) * (self.side // Square.height)
    
    def __str__(self):
        return f"Square(side={self.width})"

rect = Rectangle(10, 5)
print(rect)
print(rect.get_perimeter())
print(rect.get_area())
print(rect.set_height(3))
print(rect.get_picture())

sq = Square(9)
print(sq)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())
