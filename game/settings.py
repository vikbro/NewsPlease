from pygame.math import Vector2
# print("HEllo")
# screen
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
TILE_SIZE = 64

# Button settings
BTN_WIDTH = 150
BTN_HEIGHT = 30
BTN_ELEVATION = 3

# Grid position
GRID_CELL_SIZE = 75
GRID_POS_X = SCREEN_WIDTH - SCREEN_WIDTH/4 - GRID_CELL_SIZE
GRID_POS_Y = 100

OVERLAY_TILE_SIZE = 40
# clock position
CLOCK_POSITION = (100, 15)

# Evelope positions
# small envelope
ENV_S_WIDTH = 30
ENV_S_HEIGHT = 40
# large enelope
ENV_L_WIDTH = 250
ENV_L_HEIGHT = 150

DEC_L_WIDTH = 150
DEC_L_HEIGHT = 250
# ENV_BTN_S_POS = ()
# ENV_BTN_M_POS = ()
# ENV_BTN_L_POS = ()
DEC_BTN_WIDTH = 100
DEC_BTN_HEIGHT = 50

ENV_BTN_WIDTH = 50
ENV_BTN_HEIGHT = 50
ENV_W_PADDING = (ENV_L_WIDTH - 3*ENV_BTN_WIDTH)/4

# overlay positions
OVERLAY_POSITIONS = {
    'loyalty': (100, SCREEN_HEIGHT - 15),
    'money': (200, SCREEN_HEIGHT - 15),
    'readership': (300, SCREEN_HEIGHT - 15)}

# button position
BUTTON_POSITION = {
    "menu": (15, 30),
    "save": (15, 90),
    "pause": (15, 150),
    "continue": (SCREEN_WIDTH / 2 - BTN_WIDTH / 2, SCREEN_HEIGHT / 2 + 50),
    "pre continue": (SCREEN_WIDTH / 2 - BTN_WIDTH / 2, SCREEN_HEIGHT - 100),
    "main_play": (15, 30),
    "main_load": (15, 90),
    "main_exit": (15, 150),
}

PRE_LEVEL_TEXT_WIDTH = 700
