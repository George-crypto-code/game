# size of window
WIGHT_OF_SCREEN = 800
HEIGHT_OF_SCREEN = 600

# fps
FPS = 60

# player settings
PLAYER_SPEED = 1
WIGHT_OF_PLAYER = 50
HEIGHT_OF_PLAYER = 50
PLAYER_ANGLE = 0
PLAYER_MAX_HEALTH = 4

# enemy settings
ENEMY_SPEED = 1
WIGHT_OF_ENEMY = 50
HEIGHT_OF_ENEMY = 50
ENEMY_ANGLE = 0
ENEMY_MAX_HEALTH = 3

# map setting
WIGHT_OF_MAP = 800
HEIGHT_OF_MAP = 600

# box settings
WIGHT_OF_BOX = 50
HEIGHT_OF_BOX = 50

# aim settings
WIGHT_OF_AIM = 20
HEIGHT_OF_AIM = 20


# loud of game
def update_loud_of_game():
    with open(r"system_files\sound_effect_loud.txt") as loud:
        return float(loud.readline())
