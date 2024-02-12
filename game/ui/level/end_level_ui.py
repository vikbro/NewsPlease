from typing import Callable

import pygame

from game.settings import *
from game.ui.text_box_ui import TextBox
from game.ui.button_ui import Button
import os.path


class EndLevelUI:
    """
    Class that shows info to the player at the end of a level.

    """

    def __init__(self, game: Callable, level_ui: Callable) -> None:
        self.game = game
        self.level_ui = level_ui
        self.level = level_ui.level
        self.display_surf = pygame.display.get_surface()
        self.activated = True

        # Sound
        self.print_sound = pygame.mixer.Sound(os.path.join("game", "Music", "print.wav"))
        # bg_music.set_volume(0.1)
        x = self.display_surf.get_rect().center[0]
        y = self.display_surf.get_rect().center[1]

        self.condition = TextBox(self.display_surf,
                                 (x - PRE_LEVEL_TEXT_WIDTH / 2, y),
                                 PRE_LEVEL_TEXT_WIDTH)
        # self.condition.text = "You are done. Fired. Do not show your face at the news paper again."
        self.condition.text = "Ending level"
        self.btn_continue = Button("Continue", BTN_WIDTH, BTN_HEIGHT, BUTTON_POSITION["pre continue"], BTN_ELEVATION,
                                   self.game.next_state)

    def end_level(self) -> None:
        """
        Run the end day method in the level classes
        @return:
        """
        self.print_sound.stop()
        self.level_ui.end_day()

    def update(self):
        """
        Updates the End level ui
        @return:
        """
        if self.activated is True:
            self.print_sound.play()
            self.activated = False

        # Pottentialy unneded updateing of the display since there is nothing to be changed
        self.display_surf.fill((255, 255, 255))
        self.condition.display_text()
        self.btn_continue.draw()
