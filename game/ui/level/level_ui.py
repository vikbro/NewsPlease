from typing import Callable

import pygame

from game.model.timer import Timers
from game.ui.envelope_ui import EnvelopeUI
from game.ui.decision_ui import DecisionUI
from game.model.grid import Grid
from game.ui.overlay_ui import Overlay
from game.settings import *

import os.path
import random


class LevelUI:
    """
    Every load of a level this class reset and loads new elements. In this class all the UI elements are contained in
    one form or another

    """

    def __init__(self, game: Callable, level: Callable, player: Callable) -> None:
        self.level = level
        self.game = game
        self.player = player
        self.day = level.current_day
        self.active = False
        
        #SOUND
        self.clock_sound = pygame.mixer.Sound(os.path.join("game", "Music", "clock.wav"))
        self.ambiance_sound = pygame.mixer.Sound(os.path.join("game", "Music", "room_ambiance.wav"))
        self.bell = pygame.mixer.Sound(os.path.join("game", "Music", "ding.mp3"))


        self.all_papers_ui = []
        self.envelope_ui = []
        # how many papers have been spawned
        self.__current_count = 0

        # First envelope spawn
        self.timer = Timers(random.randint(1, 9))
        self.timer.activate()

        # background image by Nikola Chobanov - ig: teslarov_arts
        os.path.join("game", "Sprites", "level", "print_layout.png")
        self.background = pygame.image.load(
            os.path.join("game", "Sprites", "level", "print_layout.png")).convert()
        self.display_surf = pygame.display.get_surface()
        self.work_area_surf = pygame.Surface((500, 100))
        self.work_area_surf.fill((100, 100, 100))
        self.work_area_rect = self.work_area_surf.get_rect()
        self.overlay = Overlay(self.level, self.player, self)
        self.grid = Grid((int(GRID_POS_X), int(GRID_POS_Y)),
                         self.player.grid_dimentions, GRID_CELL_SIZE)

    def draw_grid(self) -> None:
        """
        Show the rectangle grid in which the news are inserted. Loading an image would be preferred

        @return:
        """
        for row in self.grid.coord_grid:
            for col in row:
                pygame.draw.rect(self.display_surf, (255, 0, 0),
                                 (col[0], col[1], GRID_CELL_SIZE, GRID_CELL_SIZE), 1)

    def show_news(self) -> None:
        """
        Make the "News" (Papers is a preferred terminology) visible

        @return:
        """
        if not self.timer.active and self.__current_count < len(self.level.all_papers):

            if type(self.level.all_papers[self.__current_count]).__name__ == "News":
                paper = EnvelopeUI(
                    self.level.all_papers[self.__current_count],
                    (random.randint(0, self.work_area_rect.bottomright[0]),
                     random.randint(0, self.work_area_rect.bottomright[1])),
                    self.player,
                    self.grid
                )
            if type(self.level.all_papers[self.__current_count]).__name__ == "Decision":
                paper = DecisionUI(
                    self.level.all_papers[self.__current_count],
                    (random.randint(0, self.work_area_rect.bottomright[0]),
                     random.randint(0, self.work_area_rect.bottomright[1])),
                    self.player
                )
            self.bell.play()
            paper.spawn()
            # Contain all papers of type Envelope,Decision,Notes
            self.all_papers_ui.append(paper)

            # change the timer
            # Timer to determine the spawn rate of the envelopes
            self.timer = Timers(random.randint(1000, 5000))
            self.timer.activate()
            self.__current_count += 1
            # Contain all papers of type Envelope
            self.envelope_ui = [envelope for envelope in self.all_papers_ui if type(
                envelope).__name__ is "EnvelopeUI"]

    def begin_day(self) -> None:
        """
        Begin level by making the level UI visible also generate all the news/decisions/notes that are to be printed
        @return:
        """
        self.active = True
        self.level.begin_day()
        self.clock_sound.play(loops=-1)  # maybe loop it
        self.ambiance_sound.play(loops=-1)

    def end_day(self) -> None:
        """
        End day and run all methods to make sure the result is calculated and the level is clear for the
        generation of the next level
        @return:
        """
        self.active = False
        self.__current_count = 0
        self.level.end_day()
        self.clock_sound.stop()
        self.ambiance_sound.stop()
        self.clear()

    def clear(self) -> None:
        """
        Clear all essential data in order to load next level

        @return:
        """
        self.all_papers_ui = []
        # self.grid = None

    def update(self):
        """
        Updated every element in the level

        @todo - fix the FPS problem

        @return:
        """
        if not self.active:
            self.begin_day()

        self.timer.update()
        self.display_surf.blit(self.background, (0, 0))
        self.display_surf.blit(self.work_area_surf, self.work_area_rect)
        self.overlay.draw()
        self.draw_grid()
        self.show_news()

        # print(self.envelope_ui)
        # Something is not right in this method- getting low fps after a long time
        for paper in self.all_papers_ui:
            if type(paper) is EnvelopeUI:
                paper.update(self.work_area_rect,
                             self.envelope_ui)
            else:
                paper.update(self.work_area_rect)
