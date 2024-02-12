from typing import Callable

import pygame
from game.ui.button_ui import Button
from game.settings import *
from game.ui.text_box_ui import TextBox


class MainManuUI:
    """
    Start screen of the game (Main menu)
    """

    def __init__(self, game: Callable) -> None:
        self.game = game
        self.display_surf = pygame.display.get_surface()
        self.display_surf.fill("white")

        self.intro_text = TextBox(self.display_surf,
                                  (SCREEN_WIDTH / 2 - PRE_LEVEL_TEXT_WIDTH / 2, SCREEN_HEIGHT / 2 - 100),
                                  PRE_LEVEL_TEXT_WIDTH)
        self.intro_text.text = "LETS PLAY A GAME.\nTHIS IS THE INTRO SCREEN...."

        self.btn_play = Button("Play", BTN_WIDTH, BTN_HEIGHT,
                               BUTTON_POSITION["main_play"], BTN_ELEVATION, self.game.next_state)
        self.btn_load = Button("Load", BTN_WIDTH, BTN_HEIGHT,
                               BUTTON_POSITION["main_load"], BTN_ELEVATION, self.game.player.load)
        self.btn_exit = Button("Exit", BTN_WIDTH, BTN_HEIGHT,
                               BUTTON_POSITION["main_exit"], BTN_ELEVATION, self.game.exit_game)

    def update(self) -> None:
        self.display_surf.fill("white")
        self.btn_play.draw()
        self.btn_load.draw()
        self.btn_exit.draw()
        self.intro_text.display_text()
