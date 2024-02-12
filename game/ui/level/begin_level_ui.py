import pygame
from game.settings import *
from game.ui.text_box_ui import TextBox
from game.ui.button_ui import Button
# from game.dayTree import *


class BeginLevelUI:
    """
    Class that renders the beginning screen of a level in order to show the tasks to the user and potential other info
    """

    def __init__(self, game, level) -> None:
        self.btn_continue = None
        self.game = game
        self.level = level
        self.display_surf = pygame.display.get_surface()
        self.activated = True

        x = self.display_surf.get_rect().center[0]
        y = self.display_surf.get_rect().center[1]

        self.condition = TextBox(self.display_surf,
                                 (x - PRE_LEVEL_TEXT_WIDTH / 2, y),
                                 PRE_LEVEL_TEXT_WIDTH)
        # self.condition.text = "You are done. Fired. Do not show your face at the news paper again."
        self.condition.text = self.level.current_day.condition_text
        self.configure_btn()

    def configure_btn(self):
        # print("CONFIGURE " + self.level.current_day.day_name)
        if "END" in self.level.current_day.day_name:
            self.btn_continue = Button("Return menu", BTN_WIDTH, BTN_HEIGHT, BUTTON_POSITION["pre continue"],
                                       BTN_ELEVATION,
                                       self.game.return_menu)
            # print("ENDING")
            # Resets the players values and returns to Day 1 when an end has been encountered
            self.game.player.reset_values()
            # Reset the day to D1 , but i dont think this logic should be in this method
        else:
            self.btn_continue = Button("Continue", BTN_WIDTH, BTN_HEIGHT, BUTTON_POSITION["pre continue"],
                                       BTN_ELEVATION,
                                       self.game.next_state)

    def update(self):
        if self.activated:
            self.configure_btn()
            self.activated = False

        self.display_surf.fill((255, 255, 255))
        self.condition.text = self.level.current_day.condition_text
        self.condition.display_text()
        self.btn_continue.draw()
