from typing import List, Optional


class News:
    """
    News class contains all the news data most importantly loyalty,money,readership values
    """

    def __init__(self, news_type: str, title: str, description: str, loyalty_score: float = 0, money_score: float = 0,
                 readership_score: float = 0) -> None:
        self.news_type = news_type

        self.title = title
        self.description = description

        self.active = False
        # if news whould be calculated in the result
        self.show = False

        self.loyalty_score = loyalty_score
        self.money_score = money_score
        self.readership_score = readership_score

        # Decision & story driven variables
        self.is_small = False
        self.is_medium = False
        self.is_large = False

        self.is_colored = False

        self.is_bad_print = False
        self.blurry_image = False

        self.has_invisable_ink = False

    def create_s(self) -> None:
        """
        Create small news article
        @return:
        """
        self.show = True
        self.is_small = True

    def create_m(self) -> None:
        """
        Create medium news article
        @return:
        """
        self.show = True
        self.is_medium = True

    def create_l(self) -> None:
        """
        Create large news article
        @return:
        """
        self.show = True
        self.is_large = True

    def clear(self) -> None:
        """
        Clear the varibles that are used while news is visible
        @return:
        """
        self.show = False
        self.is_small = False
        self.is_medium = False
        self.is_large = False

    def update(self):
        pass
