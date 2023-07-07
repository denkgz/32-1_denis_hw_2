class Figure:
    unit = 'cm'

    def __init__(self):
        self.__perimeter = 0

    @property
    def perimeter(self):
        return self.__perimeter

    @perimeter.setter
    def perimeter(self,value):
        self.__perimeter = value


    def calculate_area(self):
        pass

    def calculate_perimeter(self):
        pass

    def info(self):
        pass

class Square(Figure):
    def __init__(self, side_length):
        super().__init__()
        self.__side_length = side_length
        self.__perimeter = self.calculate_perimeter()

    def calculate_area(self):
        return self.__side_length ** 2

    def calculate_perimeter(self):
        return self.__side_length * 4

    def info(self):
        print(f'''SQUARE SIDE LENGTH: {self.__side_length}{self.unit}
PERIMETER: {self.__perimeter}{self.unit}, AREA: {self.calculate_area()}{self.unit}''')

class Rectangle(Figure):
    def __init__(self,length,width):
        super().__init__()
        self.__length = length
        self.__width = width
        self.__perimeter = self.calculate_perimeter()

    def calculate_area(self):
        return self.__length * self.__width

    def calculate_perimeter(self):
        return 2 * (self.__length + self.__width)

    def info(self):
        print(f'''RECTANGLE LENGTH: {self.__length}{self.unit},
WIDTH: {self.__width}{self.unit}
PERIMETER: {self.__perimeter}{self.unit}, AREA: {self.calculate_area()}{self.unit}''')


#Квадраты
square1 = Square(5)
square2 = Square(8)

#Прямоугольники
rectangle1 = Rectangle(5,3)
rectangle2 = Rectangle(6,4)
rectangle3 = Rectangle(10,6)

figure_list = [square1,square2,rectangle1,rectangle2,rectangle3]

for figure in figure_list:
    figure.info()
    print('--------------------')





