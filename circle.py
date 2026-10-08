import math


def area(r):
    '''
    Возвращает площадь круга.
    
            Параметры:
                    r (double): радиус круга
    
            Возвращаемое значение:
                    area (double): площадь круга

            Пример:
                    >>> area(10)
                    314.1592653589793
    '''
    return math.pi * r * r


def perimeter(r):
    '''
    Возвращает периметр круга.
    
            Параметры:
                    r (double): радиус круга
    
            Возвращаемое значение:
                    perimeter (double): периметр круга

            Пример:
                    >>> perimeter(10)
                    62.83185307179586
    '''
    return 2 * math.pi * r

