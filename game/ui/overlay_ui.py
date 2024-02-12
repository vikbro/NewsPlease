from typing import Callable

import pygame
from game.settings import *
# from clock import Clock
from game.ui.button_ui import Button


class Overlay:
    """
    Displays the user information independently from the LevelUI class

    """

    def __init__(self, level: Callable, player: Callable, level_ui: Callable) -> None:
        # screen
        self.display_surface = pygame.display.get_surface()
        self.player = player
        self.level = level
        self.level_ui = level_ui

        # buttons
        self.btn_menu = Button("MENU", BTN_WIDTH, BTN_HEIGHT,
                               BUTTON_POSITION["menu"], BTN_ELEVATION, self.level.game.return_menu)
        self.btn_save = Button("Save game", BTN_WIDTH, BTN_HEIGHT,
                               BUTTON_POSITION["save"], BTN_ELEVATION, self.level.player.save)
        self.btn_continue = Button(
            "CONTINUE", BTN_WIDTH, BTN_HEIGHT, BUTTON_POSITION["continue"], BTN_ELEVATION)
        self.btn_continue = Button("End day", BTN_WIDTH, BTN_HEIGHT,
                                   BUTTON_POSITION["pause"], BTN_ELEVATION, self.level.game.next_state)

        # money
        self.money_surf = pygame.Surface(
            (OVERLAY_TILE_SIZE + 10, OVERLAY_TILE_SIZE + 10))
        self.money_surf.fill("#475F77")
        self.money_rect = self.money_surf.get_rect(
            midbottom=OVERLAY_POSITIONS["money"])

        # loyalty
        self.loyalty_surf = pygame.Surface(
            (OVERLAY_TILE_SIZE + 10, OVERLAY_TILE_SIZE + 10))
        self.loyalty_surf.fill("#475F77")
        self.loyalty_rect = self.loyalty_surf.get_rect(
            midbottom=OVERLAY_POSITIONS["loyalty"])
        # readership
        self.readership_surf = pygame.Surface(
            (OVERLAY_TILE_SIZE + 10, OVERLAY_TILE_SIZE + 10))
        self.readership_surf.fill("#475F77")
        self.readership_rect = self.readership_surf.get_rect(
            midbottom=OVERLAY_POSITIONS["readership"])

        self.font = pygame.font.SysFont("Times New Roman", 30)

        # self.clock = Clock()

        # current_time = int(pygame.time.get_ticks()//1000) - start_time
        # score_surf = test_font.render(f'{player.readershipScore}',False,(64,64,64))
        # score_rect = score_surf.get_rect(center = (400,50))
        # screen.blit(score_surf,score_rect)

    def open_menu(self) -> None:
        # print("opened menu")
        pass

    def open_options(self) -> None:
        # print("open options")
        pass

    def draw_btn(self) -> None:
        """
        Draws the options,menu, pause save buttons
        @return:
        """

        self.btn_save.draw()
        self.btn_menu.draw()
        self.btn_continue.draw()

    def display_money(self) -> None:
        """
        Display the money information if the player allows it (perk is bought)
        @return:
        """
        self.display_surface.blit(self.money_surf, self.money_rect)
        current_money_surf = self.font.render(
            f'{self.player.money_score}', False, (255, 255, 255))
        current_money_rect = current_money_surf.get_rect(
            midbottom=OVERLAY_POSITIONS["money"])
        self.display_surface.blit(current_money_surf, current_money_rect)

    def display_readership(self) -> None:
        """
        Display the readership information if the player allows it (perk is bought)

        @return:
        """
        self.display_surface.blit(self.readership_surf, self.readership_rect)
        current_readership_surf = self.font.render(
            f'{self.player.readership_score}', False, (255, 255, 255))
        current_readership_rect = current_readership_surf.get_rect(
            midbottom=OVERLAY_POSITIONS["readership"])
        self.display_surface.blit(
            current_readership_surf, current_readership_rect)

    def display_loyalty(self) -> None:
        """
        Display the Loaylty information if the player allows it (perk is bought)

        @return:
        """
        self.display_surface.blit(self.loyalty_surf, self.loyalty_rect)
        current_loyalty_surf = self.font.render(
            f'{self.player.loyalty_score}', False, (255, 255, 255))
        current_loyalty_rect = current_loyalty_surf.get_rect(
            midbottom=OVERLAY_POSITIONS["loyalty"])
        self.display_surface.blit(current_loyalty_surf, current_loyalty_rect)

    def display_clock(self) -> None:
        """

        @todo- make timer for the level based on the work hours of the player
        @return:
        """
        # self.clock.update
        pass

    def draw(self) -> None:
        """
        Displays based on player data
        @return:
        """
        if self.player.show_loyalty:
            self.display_loyalty()
        if self.player.show_money:
            self.display_money()
        if self.player.show_readership:
            self.display_readership()

        self.draw_btn()
        # self.display_clock()
