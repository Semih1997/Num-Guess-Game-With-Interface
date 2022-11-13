from tkinter import *
from pc_functions import *

main_screen_geomerty = "400x500"
in_game_screen_geomerty = "300x400"
button_height = 5
button_width = 50

def with_pc_game():                         #Game with Pc Screen
    pc_game_screen = Tk
    pc_game_screen = Toplevel(number_game)
    pc_game_screen.title("Come Play")
    pc_game_screen.geometry(in_game_screen_geomerty)
    pc_game_screen.mainloop()
def multiplayer_game():                     #Game with Friend Screen
    multiplayer_game_screen = Tk
    multiplayer_game_screen = Toplevel(number_game)
    multiplayer_game_screen.title("!Have Fun!")
    multiplayer_game_screen.geometry(in_game_screen_geomerty)
    multiplayer_game_screen.mainloop()
def quiting():
    number_game.quit()
    
number_game = Tk()

number_game.title("Number Game")
number_game.geometry(main_screen_geomerty)

pc_button = Button(number_game,
                           text = "Play with PC",
                           height = button_height,
                           width= button_width,
                           command = with_pc_game)
pc_button.pack(pady = 15)
multip_button = Button(number_game,
                              height = button_height,
                              width = button_width,
                              text = "Play Multiplayer",
                              command = multiplayer_game)
multip_button.pack(pady = 50)
quit_button = Button(number_game,
                              height = 3,
                              width = 25,                              
                              text = "QUIT",
                              command = quiting)
quit_button.pack(pady = 30 , side = "bottom")
number_game.mainloop()