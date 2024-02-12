from typing import Tuple, Callable

import pygame
from game.ui.button_ui import Button
from game.settings import *
from game.model.timer import Timers
from game.ui.text_box_ui import TextBox


class DecisionUI:
    """
    Handles the UI of the class Decision and renders the object
    
    @todo - fix collision
    @todo - make a hierarchy that inherits user-movable objects
    @todo - add animations
    """

    def __init__(self, decision: Callable, pos: Tuple[int, int], player: Callable) -> None:
        self.pos = pos
        self.player = player
        self.timer = Timers(300)
        self.is_small = True
        self.active = False
        self.is_shown = False
        self.display_surface = pygame.display.get_surface()

        self.decision = decision

        # self.s_img = pygame.Surface((ENV_S_WIDTH, ENV_S_HEIGHT))
        # self.s_rect = self.s_img.get_rect(center=self.pos)
        self.s_img = None
        self.s_rect = None

        self.l_img = pygame.Surface((DEC_L_WIDTH, DEC_L_HEIGHT))
        self.l_rect = self.l_img.get_rect(center=self.pos)

        self.confing_img()

        self.img_surf = self.s_img
        self.rect = self.s_rect

        # Position of the title text
        self.t_pos = (self.rect.topleft[0] + 10, self.rect.topleft[1] + 10)
        self.title = TextBox(self.display_surface,
                             self.t_pos,
                             self.l_rect.topright[0] - 10, "white")
        self.title.text = self.decision.title

        # Position of the description text
        self.d_pos = (self.rect.topleft[0] + 50, self.rect.topleft[1] + 50)
        self.descrption = TextBox(self.display_surface,
                                  self.d_pos,
                                  self.l_rect.topright[0] - 10, "white", 20, 5, False)
        self.descrption.text = self.decision.description
        # Yes button position
        self.y_pos = (self.rect.center[0] - (DEC_BTN_WIDTH / 2), self.rect.center[1] + 50)
        # No button position
        self.n_pos = (self.rect.center[0] - (DEC_BTN_WIDTH / 2), self.rect.center[1] + 110)

        self.y_btn = Button("Agree",
                            DEC_BTN_WIDTH,
                            DEC_BTN_HEIGHT,
                            self.y_pos,
                            BTN_ELEVATION,
                            self.decision.agree_decision)
        self.n_btn = Button("Disagree",
                            DEC_BTN_WIDTH,
                            DEC_BTN_HEIGHT,
                            self.n_pos,
                            BTN_ELEVATION,
                            self.decision.disagree_decision)
        # variables to help configure result

    def confing_img(self) -> None:
        """
        Configure background image depending on the Description type

        @return:
        """
        # TODO open a folder with the said sprite
        # TODO no exception handling

        if self.decision.decision_type == "ONCE":
            self.s_img = pygame.image.load(
                "game/Sprites/envelope/small/decision.png").convert()
            self.l_img = pygame.image.load(
                "game/Sprites/envelope/large/decision.png").convert()
            # print("ONCE")
        if self.decision.decision_type == "CONTINUOUS":
            self.s_img = pygame.image.load(
                "game/Sprites/envelope/small/decision.png").convert()

            self.l_img = pygame.image.load(
                "game/Sprites/envelope/large/decision.png").convert()
            # print("CONTINUOUS")

        # configure rectangles
        self.s_rect = self.s_img.get_rect(center=self.pos)

    def draw(self) -> None:
        """
        Draws the decision object

        @return:
        """
        self.display_surface.blit(self.img_surf, self.rect)
        if not self.is_small:
            if self.active:
                self.rect.center = pygame.mouse.get_pos()

                # self.y_pos = (self.rect.center[0], self.rect.center[1] + 50)
                # self.n_pos = (self.rect.center[0], self.rect.center[1] + 110)
                self.y_pos = (

                    self.rect.center[0] - (DEC_BTN_WIDTH / 2), self.rect.center[1] + 10)
                self.n_pos = (
                    self.rect.center[0] - (DEC_BTN_WIDTH / 2), self.rect.center[1] + 60)

                self.y_btn.move(self.y_pos)
                self.n_btn.move(self.n_pos)

            # self.display_surface.blit(self.discription_text_surf,self.discription_text_rect)

            self.draw_buttons()
            self.draw_text()

        elif self.active:
            self.rect.center = pygame.mouse.get_pos()

    def draw_buttons(self) -> None:
        """
        Draw agree and disagree buttons

        @return:
        """
        self.y_btn.draw()
        self.n_btn.draw()

    def draw_text(self) -> None:
        """
        Draws title and description text

        @return:
        """
        self.t_pos = (
            self.rect.topleft[0] + 5, self.rect.topleft[1] + 5)
        self.d_pos = (
            self.rect.topleft[0] + 5, self.rect.topleft[1] + 50)

        self.title.width = self.l_rect.topright[0] - 5
        self.descrption.width = self.l_rect.topright[0] - 5

        self.title.move(self.t_pos)
        self.descrption.move(self.d_pos)

        self.title.display_text()
        self.descrption.display_text()

    def input(self, work_area: Tuple[int, int]) -> None:
        """
        Function that handles when user clicks on the decision rect

        @param work_area: The square area that the envelopes spawns in
        @return:
        """

        mouse_pos = pygame.mouse.get_pos()
        if work_area.collidepoint(mouse_pos) and self.rect.collidepoint(mouse_pos):
            # print("IN AREA")

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
                self.y_btn.top_rect.collidepoint(mouse_pos) == False and \
                self.n_btn.top_rect.collidepoint(mouse_pos) == False:

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
        Shows the object on the level UI
        @return:
        """
        
        # self.pos = (randint(0,working_area.bottomright[0]),randint(0,working_area.bottomright[1]))
        self.is_shown = True

    def update(self, work_area: Tuple[int, int]) -> None:
        if self.is_shown:
            self.input(work_area)
            self.timer.update()
            self.draw()
