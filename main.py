"""
1. Choose random point within equilateral triangle
2. Choose a random vertice and draw a point between it and the previous point
"""
import math
import random
import matplotlib.pyplot as plt
import numpy as np


def round_down(number: float, decimals: int = 2):
    """
    Returns a value rounded down to a specific number of decimal places.
    """
    if not isinstance(decimals, int):
        raise TypeError("decimal places must be an integer")
    elif decimals < 0:
        raise ValueError("decimal places has to be 0 or more")
    elif decimals == 0:
        return math.floor(number)

    factor = 10 ** decimals
    return math.floor(number * factor) / factor


class SierpinskiTriangle:
    def __init__(self, size, number_of_points):
        self.size = size
        self.number_of_points = number_of_points

    def calculate_vertices(self):
        x1, y1 = 0, 0
        x2, y2 = self.size, 0
        x3, y3 = self.size / 2, round((self.size * 3 ** (1 / 2)) / 2, 2)

        return [(x1, y1), (x2, y2), (x3, y3)]

    def calculate_first_point(self):
        x0 = random.randrange(self.size)
        x_temp = x0  # used for calculations of y regardless of the side on which original x0 is

        if x0 > self.size / 2:
            x_temp = self.size - x0

        y0 = round_down((x_temp * 3 ** (1 / 2)) / 2)

        first_point = (x0, y0)

        return first_point

    def calculate_points_within_triangle(self):
        first_point = self.calculate_first_point()
        vertices = self.calculate_vertices()
        all_points = vertices + [first_point]
        prev_point = first_point
        for _ in range(1, self.number_of_points):
            vertice = random.choice(vertices)

            x_new = round_down((prev_point[0] + vertice[0]) / 2)
            y_new = round_down((prev_point[1] + vertice[1]) / 2)

            new_point = [x_new, y_new]
            all_points.append(new_point)
            prev_point = new_point

        return all_points

    def plot(self):
        points_coordinates = np.array(self.calculate_points_within_triangle())
        x_axis = points_coordinates[:, 0]
        y_axis = points_coordinates[:, 1]
        plt.scatter(x_axis, y_axis)
        plt.show()


if __name__ == "__main__":
    size_of_triangle = int(input("Enter the length of the arm in the triangle: "))
    number_of_points_in_triangle = int(input("Enter the number of points in the triangle: "))

    if size_of_triangle < 1 or number_of_points_in_triangle < 1:
        raise ValueError("\nYou can't build such a triangle")

    sierp_t = SierpinskiTriangle(size=size_of_triangle, number_of_points=number_of_points_in_triangle)
    sierp_t.plot()
