from typing import Tuple

import pygame
import sys
import os.path


class TextBox:
    """
    Class which can handle text vizualization including text wraping bold/italic/font text size, color, etc..
    """

    def __init__(self, surface, pos, width, color="black", letter_size=30, word_height=0, bold=True) -> None:

        self.text = " "

        self.letter_size = letter_size

        self.color = color
        self.pos = pos
        self.width = width
        self.bold = bold
        self.custom_word_height = word_height
        self.surface = surface
        self.font = None

        # Experiment with different types of fonts. Pygame can only read .ttf files
        # self.font_path = "game/Font/Pixeltype.ttf"
        # self.font_path = "game/Font/pixelarmy/PixelArmy.ttf"
        # self.font_path = "game/Font/bitmgothic/Bitmgothic/Bitmgothic.ttf"
        # self.font_path = "game/Font/7-12-serif/712_serif.ttf"

        self.font_path = os.path.join("game", "Font", "7-12-serif", "712_serif.ttf")

    def display_text(self) -> None:
        """
        Display the text in the containment of the text box width

        @return:
        """
        self.font = pygame.font.Font(self.font_path, self.letter_size)
        self.font.set_bold(self.bold)
        collection = [word.split(' ') for word in self.text.splitlines()]
        space = self.font.size(' ')[0]
        x, y = self.pos
        for lines in collection:
            for words in lines:
                word_surface = self.font.render(words, True, self.color)
                word_width, word_height = word_surface.get_size()
                word_height = word_height - self.custom_word_height
                if x + word_width >= self.width:
                    x = self.pos[0]
                    y += word_height
                self.surface.blit(word_surface, (x, y))
                x += word_width + space
            x = self.pos[0]
            y += word_height

    def move(self, new_position: Tuple[int, int]) -> None:
        """
        Move text based on object data

        @param new_position: The new position that the text should be rendered
        @return:
        """
        self.pos = new_position
