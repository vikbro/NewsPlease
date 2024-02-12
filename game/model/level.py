from typing import Type, Callable, List

from game.model.news import News
from game.model.decision import Decision

import random
from game.dayTree import *
import copy


# LevelStates = {
#     "start_level": 0,
#     "level": 1,
#     "end_level": 2
# }


class Level:
    """
    Level class is where all the news/decisions/notes are generated by using the day class variables. Also calculate the
     result after the end of the day and writes it in the player class
    """

    def __init__(self, player: Type[Callable], game: Type[Callable], day: Callable = D1) -> None:
        self.grid = None
        self.game = game
        self.player = player
        self.current_day = day

        # self.current_state = "start_level"

        self.active = False

        self.one_time_expenses = []
        self.contiuous_expenses = []

        self.all_papers = []  # type: ignore

    # def next_state(self) -> None:
    #     """
    #     Method not used but has the same idea as next_state in Game class
    #     @return:
    #     """
    #     if self.current_state == "start_level":
    #         self.current_state == "level"
    #     if self.current_state == "level":
    #         self.current_state == "end_level"
    #     if self.current_state == "end_level":
    #         self.current_state == "start_level"

    def clear(self) -> None:
        """

        @todo fix not clean enough
        @return:
        """
        self.all_papers = []  # type: ignore
        self.grid = None

    def begin_day(self) -> None:
        # print(self.current_day.day_name)

        self.active = True
        self.all_papers = self.generate_news()

        if self.current_day.type_decisions is not type(None):
            self.all_papers = self.all_papers + self.generate_decisions()

    # right is true left is false;
    def next_day(self) -> None:
        # The all() function returns True if all items in an iterable are true, otherwise it returns False.
        # If the iterable object is empty, the all() function also returns True.
        if type(self.current_day.condition) is not type(None):
            if all([condition(self.player) for condition in self.current_day.condition]):
                self.player.day = self.current_day.rightDay.day_name
                # print(self.current_day.day_name)
            else:
                self.player.day = self.current_day.leftDay.day_name
                # print(self.current_day.day_name)
        #         This conditions could be written better
        else:
            self.player.day = self.current_day.leftDay.day_name
            # print(self.current_day.day_name)

        self.current_day = isinstance_map[self.player.day]

        # if CONDITIONS[self.current_day_name] != None:
        #     if CONDITIONS[self.current_day_name][0](self.player) == False:
        #         self.current_day_name = DAYS[self.current_day_name][1]
        #         print(self.current_day_name)
        #         return

        # self.current_day_name = DAYS[self.current_day_name][0]
        # print(self.current_day_name)

    def end_day(self):
        # print("end day")
        self.calculate_expense()
        self.calculate_result()
        self.next_day()
        self.clear()
        self.active = False
        # self.game.next_state()

    def calculate_expense(self):
        # one time expenses
        while len(self.one_time_expenses) is not 0:
            expense = self.one_time_expenses.pop()
            self.player.loyalty_score -= expense[0]
            self.player.money_score -= expense[1]
            self.player.readership_score -= expense[2]

        # continuous expences
        for expense in self.contiuous_expenses:
            self.player.loyalty_score -= expense[0]
            self.player.money_score -= expense[1]
            self.player.readership_score -= expense[2]

    def calculate_result(self):
        # print("calculating result")
        # make the changes to the news point

        news_list = [paper for paper in self.all_papers if type(paper) is News]
        if self.current_day.calculation != None:
            # print("entered none")
            for calculation in self.current_day.calculation:
                calculation(news_list)

        # add the changes to the player class
        for paper in self.all_papers:
            if paper.show == True:
                if paper.is_bad_print is not True:
                    self.player.loyalty_score += paper.loyalty_score
                    # print(self.player.loyalty_score)
                    self.player.money_score += paper.money_score
                    # print(self.player.money_score)
                    self.player.readership_score += paper.readership_score
                    # print(self.player.readership_score)

    # make news generator class
    # Random.shuffle the news articles

    def generate_news(self) -> List[Callable]:
        """
        Generate news based on what the Day class contains

        @return: List filled with the selected papers - has return for testing purposes
        """
        selected_news = []
        dict_copy = copy.deepcopy(NEWS)
        control_num = 0
        # Choose 1 weather paper and select remaining paper randomly
        for news_type in self.current_day.type_news:
            # i - not used?
            # How many news of this type to generate
            for i in range(0, news_type[1]):
                # if all news have been used
                # if all(NEWS[type[0]][-1]) == True:
                #         return selected_news
                # this is used to ensure that we don't get duplicates of the same news
                # TODO this doesn't work if all elements are True
                # print(dict_copy[news_type[0]])
                # allegedly while 1 should be faster than while True
                while 1:
                    if control_num > 20:
                        raise Exception(
                            "Somethings wrong with generating news.")
                    chosen_paper = random.choice(dict_copy[news_type[0]])
                    if chosen_paper[-1] == False:
                        break
                # chosen_paper = random.choice(NEWS[type[0]])
                chosen_paper[-1] = True
                # print("Chose" + chosen_paper[0])
                selected_news.append(
                    News(
                        news_type=news_type[0],
                        title=chosen_paper[0],
                        description=chosen_paper[1],
                        loyalty_score=chosen_paper[2],
                        money_score=chosen_paper[3],
                        readership_score=chosen_paper[4]
                    ))

        # If player allows colored papers then allow then generate the colored paper image
        for paper in selected_news:
            paper.is_colored = self.player.allow_coloured_articles

        # for paper in self.all_papers:
            # print("GENERATE" + paper.title)
        dict_copy = None
        return selected_news

    def generate_decisions(self) -> List:
        selected_decisions = []
        for type in self.current_day.type_decisions:
            for i in range(0, type[1]):  # How many paper of this type to generate
                # this is used to ensure that we don't get duplicates of the same paper
                # TODO this doesn't work if all elements are True
                # print(DECISIONS[type[0]])
                while 1:
                    # if control_num > 20:
                    #     raise Exception(
                    #         "Somethings wrong with generating paper.")
                    chosen_decision = random.choice(DECISIONS[type[0]])
                    if chosen_decision[-1] == False:
                        break
                # chosen_decision = random.choice(NEWS[type[0]])
                # raise flag used = True
                chosen_decision[-1] = True
                # print("Chose" + chosen_decision[0])
                selected_decisions.append(
                    Decision(
                        decision_type=type[0],
                        title=chosen_decision[0],
                        description=chosen_decision[1],
                        cost=chosen_decision[2],
                        consequences=chosen_decision[3],
                        player=self.player,
                        level=self)
                )

        return selected_decisions

    def update(self):
        pass