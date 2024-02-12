from game.model.level import Level
from game.model.player import Player
from game.model.day import Day


def test_generator():
    """
    Get random sort of news
    @return:
    """
    # Arrange
    # pygame.init()
    # pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    player = Player()
    day = Day(None, None, None, None, [
        ("WEATHER", 1), ("POLITICS", 2), ("AD", 2)], None)

    level = Level(player, None, day)

    # Act
    selected_news = level.generate_news()

    # Assert?
    assert (len(selected_news) == 5)
    assert (len([news for news in selected_news if news.news_type == "WEATHER"]) == 1)
    assert (len([news for news in selected_news if news.news_type == "POLITICS"]) == 2)
    assert (len([news for news in selected_news if news.news_type == "AD"]) == 2)


def test_generator_min_ads():
    """
    Get the minimum amount of ads
    @return:
    """
    # Arrange
    player = Player()
    day = Day(None, None, None, None, [
        ("AD", 1)], None)

    level = Level(player, None, day)
    # Act
    selected_news = level.generate_news()

    # Assert
    assert (all(news.news_type == "AD" for news in selected_news))
    assert (len(selected_news) == 1)


def test_generator_max_ad():
    """
    Get the max amount of ads
    @return:
    """
    # Arrange

    player = Player()
    day = Day(None, None, None, None, [
        ("AD", 5)], None)

    level = Level(player, None, day)
    # Act
    selected_news = level.generate_news()

    # Assert
    assert (all(news.news_type == "AD" for news in selected_news))
    assert (len(selected_news) == 5)


def test_generator_min_politics():
    # Arrange
    player = Player()
    day = Day(None, None, None, None, [
        ("POLITICS", 1)], None)

    level = Level(player, None, day)
    # Act
    selected_news = level.generate_news()

    # Assert
    assert (all(news.news_type == "POLITICS" for news in selected_news))
    assert (len(selected_news) == 1)


def test_generator_max_politics():
    # Arrange
    player = Player()
    day = Day(None, None, None, None, [
        ("POLITICS", 5)], None)

    level = Level(player, None, day)
    # Act
    selected_news = level.generate_news()

    # Assert
    assert (all(news.news_type == "POLITICS" for news in selected_news))
    assert (len(selected_news) == 5)


def test_generator_min_weather():
    # Arrange
    player = Player()
    day = Day(None, None, None, None, [
        ("WEATHER", 1)], None)

    level = Level(player, None, day)
    # Act
    selected_news = level.generate_news()

    # Assert
    assert (all(news.news_type == "WEATHER" for news in selected_news))
    assert (len(selected_news) == 1)


def test_generator_max_weather():
    # Arrange
    player = Player()
    day = Day(None, None, None, None, [
        ("WEATHER", 5)], None)

    level = Level(player, None, day)
    # Act
    selected_news = level.generate_news()

    # Assert
    assert (all(news.news_type == "WEATHER" for news in selected_news))
    assert (len(selected_news) == 5)
