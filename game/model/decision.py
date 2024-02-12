from typing import Tuple, List, Callable

class Decision:
    """
    User can decide between 2 options and the decision has consequences that affect the Player class variables
    @todo-make it so that it isn't a choice between 2 options
    """

    def __init__(self, decision_type: str, title: str, description: str, cost: Tuple[int, int, int],
                 consequences: List[Callable], player: Callable, level: Callable) -> None:
        """
        Initialize the Decision object

        @param decision_type: ONCE,CONTINUOUS,STORY -different bacground images
        @param title:
        @param description:
        @param cost: in terms of loyalty,money, readership
        @param consequences: in terms of player variables
        @param player: reference to the player class
        @param level: reference to the Level class
        """

        self.decision_type = decision_type
        self.cost = cost
        self.consequence = consequences
        self.player = player
        self.level = level
        self.checked = False

        self.title = title
        self.description = description

        self.active = False
        self.show = False

    def agree_decision(self) -> None:
        """
        Execute the functions that play the consequences after user agrees to decision

        @return:
        """
        if self.checked is False:
            self.checked = True
            # print("AGREE WITH DECISION")
            if self.decision_type == "ONCE":
                self.level.one_time_expenses.append(self.cost)
            if self.decision_type == "CONTINUOUS":
                self.level.contiuous_expenses.append(self.cost)

            for consequence in self.consequence:
                consequence(self.player)

    def disagree_decision(self) -> None:
        """
        Nothing happens
        @return:
        """
        if self.checked is False:
            self.checked = True

            # print("DISAGREE WITH DECISION")

    def clear(self) -> None:
        """
        Stops rendering the decision UI
        @return:
        """
        self.show = False
