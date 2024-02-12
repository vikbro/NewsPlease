from game.model.level import Level
from game.model.player import Player
from game.model.day import Day



def test_generate_min_once():
    """
    Get random sort of news
    @return:
    """
    # Arrange

    player = Player()
    day = Day(None, None, None, None, None,
              [("ONCE", 1)])

    level = Level(player, None, day)

    # Act
    #All papers contain notes/news/decisions
    selected_news = level.generate_decisions()

    # Assert?
    assert (len([news for news in selected_news if news.decision_type == "ONCE"]) == 1)

def test_generate_min_continuous():
    """
    Get random sort of news
    @return:
    """
    # Arrange

    player = Player()
    day = Day(None, None, None, None, None,
              [("CONTINUOUS", 1)])

    level = Level(player, None, day)

    # Act
    #All papers contain notes/news/decisions
    selected_news = level.generate_decisions()

    # Assert?
    assert (len([news for news in selected_news if news.decision_type == "CONTINUOUS"]) == 1)
