from typing import Tuple
import os.path
import random

import pygame


class Button:
    """
    Button class that handles the button behaviour

    @todo - make it so that on click handles more then one function
    """

    def __init__(self, text, width, height, pos, elevation, func=None) -> None:
        self.display = pygame.display.get_surface()

        self.on_click = func
        self.pressed = False
        self.elevation = elevation
        self.dynamic_elevation = elevation
        self.original_y_pos = pos[1]

        btn_clicks = [os.path.join("game", "Music", "button_click_1.wav"),
                      os.path.join("game", "Music", "button_click_2.wav")]
        self.btn_click = pygame.mixer.Sound(random.choice(btn_clicks))
        self.btn_click.set_volume(0.9)

        # top rect
        self.top_rect = pygame.Rect(pos, (width, height))
        self.top_color = "#f6edd4"

        # bottom rect
        self.bottom_rect = pygame.Rect(pos, (width, elevation))
        self.bottom_color = "#beb7a3"

        # text
        self.font = pygame.font.SysFont("Times New Roman", 30)
        self.text_surf = self.font.render(text, True, "black")
        self.text_rect = self.text_surf.get_rect(center=self.top_rect.center)

    def move(self, new_position: Tuple[int, int]) -> None:
        """
        When the object that this button is in, call this method that moves the button along with the object

        @param new_position:
        @return:
        """
        self.top_rect.topleft = new_position
        self.original_y_pos = new_position[1]

    def draw(self) -> None:
        """
        Draws the button background image text and other

        @return:
        """

        # elevation logic
        self.top_rect.y = self.original_y_pos - self.dynamic_elevation
        self.text_rect.center = self.top_rect.center

        self.bottom_rect.midtop = self.top_rect.midtop
        self.bottom_rect.height = self.top_rect.height + self.dynamic_elevation

        pygame.draw.rect(self.display, self.bottom_color, self.bottom_rect, border_radius=12)

        pygame.draw.rect(self.display, self.top_color, self.top_rect, border_radius=12)
        self.display.blit(self.text_surf, self.text_rect)

        self.check_click()

    def check_click(self) -> None:
        """
        When user clicks on the Button

        @return:
        """
        mouse_pos = pygame.mouse.get_pos()
        # print(mouse_pos)

        if self.top_rect.collidepoint(mouse_pos):
            self.top_color = "#D74B4B"
            if pygame.mouse.get_pressed()[0]:
                self.dynamic_elevation = 0
                self.pressed = True
            else:
                if self.pressed:
                    # print("click")
                    if self.on_click:
                        self.btn_click.play()
                        self.on_click()

                    self.pressed = False
                self.dynamic_elevation = self.elevation
        else:
            self.dynamic_elevation = self.elevation
            self.top_color = "#f6edd4"
