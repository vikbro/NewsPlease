import json
import os.path


class Player:
    """
    Player class handles all the variables that the player has when through the story.
    Perhaps this class is useless and all it's data could be compessed in a dictionry with save load functions
    """

    def __init__(self) -> None:
        """
        Player handles the score of the player and also all the perks

        :param loyalty_score: loyalty 
        :param money_score: money
        :param readership_score: readers

        """
        self.loyalty_score = 0
        self.money_score = 0
        self.readership_score = 0
        self.day = "D1"  # first name globals()["day_name"]
        self.allow_small_news = True

        # Features to be added - read from file?
        # Upgrades
        self.grid_dimentions = (5, 3)

        self.show_loyalty = True
        self.show_money = True
        self.show_readership = True

        self.allow_pause = False
        self.allow_medium_news = False
        self.allow_large_news = False
        self.allow_coloured_articles = False

        self.allow_clock = False
        self.work_hours = 12

        # Story line driven variables
        self.has_changed_regime = False

        self.has_rebellion_connection = False
        self.is_reblious = False
        self.has_donated_rebellion = False
        self.has_donated_party = False
        self.has_rebelion_records_cleaned = False
        self.has_party_records_removed = False

        self.user_values = {}

    def save(self) -> None:
        """
        Updates the values in the dictionary and then writes them in the player_values.json file

        @return:
        """
        self.update_values()

        with open("player_values.json", 'w', encoding="UTF-16") as outfile:
            outfile.write(json.dumps(self.user_values, indent=4))

    def reset_values(self) -> None:
        """
        resets the values of the Player class to the beginning values
        """
        self.loyalty_score = 0
        self.money_score = 0
        self.readership_score = 0
        self.day = "D1"  # first name globals()["day_name"]

        # Features to be added - read from file?
        self.grid_dimentions = (5, 3)

        self.show_loyalty = False
        self.show_money = False
        self.show_readership = False

        self.allow_pause = False
        self.allow_small_news = True
        self.allow_medium_news = False
        self.allow_large_news = False
        self.allow_coloured_articles = False

        self.allow_clock = False
        self.work_hours = 12

        # Story line driven variables
        self.has_changed_regime = False

        self.has_rebellion_connection = False
        self.is_reblious = False
        self.has_donated_rebellion = False
        self.has_donated_party = False
        self.has_rebelion_records_cleaned = False
        self.has_party_records_removed = False

        # self.user_values = {}

    def load(self) -> None:
        """
        Load from player_json file and overrides the values of the Player class
        @return:
        """
        if os.path.exists("player_values.json"):
            # Gets the user values at the start of the program
            # or creates the file if it doesnt't exist.
            with open('player_values.json', 'r', encoding="UTF-16") as openfile:
                self.user_values = json.load(openfile)
            self.update_class()
        else:
            self.reset_values()
            self.update_values()
            self.save()

    def update_values(self) -> None:
        """
        Update the values in the user_avlues dictionary from the Player class variables
        @return:
        """
        # essential variables
        self.user_values["loyalty_score"] = self.loyalty_score
        self.user_values["money_score"] = self.money_score
        self.user_values["readership_score"] = self.readership_score
        self.user_values["day"] = self.day
        self.user_values["allow_small_news"] = self.allow_small_news

        # Upgrades
        self.user_values["grid_dimentions"] = self.grid_dimentions
        self.user_values["show_loyalty"] = self.show_loyalty
        self.user_values["show_money"] = self.show_money
        self.user_values["show_readership"] = self.show_readership
        self.user_values["allow_pause"] = self.allow_pause
        self.user_values["allow_medium_news"] = self.allow_medium_news
        self.user_values["allow_large_news"] = self.allow_large_news
        self.user_values["allow_coloured_articles"] = self.allow_coloured_articles
        self.user_values["allow_clock"] = self.allow_clock

        # Story driven variables
        self.user_values["work_hours"] = self.work_hours
        self.user_values["has_changed_regime"] = self.has_changed_regime
        self.user_values["has_rebellion_connection"] = self.has_rebellion_connection
        self.user_values["is_reblious"] = self.is_reblious
        self.user_values["has_donated_rebellion"] = self.has_donated_rebellion
        self.user_values["has_donated_party"] = self.has_donated_party
        self.user_values["has_rebelion_records_cleaned"] = self.has_rebelion_records_cleaned
        self.user_values["has_party_records_removed"] = self.has_party_records_removed

    def update_class(self) -> None:
        """
        Update the values in the Player class variables from the user_values dictionary

        @return:
        """
        # Essential
        self.loyalty_score = self.user_values["loyalty_score"]
        self.money_score = self.user_values["money_score"]
        self.readership_score = self.user_values["readership_score"]
        self.day = self.user_values["day"]

        # Upgrades
        self.grid_dimentions = self.user_values["grid_dimentions"]
        self.show_loyalty = self.user_values["show_loyalty"]
        self.show_money = self.user_values["show_money"]
        self.show_readership = self.user_values["show_readership"]

        self.allow_pause = self.user_values["allow_pause"]
        self.allow_small_news = self.user_values["allow_small_news"]
        self.allow_medium_news = self.user_values["allow_medium_news"]
        self.allow_large_news = self.user_values["allow_large_news"]
        self.allow_coloured_articles = self.user_values["allow_coloured_articles"]
        self.allow_clock = self.user_values["allow_clock"]
        self.work_hours = self.user_values["work_hours"]

        # Story driven variables
        self.has_changed_regime = self.user_values["has_changed_regime"]

        self.has_rebellion_connection = self.user_values["has_rebellion_connection"]
        self.is_reblious = self.user_values["is_reblious"]
        self.has_donated_rebellion = self.user_values["has_donated_rebellion"]
        self.has_donated_party = self.user_values["has_donated_party"]
        self.has_rebelion_records_cleaned = self.user_values["has_rebelion_records_cleaned"]
        self.has_party_records_removed = self.user_values["has_party_records_removed"]

    def print_player(self) -> None:
        """
        Print user_values
        @return:
        """
        for key, value in self.user_values.items():
            print(key, value)

    def print_class(self):
        """
        Print class variables
        @return:
        """
        print("===========")
        
        print(f"self.loyalty_score = {self.loyalty_score}")
        print(f"self.money_score = {self.money_score}")
        print(f"self.readership_score = {self.readership_score}")
        print(f"self.day = {self.day}")
        print(f"self.grid_dimentions = {self.grid_dimentions}")
        print(f"self.show_loyalty = {self.show_loyalty}")
        print(f"self.show_money = {self.show_money}")
        print(f"self.show_readership = {self.show_readership}")
        print(f"self.allow_pause = {self.allow_pause}")
        print(f"self.allow_small_news = {self.allow_small_news}")
        print(f"self.allow_medium_news = {self.allow_medium_news}")
        print(f"self.allow_large_news = {self.allow_large_news}")
        print(f"self.allow_coloured_articles = {self.allow_coloured_articles}")
        print(f"self.allow_clock = {self.allow_clock}")
        print(f"self.work_hours = {self.work_hours}")
        print(f"self.has_changed_regime = {self.has_changed_regime}")
        print(f"self.has_rebellion_connection = {self.has_rebellion_connection}")
        print(f"self.is_reblious = {self.is_reblious}")
        print(f"self.has_donated_rebellion = {self.has_donated_rebellion}")
        print(f"self.has_donated_party = {self.has_donated_party}")
        print(f"self.has_rebelion_records_cleaned = {self.has_rebelion_records_cleaned}")
        print(f"self.has_party_records_removed = {self.has_party_records_removed}")
        
        print("===========")

# pl = Player()
# # pl.save()
# pl.load()
# pl.print_player()
# pl.print_class()
