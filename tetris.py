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

# randomize the colors of the shapes
random.shuffle(color_list)


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
    Convert the given shape into a format that can be easily put into a list 
    
    :param shape: Shape object to be converted 
    
    :return: List of tuples of (x, y) coordinates 
    """

    positions = [] 
    format = shape.shape[shape.rotation % len(shape.shape)]

    for i, line in enumerate(format): 
        row = list(line) 
        for j, column in enumerate(row): 
            if column == \"0\": 
                positions.append((shape.x + j, shape.y + i))

    for i, pos in enumerate(positions): 
        positions[i] = (pos[0] - 2, pos[1] - 4) 

    return positions



def check_valid_space(shape, grid):
    """
    Returns a boolean if the given positions for the shapes is allowed

    :param shape: Shape object to be checked for a valid position 
    :param grid: 2D list to represent the grid in the game 

    :return: Boolean for if the space is allowed for the shape 
    """

    allowed_positions = [[(j, i) for j in range(10) if grid[i][j] == (0,0,0)] for i in range(20)]

    allowed_positions = [j for sub in allowed_positions for j in sub]

    formatted_shape = convert_shape_format(shape)

    for pos in formatted_shape: 
        if pos not in allowed_positions: 
            if pos[1] > -1: 
                return False

    return True


def check_lost(positions):
    """
    Check the positions of all of the shapes and determines if the game is over 

    :param positions: 2D list of tuples of (x, y) coordinates 
    
    :return: Boolean stating if the game is over 
    """

    # iterate through each shapes position 
    for pos in positions: 
        x, y = pos

        # if a shape is at the top, then the game is over 
        if y < 1: 
            return True 
    
    return False 


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
    Draws the grid lines on the playing grid 

    :param area: Surface to draw on the window 
    :param row: Integer for the number of rows in the grid 
    :param column: Integer for the number of columns in the grid 
    """
    grid_x = top_left_x
    grid_y = top_left_y

    for i in range(row):

        # draw the horizontal liens
        pygame.draw.line(
            area,
            (128, 128, 128),
            (grid_x, grid_y + i * 30),
            (grid_x + play_width, grid_y + i * 30),
        )

        for j in range(column):

            # draw the vertical lines
            pygame.draw.line(
                area,
                (128, 128, 128),
                (grid_x + j * 30, grid_y),
                (grid_x + j * 30, grid_y + play_height),
            )


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
    Draws the whole window onto a specific area (in this case it is the whole
    window)

    :param area: surface to draw the window on
    """

    area.fill((0, 0, 0))

    font = pygame.font.SysFont("comicsans", 60)
    label = font.render("Tetris", 1, (255, 255, 255))

    area.blit(label, (top_left_x + play_width / 2 - (label.get_width() / 2), 30))

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            pygame.draw.rect(
                area, grid[i][j], (top_left_x + j * 30, top_left_y + i * 30, 30, 30), 0
            )

    # draw the grid and border
    draw_grid(area, 20, 10)
    pygame.draw.rect(
        area, (255, 255, 5), (top_left_x, top_left_y, play_width, play_height), 5
    )

    pygame.display.update()


def main():
    """
    Main function for the game
    """

    global grid

    # create the grid based on the positions that are currently taken
    locked_positions = {}
    grid = create_grid(locked_positions)

    # booleans for running the game
    change_shape = False
    is_playing = True

    # get the first two shapes
    current_shape = get_shape()
    next_shape = get_shape()

    # run an internal timer for the score
    clock = pygame.time.Clock()

    # represents how long it takes for a shape to fall down
    fall_time = 0

    # run the this main loop when the game is still running
    while is_playing:
        
        fall_speed = .27

        grid = create_grid(locked_positions) 
        fall_time += clock.get_rawtime()
        clock.tick()

        # adding falling of the shapes 
        if (fall_time / 1000) >= fall_speed: 
            fall_time = 0 
            current_shape.y += 1 
            if not check_valid_space(current_shape, grid) and (current_shape.y > 0): 
                current_shape.y -= 1 
                change_shape = True

        for event in pygame.event.get():

            # quit sequence
            if event.type == pygame.QUIT:
                run = False
                pygame.display.quit()
                quit()

            # if one of the following pieces are being pressed
            if event.type == pygame.KEYDOWN:

                # move the shape to the left
                if event.key == pygame.K_LEFT:
                    current_shape.x -= 1

                    if not check_valid_space(current_shape, grid):
                        current_shape.x += 1

                # move the shape to the right
                elif event.key == pygame.K_RIGHT:
                    current_shape.x += 1
                    if not check_valid_space(current_shape, grid):
                        current_shape.x -= 1

                # rotate the shape clockwise
                elif event.key == pygame.K_UP:
                    current_shape.rotation = current_shape.rotation + 1 % len(
                        current_shape.shape
                    )

                    if not check_valid_space(current_shape, grid):
                        current_shape.rotation = current_shape.rotation - 1 % len(
                            current_shape.shape
                        )

                # move the piece down (overrides the current fall rate)
                if event.key == pygame.K_DOWN:
                    current_shape.y += 1

                    if not check_valid_space(current_shape, grid):
                        current_shape.y -= 1

        # update the window
        draw_window(window)


def main_menu():
    """
    """

    pass


# main_menu()

window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Tetris")

main()
