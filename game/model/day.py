from typing import Callable, List, Union


class Day:
    def __init__(self, left, right, condition: Union[List[Callable], None], calculation, type_news,
                 type_decisions,
                 text=None, day_name="") -> None:
        """
        Day handles the conditions the calculation and the children of the class (Node) in the graph also commands
        what type stories will be printed, decisions,notes, and the consequences to the decisions taken by the user

        :param left: the left children of the node
        :param right: the left children of the node
        @todo - be able to read the day data from a file
        @todo - day name potentially not needed
 
        """
        self.day_name = day_name
        # TODO refactor name
        self.leftDay = left
        self.rightDay = right
        # if there is a condition left & right should != None
        self.condition = condition
        self.calculation = calculation
        self.type_news = type_news
        self.type_decisions = type_decisions
        self.condition_text = text

        # TODO Features to be added - read the day data from a  file?
