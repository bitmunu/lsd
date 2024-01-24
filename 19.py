import math
from scipy.spatial import distance
import matplotlib.pyplot as plt
from itertools import combinations
import random

class Line:
    def __init__(self, k, b):
        self.k = k
        self.b = b

    def intersection_with_other_line(self, other):
        k1, b1 = self.k, self.b
        k2, b2 = other.k, other.b

        if k1 == k2:
            return None  # Прямые параллельны

        x = (b2 - b1) / (k1 - k2)
        y = k1*x + b1

        return (x, y)

    def intersection_with_segment(self, Segment):
        x1, y1, x2, y2 = Segment.x1, Segment.y1, Segment.x2, Segment.y2  #концы отрезка

        if x1 == x2:
            x = x1
            y = self.k* x + self.b
            if min(y1, y2) <= y <= max(y1, y2):
                return (x, y)
            else:
                return None

        if self.k == Segment.kline:
            return None

        xIntersect = (Segment.bline - self.b) / (self.k - Segment.kline)
        yIntersect = self.k*xIntersect + self.b

        # Проверяем, лежит ли точка пересечения в пределах отрезка
        if min(x1, x2) <= xIntersect <= max(x1, x2) and min(y1, y2) <= yIntersect <= max(y1, y2):
            return (xIntersect, yIntersect)
        else:
            return None

class Segment:
    def __init__(self, x1, x2, y1, y2):
        if x1 !=x2:
            self.x1 = x1
            self.x2 = x2
            self.y1 = y1
            self.y2 = y2
            self.kline = (y2 - y1) / (x2 - x1)
            self.bline = y1 - self.kline * x1
        else:
            self.kline = y2 - y1
            self.x1 = x1
            self.x2 = x2
            self.y1 = y1
            self.y2 = y2
            self.bline = 0

    def __module(self):
        return math.sqrt((self.x1-self.x2)**2 + (self.y1-self.y2)**2)

    def intersection_with_other_segment(self, other):

        if self.kline == other.kline:
            return (-17, -17)# Прямые параллельны

        # Вычисление точки пересечения
        xIntersect = (other.bline - self.bline) / (self.kline - other.kline)
        yIntersect = xIntersect * self.kline + self.bline

        # Проверка, находится ли точка пересечения в пределах обоих отрезков
        if (min(self.x1, self.x2) <= xIntersect <= max(self.x1, self.x2)
                and
                min(self.y1, self.y2) <= yIntersect <= max(self.y1, self.y2)
                and
                min(other.x1, other.x2) <= xIntersect <= max(other.x1, other.x2)
                and
                min(other.y1, other.y2) <= yIntersect <= max(other.y1, other.y2)):
            return (xIntersect, yIntersect)
        else:
            return None


class Circle:
    def __init__(self, center_x, center_y, radius):
        self.cx = center_x
        self.cy = center_y
        self.rad = radius

    def intersection_with_line(self, Line):
        k, b = Line.k, Line.b # коэффициенты уравнения прямой
        x0, y0, r = self.cx, self.cy, self.rad  # центр и радиус окружности

        #коэффиценты квадратного уравнения для х
        A = 1 + k**2
        B = -2*x0 + 2*k*b - 2*k*y0
        C = x0**2 + b**2 - 2*b*y0 + y0**2 - r**2

        discriminant = B**2 - 4*A*C
        if discriminant < 0:
            return []  # нет реальных корней, пересечений нет

        x1 = (-B + math.sqrt(discriminant)) / (2*A)
        x2 = (-B - math.sqrt(discriminant)) / (2*A)
        y1 = k*x1 + b
        y2 = k*x2 + b

        if discriminant > 0:
            return [(x1, y1), (x2, y2)]
        else:
            return [(x1, y1)]

    def intersection_with_segment(self, Segment):
        x1, y1, x2, y2 = Segment.x1, Segment.y1, Segment.x2, Segment.y2
        x0, y0, r = self.cx, self.cy, self.rad # центр и радиус окружности

        #уравнение прямой
        if x2 != x1:
            p1 = (y2 - y1)
            p2 = (x2 - x1)
            line = Line(p1/p2, y1 - (p1/p2)*x1)
        else:
            # Отрезок вертикален
            line = None

        #точки пересечения прямой и окружности
        if line is not None:
            intersections = self.intersection_with_line(line)
        else:
            A = 1
            B = -2 * y0
            C = y0**2 - r**2 + (x1 - x0)**2
            discriminant = B**2 - 4*A*C

            if discriminant < 0:
                return []  # нет действительных корней, пересечений нет
            y1 = (-B + math.sqrt(discriminant)) / (2*A)
            y2 = (-B - math.sqrt(discriminant)) / (2*A)
            intersections = [(x1, y1), (x1, y2)] if discriminant > 0 else [(x1, y1)]

        return [(x, y) for x, y in intersections if min(x1, x2) <= x <= max(x1, x2) and min(y1, y2) <= y <= max(y1, y2)]

    def is_point_inside_circle(self, x, y):
        return ((x - self.cx) ** 2 + (y - self.cy) ** 2) < self.rad ** 2

    def is_valid(self, triangle1, triangle2):

        for point in triangle1:
            if not self.is_point_inside_circle(point[0], point[1]):
                print("точка треугольника выходит за пределы окружности")
                return False

        for point in triangle2:
            if not self.is_point_inside_circle(point[0], point[1]):
                print("точка треугольника выходит за пределы окружности")
                return False

        omegaCount = 0
        for i in range(3):
            segment1 = Segment(triangle1[i][0], triangle1[(i + 1) % 3][0], triangle1[i][1], triangle1[(i + 1) % 3][1])
            count = 0
            for j in range(3):
                segment2 = Segment(triangle2[j][0], triangle2[(j + 1) % 3][0], triangle2[j][1], triangle2[(j + 1) % 3][1])
                if segment1.intersection_with_other_segment(segment2) is not None or segment1.intersection_with_other_segment(segment2) == (-17, -17):
                    print("Треугольники пересекаются")
                    return False
                if triangle2[j][0] * segment1.kline + segment1.bline < 0:
                    count-=1
                elif triangle2[j][0] * segment1.kline + segment1.bline > 0:
                    count+=1
            if count == 3 or count == -3:
                omegaCount+=1

        if omegaCount == 3:
            return False
        print("готово")
        return True

def find_triangles(points):
    valid_triangles = []

    for combination in combinations(points, 3):
        if is_valid_triangle(combination):
            valid_triangles.append(combination)
    return valid_triangles


def is_valid_triangle(points):
    (x1, y1), (x2, y2), (x3, y3) = points

    #площадь треугольника
    area = 0.5 * abs(x1*(y2 - y3) + x2*(y3 - y1) + x3*(y1 - y2))

    # не равна ли площадь нулю
    return area > 1e-6  # погрешность


def generate_random_points(num_points, x_range, y_range):
    return [(random.randint(x_range[0], x_range[1]), random.randint(y_range[0], y_range[1])) for _ in range(num_points)]


def circumcircle(triangle):
    (x1, y1), (x2, y2), (x3, y3) = triangle

    #середины сторон треугольника
    mid1 = ((x1 + x2) / 2, (y1 + y2) / 2)
    mid2 = ((x1 + x3) / 2, (y1 + y3) / 2)

    #угол наклона перпендикуляров к сторонам треугольника
    if y2 != y1:
        k1 = -(x2 - x1) / (y2 - y1)
        b1 = mid1[1] - k1 * mid1[0]
        line1 = Line(k1, b1)
    else:
        line1 = None

    if y3 != y1:
        k2 = -(x3 - x1) / (y3 - y1)
        b2 = mid2[1] - k2 * mid2[0]
        line2 = Line(k2, b2)
    else:
        line2 = None

    #точка пересечения серединных перпендикуляров - центр описанной окружности
    if line1 and line2:
        center = line1.intersection_with_other_line(line2)
    elif line1 is None:
        center = (mid1[0], k2 * mid1[0] + b2)
    elif line2 is None:
        center = (mid2[0], k1 * mid2[0] + b1)

    #радиус - расстояние от центра до любой вершины треугольника
    radius = distance(center, (x1, y1))

    return center[0], center[1], radius

def find_bigger_circle(triangle1, triangle2, center):
    max_distance = 0
    for point in triangle1:
        for point2 in triangle2:
            dist = distance(point, point2)
            if dist > max_distance:
                max_distance = dist
    circle_radius = max_distance*2
    print(f"Large Circle: Center={center}, Radius={circle_radius}")
    return (max_distance + radius) / 2

def distance(point1, point2):
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

def draw_system(triangle1, triangle2, center_x, center_y, rad):
    fig, ax = plt.subplots(figsize=(10, 10))

    #рисуем треугольник
    triangle1_x = [point[0] for point in triangle1] + [triangle1[0][0]]
    triangle1_y = [point[1] for point in triangle1] + [triangle1[0][1]]
    ax.plot(triangle1_x, triangle1_y, label='Треугольник', color='blue')

    triangle2_x = [point[0] for point in triangle2] + [triangle2[0][0]]
    triangle2_y = [point[1] for point in triangle2] + [triangle2[0][1]]
    ax.plot(triangle2_x, triangle2_y, label='Треугольник', color='black')

    #рисуем окружность
    circle_center, circle_radius = (center_x, center_y), rad
    circle_plot = plt.Circle(circle_center, circle_radius, color='green', fill=False, label='Большая окружность')
    ax.add_artist(circle_plot)

    ax.set_aspect(aspect=1, adjustable='datalim')
    ax.legend()
    plt.show()


random_points = generate_random_points(100, (-10, 10), (-10, 10))

triangles = find_triangles(random_points) #одбор треугольников

#Перебор найденных треугольников
for triangle1 in triangles:
    flag = False
    center_x, center_y, radius = circumcircle(triangle1)
    circle = Circle(center_x, center_y, radius)

    for triangle2 in triangles:
        #distt = find_bigger_circle(triangle1, triangle2, (center_x, center_y))
       # circle.rad = distt
        if circle.is_valid(triangle1, triangle2) is True:
            draw_system(triangle1, triangle2, circle.cx, circle.cy, circle.rad)
            flag = True
            break
    if flag is True:
        break
else:
    print("конфигурация не найдена")