import pygame
import random

pygame.font.init()

# Global variables
window_width = 800
window_height = 700

play_width = 300
play_height = 600

block_size = 30

top_left_x = (window_width - play_width) // 2
top_left_y = window_height - play_height

# The shapes
S = [
    [".....", "......", "..00..", ".00...", "....."],
    [".....", "..0..", "..00.", "...0.", "....."],
]

Z = [
    [".....", ".....", ".00..", "..00.", "....."],
    [".....", "..0..", ".00..", ".0...", "....."],
]

I = [
    ["..0..", "..0..", "..0..", "..0..", "....."],
    [".....", "0000.", ".....", ".....", "....."],
]

O = [[".....", ".....", ".00..", ".00..", "....."]]

J = [
    [".....", ".0...", ".000.", ".....", "....."],
    [".....", "..00.", "..0..", "..0..", "....."],
    [".....", ".....", ".000.", "...0.", "....."],
    [".....", "..0..", "..0..", ".00..", "....."],
]

L = [
    [".....", "...0.", ".000.", ".....", "....."],
    [".....", "..0..", "..0..", "..00.", "....."],
    [".....", ".....", ".000.", ".0...", "....."],
    [".....", ".00..", "..0..", "..0..", "....."],
]

T = [
    [".....", "..0..", ".000.", ".....", "....."],
    [".....", "..0..", "..00.", "..0..", "....."],
    [".....", ".....", ".000.", "..0..", "....."],
    [".....", "..0..", ".00..", "..0..", "....."],
]

shape_list = [S, Z, I, O, J, L, T]
color_list = [
    (255, 255, 0),
    (0, 255, 0),
    (255, 0, 0),
    (0, 255, 255),
    (255, 165, 0),
    (128, 0, 128)(0, 0, 255),
]


class Shape(object):
    """
    """

    # y axis
    rows = 20

    # x axis
    columns = 10

    def __init__(self, column, row, shape):
        self.x = column
        self.y = row
        self.shape = shape
        self.columns = color_list[shape_list.index(shape)]
        self.rotation = 0


def create_grid(locked_positions={}):
    """
    Creates the grid using a tuple to represent the colors using
    a dictionary to show which positions are already taken

    :param locked_positions: dictionary of the positions that are
                             currently filled

    :return: a 2D list of tuples as RGB values
    """

    # make a grid of colors a size of 10 by 20
    grid = [[(0, 0, 0) for x in range(10)] for y in range(20)]

    # iterate through the whole grid
    for i in range(len(grid)):
        for j in range(len(grid[0])):

            # changes the color if the position is already taken
            if (j, i) in locked_positions:

                c = locked_positions[(j, i)]
                grid[i][j] = c

    return grid


def convert_shape_format(shape):
    pass


def check_valid_space(shape, grid):
    pass


def check_lost(positions):
    pass


def get_shape():
    pass


def draw_text_middle(text, size, color, area):
    pass


def draw_grid(area, row, column):
    pass


def clear_rows(grid, locked):
    pass


def draw_next_shape(shape, area):
    pass


def draw_window(area):
    pass


def main():
    pass


def main_menu():
    pass


main_menu()
