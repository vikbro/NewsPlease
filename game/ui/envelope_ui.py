import os.path
from typing import Tuple, List, Callable

import pygame
from game.ui.button_ui import Button
from game.settings import *
from game.model.timer import Timers
from game.ui.text_box_ui import TextBox
from game.ui.news_ui import NewsUI


# EnvelopeUI makes the connection between player and news (color->color)
class EnvelopeUI:
    """
    Class that handles the visualization of the news and UI
    
    @todo - fix collision
    @todo - make a hierarchy that inherits user-movable objects
    @todo - add animations
    """

    def __init__(self, news: Callable, pos: Tuple[int, int], player: Callable, grid: Tuple[int, int]) -> None:
        """
        Initialize the EnvelopeUI class

        @param news:
        @param pos:
        @param player:
        @param grid:
        """
        self.pos = pos
        self.grid = grid
        self.player = player
        self.timer = Timers(300)
        self.is_small = True
        self.active = False
        self.is_shown = False
        self.display_surface = pygame.display.get_surface()

        self.news = news
        # change news variables
        self.news.color = player.allow_coloured_articles

        self.news_ui = NewsUI(self.news, self.grid)

        self.s_img = None
        self.s_rect = None

        self.l_img = pygame.Surface((ENV_L_WIDTH, ENV_L_HEIGHT))
        self.l_rect = self.l_img.get_rect(center=self.pos)

        self.confing_img()

        self.img_surf = self.s_img
        self.rect = self.s_rect

        # Title position
        self.t_pos = (self.rect.topleft[0] + 10, self.rect.topleft[1] + 10)
        self.title = TextBox(self.display_surface,
                             self.t_pos,
                             self.l_rect.topright[0] - 10)
        self.title.text = self.news.title
        # Desciption position
        self.d_pos = (self.rect.topleft[0] + 50, self.rect.topleft[1] + 50)
        self.descrption = TextBox(self.display_surface,
                                  self.d_pos,
                                  self.l_rect.topright[0] - 10, "black", 20, 5, False)
        self.descrption.text = self.news.description

        # Button positions
        self.s_pos = (self.rect.center[0] + 30, self.rect.center[1] + 20)
        self.m_pos = (self.rect.center[0] - 20, self.rect.center[1] + 20)
        self.l_pos = (self.rect.center[0] - 75, self.rect.center[1] + 20)

        self.s_btn = Button("S",
                            ENV_BTN_WIDTH,
                            ENV_BTN_HEIGHT,
                            self.s_pos,
                            BTN_ELEVATION,
                            self.create_s_news)
        self.m_btn = Button("M",
                            ENV_BTN_WIDTH,
                            ENV_BTN_HEIGHT,
                            self.m_pos,
                            BTN_ELEVATION,
                            self.create_m_news)
        self.l_btn = Button("L",
                            ENV_BTN_WIDTH,
                            ENV_BTN_HEIGHT,
                            self.l_pos,
                            BTN_ELEVATION,
                            self.create_l_news)

    def confing_img(self) -> None:
        """
        Configure the images of the large and small envelope depending on the news type
        @return:
        """
        # TODO open a folder with the said sprite
        # TODO add exception hadling
        if self.news.news_type == "WEATHER":
            os.path.join("game", "Sprites", "envelope", "small", "weather_envelope.png")
            os.path.join("game", "Sprites", "envelope", "small", "politics_envelope.png")
            os.path.join("game", "Sprites", "envelope", "small", "ad_envelope.png")

            self.s_img = pygame.image.load(
                os.path.join("game", "Sprites", "envelope", "small", "weather_envelope.png")).convert()
            self.l_img = pygame.image.load(
                os.path.join("game", "Sprites", "envelope", "large", "weather_envelope.png")).convert()
            # print("WEATHER")
        if self.news.news_type == "POLITICS":
            self.s_img = pygame.image.load(
                os.path.join("game", "Sprites", "envelope", "small", "politics_envelope.png")).convert()

            self.l_img = pygame.image.load(
                os.path.join("game", "Sprites", "envelope", "large", "politics_envelope.png")).convert()
            # print("POLITICS")
        if self.news.news_type == "AD":
            self.s_img = pygame.image.load(
                os.path.join("game", "Sprites", "envelope", "small", "ad_envelope.png")).convert()

            self.l_img = pygame.image.load(
                os.path.join("game", "Sprites", "envelope", "large", "ad_envelope.png")).convert()
            # print("AD")

        # configure rectangles
        self.s_rect = self.s_img.get_rect(center=self.pos)

    def create_s_news(self) -> None:
        """
        Create small news
        @return:
        """
        self.active = False
        self.news_ui.create_s()
        # print("small NEWS")

    def create_m_news(self) -> None:
        """
        Create medium news
        @return:
        """
        self.active = False
        self.news_ui.create_m()
        # print("medium")

    def create_l_news(self) -> None:
        """
        Create large news
        @return:
        """
        self.active = False
        self.news_ui.create_l()
        # print("large")

    def draw(self) -> None:
        """
        Draws the envelope on the level UI

        @return:
        """
        self.display_surface.blit(self.img_surf, self.rect)
        if not self.is_small:
            if self.active:
                self.rect.center = pygame.mouse.get_pos()
                self.s_pos = (
                    self.rect.center[0] + 30, self.rect.center[1] + 20)
                self.m_pos = (
                    self.rect.center[0] - 20, self.rect.center[1] + 20)
                self.l_pos = (
                    self.rect.center[0] - 75, self.rect.center[1] + 20)

                self.s_btn.move(self.s_pos)
                self.m_btn.move(self.m_pos)
                self.l_btn.move(self.l_pos)

            self.draw_buttons()
            self.draw_text()

        elif self.active:
            self.rect.center = pygame.mouse.get_pos()

    def draw_buttons(self) -> None:
        """
        Draw buttons

        @return:
        """
        if self.player.allow_small_news:
            self.s_btn.draw()
        if self.player.allow_medium_news:
            self.m_btn.draw()
        if self.player.allow_large_news:
            self.l_btn.draw()

    def draw_text(self) -> None:
        """
        Draw text

        @return:
        """
        self.t_pos = (
            self.rect.topleft[0] + 15, self.rect.topleft[1] + 10)
        self.d_pos = (
            self.rect.topleft[0] + 15, self.rect.topleft[1] + 40)

        self.title.width = self.l_rect.topright[0] - 10
        self.descrption.width = self.l_rect.topright[0]

        self.title.move(self.t_pos)
        self.descrption.move(self.d_pos)

        self.title.display_text()
        self.descrption.display_text()

    def input(self, work_area: Tuple[int, int]) -> None:
        """
        Logic when user clicks on the envelope

        @param work_area: Area in which the news/decision/notes spawn in
        @todo - fix collision overlap problem
        @return:
        """
        mouse_pos = pygame.mouse.get_pos()
        if work_area.collidepoint(mouse_pos) and self.rect.collidepoint(mouse_pos):
            self.img_surf = self.s_img
            self.rect = self.s_rect
            self.is_small = True

            if not self.timer.active:
                if pygame.mouse.get_pressed()[0] and not self.timer.active and self.active == True:
                    # print(
                    #     f"active : {self.active} timer: {self.timer.active} pressed: {pygame.mouse.get_pressed()[0]}")
                    # print("clicked off -")
                    self.timer.activate()
                    self.active = False

                elif pygame.mouse.get_pressed()[0] and not self.timer.active and self.active == False:
                    # print("clicked on -")
                    self.timer.activate()
                    self.active = True

        elif self.rect.collidepoint(mouse_pos) and \
                self.s_btn.top_rect.collidepoint(mouse_pos) == False and \
                self.m_btn.top_rect.collidepoint(mouse_pos) == False and \
                self.l_btn.top_rect.collidepoint(mouse_pos) == False:

            self.img_surf = self.l_img
            self.rect = self.l_rect
            self.is_small = False
            # print(f"active : {self.active} timer: {self.timer.active} pressed: {pygame.mouse.get_pressed()[0]}")
            if not self.timer.active:
                if pygame.mouse.get_pressed()[0] and not self.timer.active and self.active == True:
                    # print("clicked off")
                    self.timer.activate()
                    self.active = False

                elif pygame.mouse.get_pressed()[0] and not self.timer.active and self.active == False:
                    # print("clicked on")
                    self.timer.activate()
                    self.active = True

    def spawn(self) -> None:
        """
        Make envelope visible in the level UI

        @return:
        """
        # self.pos = (randint(0,working_area.bottomright[0]),randint(0,working_area.bottomright[1]))
        self.is_shown = True

    def update(self, work_area: Tuple[int,int], paper_list: List) -> None:
        if self.is_shown:
            self.news_ui.update(paper_list)
            self.input(work_area)
            self.timer.update()
            self.draw()
