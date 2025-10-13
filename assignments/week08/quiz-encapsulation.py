"""
Write a Python class Rectangle with:

Private attributes for length and width
Methods to calculate area (getArea()) and perimeter getPerimeter())
A method to check if it's a square (isSquare())

"""
    
class Rectangle :
     def __init__(self,lenght,width):
          self.__lenght = lenght
          self.__width = width 

     def getArea(self):
          return f"Area = {self.__lenght * self.__width}"
     
     def getPerimeter(self):
          return f"Perimeter = {(self.__lenght + self.__width)*2}"
     
     def isSquare(self):
          if self.__width == self.__lenght :
               return f"it's a square"
          else :
               return f"Not it's a square"

rectangle = Rectangle(20,40)
print(rectangle.getArea())
print(rectangle.getPerimeter())
print(rectangle.isSquare())

