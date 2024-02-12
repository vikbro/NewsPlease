from game.model.day import Day


# conditions
# conditions restricted by the player class


def loyalty_above_ten(player): return player.loyalty_score > 10


def loyalty_above_twenty(player): return player.loyalty_score > 20


def loyalty_above_forty(player): return player.loyalty_score > 40


def money_above_ten(player): return player.money_score > 10


def money_above_twenty(player): return player.money_score > 20


def money_above_forty(player): return player.money_score > 40


def readership_above_ten(player): return player.readership_score > 10


def readership_above_twenty(player): return player.readership_score > 20


def readership_above_forty(player): return player.readership_score > 40


# Calculation enchancment


def encourage_weather(news):
    for new in news:
        if new.news_type == "WEATHER":
            new.loyalty_score += 2
            new.money_score += 2
            new.readership_score += 2


def encourage_politics(news):
    for new in news:
        if new.news_type == "POLITICS":
            new.loyalty_score += 2
            new.money_score += 2
            new.readership_score += 2


def encourage_ads(news):
    for new in news:
        if new.news_type == "AD":
            new.loyalty_score += 2
            new.money_score += 2
            new.readership_score += 2


def size_matters(news):
    m_coefficient = 2
    l_coefficient = 2
    for new in news:
        if new.is_large:
            new.loyalty_score = int(new.loyalty_score * l_coefficient)
            new.money_score = int(new.money_score * l_coefficient)
            new.readership_score = int(new.readership_score * l_coefficient)
        elif new.is_medium:
            new.loyalty_score = int(new.loyalty_score * m_coefficient)
            new.money_score = int(new.money_score * m_coefficient)
            new.readership_score = int(new.readership_score * m_coefficient)


def colour_matters(news):
    l_coefficient = 2
    for new in news:
        if new.is_large:
            new.loyalty_score = int(new.loyalty_score * l_coefficient)
            new.money_score = int(new.money_score * l_coefficient)
            new.readership_score = int(new.readership_score * l_coefficient)


# Consequences


def show_loyalty(player): player.show_loyalty = True


def show_money(player): player.show_money = True


def show_readership(player): player.show_readership = True


def allow_medium_news(player): player.allow_medium_news = True


def allow_large_news(player): player.allow_large_news = True


def allow_coloured_articles(player): player.allow_coloured_articles = True


def allow_clock(player): player.allow_clock = True


def allow_pause(player): player.allow_pause = True


def work_hours_ten(player): player.work_hours = 10


def work_hours_eight(player): player.work_hours = 8


def work_hours_six(player): player.work_hours = 6


def has_rebellion_connection(player): player.has_rebellion_connection = True


def has_changed_regime(player): player.has_rebellion_connection = True


def has_donated_rebellion(player): player.has_donated_rebellion = True


def has_donated_party(player): player.has_donated_party = True


def chose_rebellion(player): player.is_reblious = True


def enlarge_paper(player):
    player.grid_dimentions[0] += 1
    player.grid_dimentions[1] += 1


def has_rebelion_records_cleaned(player):
    player.has_rebelion_records_cleaned = True
    player.has_rebellion_connection = False
    player.is_reblious = False
    player.has_donated_rebellion = False


def has_party_records_removed(player):
    player.has_party_records_removed = True
    player.has_donated_party = False


# endings
END4 = Day(None, None, None, None, None, None,
           "You have done glourious work! End 4", "END4")
END3 = Day(None, None, None, None, None, None, "YOU HAVE FAILED 3", "END3")
END2 = Day(None, None, None, None, None, None, "YOU HAVE FAILED 2", "END2")
END1 = Day(None, None, None, None, None, None,
           "You are done. Fired. Do not show your face at the newspaper again \n End 1", "END1")

# day5
DRR5 = Day(END4, None, None, None, [
    ("WEATHER", 4), ("POLITICS", 4), ("AD", 4)], [("ONCE", 1), ("CONTINUOUS", 1)], "", "DRR5")
DRL5 = Day(END3, None, None, None, [
    ("WEATHER", 4), ("POLITICS", 4), ("AD", 4)], [("ONCE", 1), ("CONTINUOUS", 1)], "", "DRL5")

# day4
DR4 = Day(DRL5, DRR5, [readership_above_forty, loyalty_above_forty], None, [("POLITICS", 2)], [("ONCE", 1)],
          "Get loyalty above 40\nGet readership above 40", "DR4")
DLL4 = Day(END1, None, None, None, [
    ("WEATHER", 4), ("POLITICS", 4), ("AD", 4)], [("ONCE", 1), ("CONTINUOUS", 1)], "No tasks", "DLL4")
DLR4 = Day(END2, None, None, None, [
    ("WEATHER", 4), ("POLITICS", 4), ("AD", 4)], [("ONCE", 1), ("CONTINUOUS", 1)], "No task", "DLR4")

# day3
DL3 = Day(DLL4, DLR4, [readership_above_forty, loyalty_above_twenty],
          None, [
              ("WEATHER", 3), ("POLITICS", 3), ("AD", 3)], [("ONCE", 1), ("CONTINUOUS", 1)],
          "Get loyalty above 20\nGet readership above 40", "DL3")
DR3 = Day(DR4, None, None, None, [
    ("WEATHER", 3), ("POLITICS", 3), ("AD", 3)], [("ONCE", 1), ("CONTINUOUS", 1)], "Get loyalty above 20\nGet readership above 40", "DR3")

# day2
DR2 = Day(DR3, None, None, [size_matters], [
    ("WEATHER", 2), ("POLITICS", 2), ("AD", 2)], [("ONCE", 1), ("CONTINUOUS", 1)], "People prefer larger news", "DR2")
DL2 = Day(DL3, None, None, [size_matters], [
    ("WEATHER", 2), ("POLITICS", 2), ("AD", 2)], [("ONCE", 1), ("CONTINUOUS", 1)], "People prefer larger news", "DL2")

# day1
D1 = Day(DL2, DR2, [loyalty_above_ten], None, [
    ("WEATHER", 1), ("AD", 1), ("POLITICS", 1)], [("ONCE", 1), ("CONTINUOUS", 1)],
    "Get loyalty above 10", "D1")

# Not sure if this is the best solution to loading the day from the save file
isinstance_map = {
    "D1": D1,
    "DL2": DL2,
    "DR2": DR2,
    "DR3": DR3,
    "DL3": DL3,
    "DLR4": DLR4,
    "DR4": DR4,
    "DLL4": DLL4,
    "DRL5": DRL5,
    "DRR5": DRR5,
    "END1": END1,
    "END2": END2,
    "END3": END3,
    "END4": END4,
}

# could put the conditions next to the children?
# rigth is true left is false

# DAYS = {
#     "D1": ["DL2", "DR2"],
#     "DL2": ["DL3"],
#     "DR2": ["DR3"],
#     "DL3": ["DLL4", "DLR4"],
#     "DR3": ["DR4"],
#     "DLL4": [None],
#     "DLR4": [None],
#     "DR4": ["DRL5", "DRR5"],
#     "DRL5": [None],
#     "DRR5": ["DR3"]
# }

# CONDITIONS = {
#     "D1": (lambda player: player.readershipScore > 10, "Get the READERSHIP up to 10"),
#     "DL2": None,
#     "DR2": None,
#     "DL3": (lambda player: player.loyaltyPoints > 50, "Get the LOYALTY up to 50"),
#     "DR3": None,
#     "DLL4": None,
#     "DLR4": None,
#     "DR4": (lambda player: player.readershipScore > 10 and player.loyaltyPoints > 50, "Get the READERSHIP up to 10 and LOYALTY up to 50"),
#     "DRL5": None,
#     "DRR5": None,
# }

# CALCULATIONS = {
#     # "D1" : (lambda news: map( news.readership_score += 10 if news.type == "WEATHER" else news.readership_score ,news),"Get the READERSHIP up to 10") ,
#     "D1" : (lambda news: map(news.readership_score = news.readership_score + 1,news),"Get the READERSHIP up to 10"),
#     "DL2" : None,
#     "DR2" : None,
#     "DL3" : (lambda player: player.loyaltyPoints > 50,"Get the LOYALTY up to 50") ,
#     "DR3" : None,
#     "DLL4" : None ,
#     "DLR4" : None ,
#     "DR4" : (lambda player: player.readershipScore > 10 and player.loyaltyPoints > 50,"Get the READERSHIP up to 10 and LOYALTY up to 50") ,
#     "DRL5" : None,
#     "DRR5" : None
# }

###################################################
# NEWS
###################################################

NEWS = {
    "WEATHER": [
        ["Storm ahead!", "Our top scientist warn of a big storm comming tommorow", 4, 0, 8, False],
        ["Sunny Day!", "The sun shall shine bright on this glorious day!", 2, 0, 5, False],
        ["Sunny!", "The WA Institute has ordered for great weather!", 4, 0, 6, False],
        ["Rain!", "The WA Institute has ordered for rain!", 5, 0, 7, False],
        ["HEAT!", "Hide, unexpected heat wave incoming!", 2, 0, 7, False],
        ["FREEZING!", "Hide, unexpected cold wave incoming!", 2, 0, 7, False]
    ],
    "POLITICS": [
        ["GREAT SUCCESS!", "Our leader has struck a deal for more exporting of wool!", 6, 0, 8, False],
        ["GOOD NEWS!", "More chocolate in the future!", 5, 0, 9, False],
        ["GREAT SUCCESS!!!!!",
         "We have even more reasons to believe in our system!", 8, 0, 8, False],
        ["BAD CHOISE", "A town comitie has chosen wrong and now is being punished.", 9, 0, 10, False],
        ["RESULTS", "Our plans are successfull - CC says ", 6, 0, 8, False],
        ["BAD NEWS", "LESS CHOCOLATE IN THE FUTURE", -6, 0, 11, False],
        ["HORRIBLE NEWS", "THE COMITTIE IS CORRUPT!", -10, 0, 15, False],
        ["ENOUGH!,", "GOLDSTEIN WAS RIGHT!", -10, 0, 16, False]
    ],
    "AD": [
        ["BREAD", "Get the all new formula BREAD!", -1, 3, 6, False],
        ["MILK", "Get the all new formula MILK!", -1, 2, 5, False],
        ["SOAP", "If you are a clean person, USE SOAP", -1, 3, 6, False],
        ["PERFUMÈ", "If you are an even cleaner person, USE PERFUMÈ", -1, 6, 4, False],
        ["HIIO", "The water for those with TASTÈ", -1, 7, 3, False]
    ],
    "LEASURE": [
        [],
        []
    ],
    "WAR": [
        [],
        []
    ],
    "SPORT": [
        ["SECOND PLACE!"]
    ],
    "SPECIAL": [
        ["MAKE WAY", "Forest to be chopped for more news papers", 3, 0, 8, False],
        [""]
    ],
    "TEST":[
        ["TEST", "Test test", 5, 5, 5, False],
    ]

}

###################################################
# DECISIONS
###################################################

# seperate into uprgades and decisions
DECISIONS = {
    "ONCE": [
        ["Loyalty information",
         "The Ministry of Information has allowed you to be informed about loyalty. Get the loyalty meter", (
             0, 20, 0),
         [show_loyalty], False],
        ["Readership information",
         "The Ministry of Information has allowed you to be informed about readership. Get the readership meter",
         (0, 30, 0), [show_readership], False],
        ["Financial information",
         "The Ministry of Information has allowed you to be informed about finances. Get the finance meter", (
             0, 30, 0),
         [show_money], False],
        ["Times up!", "The Ministry of Labour has allowed the presence of a clock.",
         (0, 20, 0), [allow_clock], False],
        ["YOU DO NOT DECIDE!",
         "The M.I. has decided that the decision is not for you to decide", (0, 0, 0), [], False],
        ["What do you do?",
         "I work for the goverment- agree, I work for the people - disagree", (-10, 0, 0), [chose_rebellion], False]
    ],
    "CONTINUOUS": [
        ["Colored print!", "The ministy of information has researched color printing machines.",
         (0, 90, 0), [allow_coloured_articles], False],
        ["Break time",
         "The Ministry of Labour has allowed the ability to take a break. You need to pay every time you take a break.",
         (0, 10, 0), [allow_pause], False],
        ["BIG NEWS", "The Ministry of Information has researched big printing machines. You can print big news",
         (0, 80, 0), [allow_large_news], False],
        ["Medium News", "The Ministry of Information has researched medium printing machines.",
         (0, 50, 0), [allow_medium_news], False],
        ["More news!", "The Ministry of Information has researched bigger paper.",
         (0, 80, 0), [enlarge_paper], False]
    ],
    "STORY": [
        # Dear editor we are trying to establisha  connection with you! Please respond if you are intrested.
        ["Connection", "Hello ######, WE ### ###### ## ESTABLISH CONNECTION! ###### RESPOND IF ### ### INTERESTED!",
         False],
        ["GO UP", "hello editor, get the viewership ##. Resistance wants to spread ### #### around", False],
        ["WHAT WAR", "##### editor, prove your loyalty to the resistance. Sabotage the M.W. Show the real war", False],
        ["Democracy!", ""]
    ]
}

###################################################
# NOTES
###################################################

NOTES = {
    "TUTORIAL": [
        ["WELCOME",
         "Hello editor, to decide what articles to be printed, you need to drag the envelopes away from your work desk and click on the buttons to decide what size of the print you want.",
         False],
        ["Break downs",
         "Sometimes the printing machines malfunction, bear that in mind since in lowers your income and readers arent fond of this breakdowns"],

    ]
}
