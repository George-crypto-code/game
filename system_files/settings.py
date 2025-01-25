import tkinter as tk

# size of window
root = tk.Tk()
WIGHT_OF_SCREEN = root.winfo_screenwidth()
HEIGHT_OF_SCREEN = root.winfo_screenheight()
root.destroy()

# fps
FPS = 60

# player settings
PLAYER_SPEED = 2
WIGHT_OF_PLAYER = WIGHT_OF_SCREEN / 16
HEIGHT_OF_PLAYER = WIGHT_OF_SCREEN / 16
PLAYER_ANGLE = 0
PLAYER_MAX_HEALTH = 4

# enemy settings
ENEMY_SPEED = 1
WIGHT_OF_ENEMY = WIGHT_OF_SCREEN / 16
HEIGHT_OF_ENEMY = WIGHT_OF_SCREEN / 16
ENEMY_ANGLE = 0
ENEMY_MAX_HEALTH = 3

# map setting
WIGHT_OF_MAP = WIGHT_OF_SCREEN
HEIGHT_OF_MAP = HEIGHT_OF_SCREEN

# box settings
WIGHT_OF_BOX = WIGHT_OF_SCREEN / 16
HEIGHT_OF_BOX = WIGHT_OF_SCREEN / 16

# aim settings
WIGHT_OF_AIM = WIGHT_OF_SCREEN / 40
HEIGHT_OF_AIM = WIGHT_OF_SCREEN / 40


# loud of game
def update_loud_of_game():
    with open(r"system_files\sound_effect_loud.txt") as loud:
        return float(loud.readline())
