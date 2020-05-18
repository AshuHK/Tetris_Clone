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
    (255, 0, 0),
    (255, 255, 0),
    (0, 255, 0),
    (255, 165, 0),
    (0, 255, 255),
    (0, 0, 255),
    (128, 0, 128),
]


class Shape(object):
    """
    Class representing the shapes on the grid
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
    """
    """

    pass


def check_valid_space(shape, grid):
    """
    """

    pass


def check_lost(positions):
    """
    """

    pass


def get_shape():
    """
    Returns a randomly selected shape 

    :return: A randomly selected shape from the 
    """

    # using the global variables 
    global shape_list, color_list

    # select a random index in the shape list 
    random_shape = shape_list[random.randint(0, len(shape_list) - 1)]

    # return that shape 
    return Shape(5, 0, random_shape)


def draw_text_middle(text, size, color, area):
    """
    """

    pass


def draw_grid(area, row, column):
    """
    """
    area.fill((0,0,0))

    # font = pygame.font.SysFont(\"comicsans\", 60) 
    font = pygame.font.SysFont("comicsans", 60)
    label = font.render("Tetris", 1, (255,255,255))

    area.blit(label, (top_left_x + play_width / 2 - (label.get_width() / 2), 30))

    for i in range(len(grid)): 
        for j in range(len(grid[0])): 
            pygame.draw.rect(area, grid[i][j], (top_left_x + j * 30, top_left_y + 1 * 30, 30, 30), 0) 
    
    draw_grid(area, 20, 10) 

    pygame.draw.rect(area, (255,0,0), (top_left_x, top_left_y, play_width, play_height), 5) 
    
    pygame.display.update()


def clear_rows(grid, locked):
    """
    """

    pass


def draw_next_shape(shape, area):
    """
    """

    pass


def draw_window(area):
    """
    """

    pass


def main():
    """
    """

    global grid 

    locked_positions = {} 
    grid = create_grid(locked_positions)

    change_piece = False 
    is_playing = True 
    
    current_shape = get_shape()
    next_shape = get_shape()

    clock = pygame.time.Clock()

    fall_time = 0 

    while is_playing: 
        
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                run = False 
                pygame.display.quit()
                quit() 
        
            if event.type == pygame.KEYDOWN: 
                if event.key == pygame.K_LEFT: 
                    current_shape.x -= 1 

                    if not check_valid_space(current_shape, grid): 
                        current_shape.x += 1 

                elif event.key == pygame.K_RIGHT: 
                    current_shape.x += 1 
                    if not check_valid_space(current_shape, grid): 
                        current_shape.x -= 1 
                
                elif event.key == pygame.K_UP: 
                    current_shape.rotation = current_shape.rotation + 1 % len(current_shape.shape) 

                    if not check_valid_space(current_shape, grid): 
                        current_shape.rotation = current_shape.rotation - 1 % len(current_shape.shape) 
                
                if event.key == pygame.K_DOWN: 
                    current_shape.y += 1 

                    if not check_valid_space(current_shape, grid): 
                        current_shape.y -= 1
        draw_window(window)


def main_menu():
    """
    """

    pass


# main_menu()

window = pygame.display.set_mode((window_width, window_height)) 
pygame.display.set_caption("Tetris")

main()
