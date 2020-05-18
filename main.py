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

S = [['.....',
      '......',
      '..00..',
      '.00...',
      '.....'],
     ['.....',
      '..0..',
      '..00.',
      '...0.',
      '.....']]
