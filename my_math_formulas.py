def circle_area(r):
    pi = float(3.1415926535)
    if r <= 0:
        raise ValueError("Радиус должен быть положительным числом.")
    s = pi * r ** 2
    return s

def triangle_area(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        raise ValueError("Длины сторон треугольника должны быть положительными числами.")
    
    if a + b <= c or a + c <= b or b + c <= a:
        raise ValueError("Треугольника с такими сторонами не существует.")
    
    sides = [a, b, c]
    max_side = max(sides)
    sides.remove(max_side)
    if sides[0] ** 2 + sides[1] ** 2 == max_side **2:
        print('Введенный треугольник является прямоугольным')
        return sides[0] * sides[1] / 2
    else:
        # для 3-х сторон формула Герона, сначала посчитаем полупериметр
        p = (a + b + c) / 2
        s = (p * (p - a) * (p - b) * (p - c))  ** (1 / 2)
        return s 
    
def main():
    print(triangle_area(3,4,6))
    print(circle_area(3))
    

if __name__ == '__main__':
    main()
