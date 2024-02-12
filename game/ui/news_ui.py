from typing import Tuple, List, Callable

import pygame

from game.settings import *
from game.model.timer import Timers
from game.ui.text_box_ui import TextBox
import os.path


# TODO add story image


class NewsUI:
    """
    UI class that is rendered on screen. This class handles news articles that are shown on the news paper grid.
    Currently, has collision problems that makes two UI intractable news to be grouped together when rect are
    intersecting and user clicks on the intersecting area. Code was inspired by this battleship tutorial:
    https://github.com/GrizzlyH/Battleship_Walkthrough. The code has been heavily modified

    @todo - fix collision
    @todo - make a hierarchy that inherits user-movable objects
    @todo - add animations
    """

    def __init__(self, news: Callable, grid: Tuple[int, int]) -> None:
        """
        Initialize NewsUI class
        @param news:
        @param grid:
        """
        # All the info about the news
        self.grid = grid
        self.news = news
        self.pos = (300, 300)

        # TODO what if file is not found and Exception should be handled
        self.background_surf = [
            pygame.image.load(
                os.path.join("game", "Sprites", "articles", "small_article.png")).convert(),
            pygame.image.load(
                os.path.join("game", "Sprites", "articles", "medium_article.png")).convert(),
            pygame.image.load(
                os.path.join("game", "Sprites", "articles", "large_article.png")).convert()]

        self.current_surf = None
        self.current_rect = self.background_surf[0].get_rect()

        self.s_pos = (
            self.current_rect.topleft[0] + 87, self.current_rect.topleft[1] + 38)

        if self.news.title == "Sunny!":

            if self.news.is_colored == True:
                img_path = os.path.join("game", "Sprites", "news_images", str.lower(self.news.news_type),
                                        str.lower(self.news.title) + "_color.png")
            else:
                img_path = os.path.join("game", "Sprites", "news_images", str.lower(self.news.news_type),
                                        str.lower(self.news.title) + "_gray.png")
                # file_name = "game/Sprites/news_images/" + str.lower(self.news.news_type) + '/' + str.lower(self.news.title) + ".png"
            self.story_image_surf = pygame.image.load(img_path).convert()
            self.story_image_rect = self.story_image_surf.get_rect()

        # Timer is used for a cooldown on clicking on the article else the user would have the UI perminantly
        # stuck to the mouse position
        self.timer = Timers(200)

        self.display_surface = pygame.display.get_surface()

        # Title position
        self.t_pos = (
            self.current_rect.topleft[0] + 5, self.current_rect.topleft[1])
        self.title = TextBox(self.display_surface,
                             self.t_pos,
                             self.current_rect.topright[0] - 5, "white", 25, 5)
        self.title.text = self.news.title

        # This helps us determine if the user is currently interacting with object hence object is actively in use
        self.active = False

    def input(self, envelope_list: List[Callable]) -> None:
        """
        Handles the user input. And provides the check_for_collision envelope list

        @param envelope_list: A list with all objects of type EnvelopeUI
        @return:
        """
        if self.current_rect.collidepoint(pygame.mouse.get_pos()):
            # print(f"active : {self.active} timer: {self.timer.active} pressed: {pygame.mouse.get_pressed()[0]}")
            if not self.timer.active:
                if pygame.mouse.get_pressed()[0] and not self.timer.active and self.active == True:
                    # print("clicked off")
                    # self.return_to_default_position()
                    self.configure_grid_snap(envelope_list)
                    self.timer.activate()
                    self.active = False

                if pygame.mouse.get_pressed()[0] and not self.timer.active and self.active == False:
                    # print("clicked on")
                    self.timer.activate()
                    self.active = True

    def check_for_collision(self, envelope_list: List[Callable]) -> None:
        """Check to make sure the news is not colliding with any of the other news in the news grid"""
        # print(envelope_list)
        n_list = [envelope.news_ui for envelope in envelope_list].copy()
        # removes the reference to the current NewsUI object
        n_list.remove(self)
        for item in n_list:
            if not item.news.show:
                # print("No collision")
                continue
            if self.current_rect.colliderect(item.current_rect):
                # print("Collide")
                return True
        return False

    def return_to_default_position(self) -> None:
        """Returns the news to its default position - Non existing"""
        self.active = False
        self.news.clear()
        self.current_rect = None

    def snap_to_grid_edge(self) -> None:
        """
        Function that handles the edge cases of when the user puts the news ui on the edge of the paper.

        @todo - rework the collision logic
        """
        if self.current_rect.topleft != self.pos:
            # print(f"rect.left : {self.rect.left}")
            # print(f"rect.midleft : {self.rect.midleft}")
            # print("=========")
            #  Check to see if the ships position is outside of the grid:
            # print("=====")
            # print("top news coords: " + str(self.current_rect.top))
            # print("top gripd coords: " + str(self.grid.coord_grid[-1][0][1]))

            if self.current_rect.left > self.grid.coord_grid[0][-1][0] + GRID_CELL_SIZE or \
                    self.current_rect.right < self.grid.coord_grid[0][0][0] or \
                    self.current_rect.top > self.grid.coord_grid[-1][0][1] + GRID_CELL_SIZE or \
                    self.current_rect.bottom < self.grid.coord_grid[0][0][1]:
                self.return_to_default_position()
            elif self.current_rect.right > self.grid.coord_grid[0][-1][0] + GRID_CELL_SIZE:
                self.current_rect.right = self.grid.coord_grid[0][-1][0] + \
                                          GRID_CELL_SIZE
            elif self.current_rect.left < self.grid.coord_grid[0][0][0]:
                self.current_rect.left = self.grid.coord_grid[0][0][0]
            elif self.current_rect.top < self.grid.coord_grid[0][0][1]:
                self.current_rect.top = self.grid.coord_grid[0][0][1]
            elif self.current_rect.bottom > self.grid.coord_grid[-1][0][1] + GRID_CELL_SIZE:
                self.current_rect.bottom = self.grid.coord_grid[-1][0][1] + \
                                           GRID_CELL_SIZE
            # 23.04.2021 - 15:30

    def snap_to_grid(self) -> None:
        """
        Position the news ui element to fit inside the cells of the paper grid
        @return:
        """
        for rowX in self.grid.coord_grid:
            for cell in rowX:
                if cell[0] <= self.current_rect.left < cell[0] + GRID_CELL_SIZE and cell[1] <= self.current_rect.top < \
                        cell[1] + GRID_CELL_SIZE:
                    self.current_rect.topleft = (
                        cell[0], cell[1] + (GRID_CELL_SIZE - self.current_surf.get_height()) // 2)

    def draw(self):
        """Draw the n news to the screen"""
        if self.active:
            self.pos = pygame.mouse.get_pos()
            self.current_rect.center = self.pos

        if self.news.show:
            self.display_surface.blit(self.current_surf, self.current_rect)
            self.s_pos = (
                self.current_rect.topleft[0] + 87, self.current_rect.topleft[1] + 38)
            self.draw_text()

            # TODO - Draw more story images
            if self.news.is_large is True and self.news.title == "Sunny!":
                self.s_pos = (
                    self.current_rect.topleft[0] + 87, self.current_rect.topleft[1] + 38)
                self.story_image_rect.topleft = self.s_pos
                self.display_surface.blit(
                    self.story_image_surf, self.story_image_rect)

    def configure_grid_snap(self, envelope_list: List[Callable]) -> None:
        if self.check_for_collision(envelope_list):
            self.return_to_default_position()
            return
        if self.active:
            self.snap_to_grid_edge()
        if self.active:
            self.snap_to_grid()

    def create_s(self) -> None:
        """
        Creates a small 1x1 article. Calls the News create_s func()

        @return:
        """
        self.news.create_s()
        self.current_surf = self.background_surf[0]
        self.current_rect = self.current_surf.get_rect(center=self.pos)
        self.title.letter_size = 15
        self.active = True

    def create_m(self) -> None:
        """
        Creates a medium 2x1 article
        @return:
        """
        self.news.create_m()
        self.current_surf = self.background_surf[1]
        self.current_rect = self.current_surf.get_rect(center=self.pos)
        self.title.letter_size = 20

        self.active = True

    def create_l(self) -> None:
        """
        Create a large 3x3 article
        @return:
        """
        self.news.create_l()
        self.current_surf = self.background_surf[2]
        self.current_rect = self.current_surf.get_rect(center=self.pos)
        self.title.letter_size = 35

        self.active = True

    def draw_text(self) -> None:
        """
        Draws the title of the news article above the news article background image
        @return:
        """
        self.t_pos = (
            self.current_rect.topleft[0] + 5, self.current_rect.topleft[1])

        self.title.width = self.current_rect.topright[0] - 5

        self.title.move(self.t_pos)

        self.title.display_text()

    def clear(self):
        """
        Cleared the rendered news objects since the level is over or some other case
        @return:
        """
        self.news.clear()
        self.active = False

    def update(self, envelope_list):
        if self.news.show:
            self.timer.update()
            self.input(envelope_list)
            self.draw()
