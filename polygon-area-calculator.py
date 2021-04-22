class Rectangle:

  def __init__(self,width,height):
    self.width = width
    self.height = height

  def __str__(self):
    text = "Rectangle(width="+str(self.width)+", height="+str(self.height)+")"
    return text

  def set_width(self, num):
    self.width = num

  def set_height(self, num):
    self.height = num

  def get_area(self):
    area = self.width*self.height
    return area

  def get_perimeter(self):
    perimeter = 2*self.width+ 2*self.height
    return perimeter

  def get_diagonal(self):
    diagonal = (self.width ** 2 + self.height ** 2) ** .5
    return diagonal

  def get_picture(self):
    picture = []
    if self.width >50 or self.height>50:
      return "Too big for picture."
    else:
        for i in range(int(self.height)):
          picture.append("*"*(int(self.width)))
          picture.append("\n")
    return "".join(picture)

  def get_amount_inside(self, other):
    return int(self.get_area() / other.get_area())



class Square(Rectangle):

  def __init__(self,side):
    Rectangle.width = side
    Rectangle.height = side

  def set_side(self,num):
    Rectangle.set_width(self,num)
    Rectangle.set_height(self,num)

  def __str__(self):
    text ="Square(side="+str(self.width)+")"
    return text
