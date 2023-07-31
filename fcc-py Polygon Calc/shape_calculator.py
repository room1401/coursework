class Rectangle:

  def __init__(self, width, height):
    self.width = width
    self.height = height

  def __str__(self):
    return f'Rectangle(width={self.width}, height={self.height})'

  def set_width(self, newWidth):
    self.width = newWidth

  def set_height(self, newHeight):
    self.height = newHeight

  def get_area(self):
    return self.width * self.height

  def get_perimeter(self):
    return (self.width + self.height) * 2

  def get_diagonal(self):
    return (self.width**2 + self.height**2)**0.5

  def get_picture(self):
    if (self.width or self.height) > 50:
      return "Too big for picture."
    return ('*' * self.width + '\n') * self.height

  def get_amount_inside(self, other):
    return (self.width // other.width) * (self.height // other.height)


class Square(Rectangle):

  def __init__(self, side):
    self.width = side
    self.height = side

  def __str__(self):
    return f'Square(side={self.width})'

  def set_side(self, newSide):
    self.width = self.height = newSide

  def set_width(self, newWidth):
    self.width = self.height = newWidth

  def set_height(self, newHeight):
    self.width = self.height = newHeight
