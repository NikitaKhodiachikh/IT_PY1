list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

# TODO Разделите участников на две команды
number_player = len(list_players) // 2
first_team = list_players[:number_player]
second_team = list_players[number_player:]
print(first_team)
print(second_team)
