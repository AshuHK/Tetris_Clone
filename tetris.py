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
        self.color = color_list[shape_list.index(shape)]
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
            if column == "0":
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

    allowed_positions = [
        [(j, i) for j in range(10) if grid[i][j] == (0, 0, 0)] for i in range(20)
    ]

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

    font = pygame.font.SysFont("comicsans", size, bold=True)
    label = font.render(text, 1, color)

    area.blit(
        label,
        (
            top_left_x + play_width / 2 - (label.get_width() / 2),
            top_left_y + play_height / 2 - label.get_height() / 2,
        ),
    )


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
    Clears a row when it gets filled

    :param grid: 2D list of all of the positions on the grid
    :param locked: dictionary of all of the positions that are currently taken
                   on the board
    """
    count1 = 0

    for i in range(len(grid) - 1, -1, -1):
        row = grid[i]

        if (0, 0, 0) not in row:
            count1 += 1
            count2 = i

            for j in range(len(row)):
                try:
                    del locked[(j, i)]
                except:
                    continue

    if count1 > 0:
        for key in sorted(list(locked), key=lambda x: x[1])[::-1]:
            x, y = key
            if x < count2:
                new_key = (x, y + count1)
                locked[new_key] = locked.pop(key)

    return count1


def draw_next_shape(shape, area):
    """
    Draw the next shape on the side of the screen

    :param shape: Shape object that is set to be your next shape
    :param area: Surface object where you draw on the window
    """

    font = pygame.font.SysFont("comicsans", 30)
    label = font.render("Next Shape", 1, (255, 255, 255))

    box_x = top_left_x + play_width + 50
    box_y = top_left_y + play_height / 2 - 100

    shape_format = shape.shape[shape.rotation % len(shape.shape)]

    for i, line in enumerate(shape_format):
        row = list(line)
        for j, column in enumerate(row):
            if column == "0":
                pygame.draw.rect(
                    area, shape.color, (box_x + j * 30, box_y + i * 30, 30, 30), 0
                )

    area.blit(label, (box_x + 10, box_y - 30))


def draw_window(area, grid, score=0, last_score=0):
    """
    Draws the whole window onto a specific area (in this case it is the whole
    window)

    :param area: surface to draw the window on
    """

    area.fill((0, 0, 0))

    pygame.font.init()
    font = pygame.font.SysFont("comicsans", 60)
    label = font.render("Tetris", 1, (255, 255, 255))

    area.blit(label, (top_left_x + play_width / 2 - (label.get_width() / 2), 30))

    font = pygame.font.SysFont("comicsans", 30)
    label = font.render("Score: {}".format(score), 1, (255, 255, 255))

    box_x = top_left_x + play_width + 50
    box_y = top_left_y + play_height / 2 - 100

    area.blit(label, (box_x + 20, box_y + 160))

    label = font.render("High Score: {}".format(last_score), 1, (255, 255, 255))

    box_x = top_left_x - 200
    box_y = top_left_y + 200

    area.blit(label, (box_x + 20, box_y + 160))

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            pygame.draw.rect(
                area,
                grid[i][j],
                (
                    top_left_x + j * block_size,
                    top_left_y + i * block_size,
                    block_size,
                    block_size,
                ),
                0,
            )

    pygame.draw.rect(
        area, (255, 0, 0), (top_left_x, top_left_y, play_width, play_height), 5
    )

    draw_grid(area, 20, 10)


def update_score(new_score):
    """
    Updates the high score in the scores.txt file 

    :param new_score: Integer of the new score to be updated in scores.txt 
    """
    with open("scores.txt", "w") as file_ptr:
        if int(score) > new_score:
            file_ptr.write(str(score))
        else:
            file_ptr.write(str(new_score))


def max_score():
    """
    Get the highest score 

    :return: String for the height score in the file 
    """
    with open("scores.txt", "r") as file_ptr:
        lines = file_ptr.readlines()
        score = lines[0].strip()

    return score


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
    fall_speed = 0.27
    level_time = 0
    score = 0
    last_score = max_score()

    # run the this main loop when the game is still running
    while is_playing:

        # set a fall speed and have it increase over time
        grid = create_grid(locked_positions)
        fall_time += clock.get_rawtime()
        level_time += clock.get_rawtime()
        clock.tick()
        if level_time / 1000 > 5:
            level_time = 0
            if level_time > 0.12:
                level_time -= 0.005

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

        shape_pos = convert_shape_format(current_shape)

        # set the position in the grid that specific color of the piece
        for i in range(len(shape_pos)):
            x, y = shape_pos[i]
            if y > -1:
                grid[y][x] = current_shape.color

        # when the shape hits the bottom of the grid
        if change_shape:
            for pos in shape_pos:
                p = (pos[0], pos[1])
                locked_positions[p] = current_shape.color
            current_shape = next_shape
            next_shape = get_shape()
            change_shape = False
            clear_rows(grid, locked_positions)
            score += clear_rows(grid, locked_positions) * 10

        # update the window
        draw_window(window, grid, score, last_score)

        # draws the next shape into its own area on the right side of the screen
        draw_next_shape(next_shape, window)
        pygame.display.update()

        # quit execution when you lose
        if check_lost(locked_positions):
            draw_text_middle("You Lose :(", 80, (255,255,255))
            pygame.display.update()
            pygame.time.delay(1500)
            is_playing = False
            update_score(score)


def main_menu():
    """
    """

    pass



window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Tetris")

main_menu()
