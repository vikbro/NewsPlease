import pygame
import sys

from game.model.player import Player
from game.model.level import Level
from game.ui.main_menu_ui import MainManuUI
from game.ui.level.begin_level_ui import BeginLevelUI
from game.ui.level.end_level_ui import EndLevelUI
from game.ui.level.level_ui import LevelUI
from game.dayTree import isinstance_map, DECISIONS

# Enum for what game state we are in currently
GameStates = {

    "MainScreen": 0,
    "BeginLevel": 1,
    "Level": 2,
    "EndLevel": 3
}


class Game:
    """
    Handles the logic of which scene should be currently displayed. Everything starts from this class.
    """

    def __init__(self):
        # game states
        self.player = Player()
        self.level = Level(self.player, self)
        self.run_game = True

        # Maybe not initialize UI for testing purposes?
        self.level_ui = LevelUI(self, self.level, self.player)
        self.main_screen = MainManuUI(self)
        self.begin_level = BeginLevelUI(self, self.level)
        self.end_level = EndLevelUI(self, self.level_ui)

        # TODO ENDING
        # self.ending = Ending()
        # Enum value of what state we are in currently

        self.current_state = "MainScreen"

        # UI
        self.updates = [self.main_screen.update, self.begin_level.update,
                        self.level_ui.update, self.end_level.update]

    def next_state(self) -> None:
        # print("NEXT STATE " + self.current_state)
        match self.current_state:
            case "MainScreen":
                self.begin_level.activated = True
                self.current_state = "BeginLevel"

            case "BeginLevel":
                self.current_state = "Level"

            case "Level":
                self.level_ui.end_day()
                self.end_level.activated = True
                self.current_state = "EndLevel"

            case "EndLevel":
                self.begin_level.activated = True
                self.current_state = "BeginLevel"

    def reset_decisions(self) -> None:
        # Reset all decisions that have been used
        for decision_list in DECISIONS["ONCE"]:
            # Change the last element of the interior list to False
            decision_list[-1] = False
        for decision_list in DECISIONS["CONTINUOUS"]:
            # Change the last element of the interior list to False
            decision_list[-1] = False
        # for decision_list in DECISIONS["STORY"]:
        #     # Change the last element of the interior list to False
        #     decision_list[-1] = False

    def return_menu(self) -> None:
        if "END" in self.level.current_day.day_name:
            # messy solution in order to start a new level also resets the used decisions
            self.level.current_day = isinstance_map[self.player.day]
            self.reset_decisions()

        if self.current_state == "Level":
            self.level_ui.end_day()
        self.end_level.activated = True
        self.current_state = "MainScreen"

    def exit_game(self) -> None:
        """
        @todo Not what is intendet
        @return:
        """
        self.run_game = False
        # pygame.quit()
        # sys.exit()

    def run(self, clock) -> None:
        """
        Run the game trough this method. All the game is conducted here
        @param clock:
        @return:
        """
        # Added "exit" to see if i could make a profile of the code but for some reason doesnt show
        self.run_game = True
        while self.run_game:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run_game = False

            # dt = self.clock.tick(60) / 1000
            # FPS of the game but if there are a lot of objects there is a severe frame rate drop
            clock.tick(60)
            self.updates[GameStates[self.current_state]]()
            pygame.display.update()
