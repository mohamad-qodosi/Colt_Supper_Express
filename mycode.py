def show_rail(player_list: list, rail: list) -> None:
    for i, value in enumerate(rail):
        if i == 0:
            box_name = "locomotive"
        elif i == n - 1:
            box_name = "empty"
        else:
            box_name = f"vagon{i}"
        for i, color in enumerate(value):
            for player in player_list:
                if player[1] == color:
                    my_player = player
                    break
            value[i] = f"{box_name}= {color} dir:{my_player[2]} up-down:{my_player[3]} dead-alive{my_player[4]}"
    for item in rail:
        print(item)

def get_player_vagon(rail, color):
    for i in range(len(rail)):
        if color in rail[i]:
            return i

def initialize(colors: list, names: list) -> list:
    import random
    n = len(colors)
    my_colors = colors.copy()
    rail = [[], []]
    for i in range(n):
        item = random.choice(my_colors)
        my_colors.remove(item)
        rail.insert(1, [item])
    player_list = [[names[i], colors[i], '', 'up', 'alive'] for i in range(n)]
    for i, player in enumerate(player_list):
        color = player[1]
        index = get_player_vagon(rail, color)
        if index <= n // 2:
            player[2] = 'right'
        else:
            player[2] = 'left'
    return (player_list, rail)

