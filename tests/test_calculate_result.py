from game.model.level import Level
from game.model.player import Player
from game.model.day import Day


def test_calulate_result():
    """
    Check if calculate_result works
    @return:
    """
    # Arrange

    player = Player()
    day = Day(None, None, None, None, [("TEST", 1)],
              [])

    level = Level(player, None, day)

    # Act
    # All papers contain notes/news/decisions
    level.all_papers = level.generate_news()
    # make all news visible
    for paper in level.all_papers:
        paper.show = True

    level.calculate_result()

    # Assert?
    assert (player.loyalty_score == 5)
    assert (player.money_score == 5)
    assert (player.readership_score == 5)


# def test_calculate_expense():
#     """
#     Check if calculate_expense works
#     @return:
#     """
#     # Arrange
#
#     player = Player()
#     day = Day(None, None, None, None, None,
#               [("Test", 1)])
#
#     level = Level(player, None, day)
#
#     # Act
#     # All papers contain notes/news/decisions
#     level.all_papers = level.generate_news()
#     # make all news visible
#     for paper in level.all_papers:
#         paper.show = True
#
#     level.calculate_result()
#
#     # Assert?
#     assert (player.loyalty_score == 5)
#     assert (player.money_score == 5)
#     assert (player.readership_score == 5)
