from multiprocessing.resource_sharer import stop
import tkinter
from tkinter import Place, Toplevel, messagebox
from pc_functions import *

def with_pc_game():                         #Game with Pc Screen
    pc_game_screen = tkinter.Tk
    pc_game_screen = Toplevel(number_game)
    pc_game_screen.title("Come Play")
    pc_game_screen.geometry("300x400")
    pc_game_screen.mainloop()
def multiplayer_game():                     #Game with Friend Screen
    multiplayer_game_screen = tkinter.Tk
    multiplayer_game_screen = Toplevel(number_game)
    multiplayer_game_screen.title("Have Fun With Your Friend")
    multiplayer_game_screen.geometry("300x400")
    multiplayer_game_screen.mainloop()
def quiting():
    number_game.quit()
    
number_game = tkinter.Tk()

number_game.title("Number Game")
number_game.geometry("400x500")

pc_button = tkinter.Button(number_game,
                           text = "Play with PC",
                           height = 5,
                           width= 50,
                           command = with_pc_game)
pc_button.pack(pady = 15)
multip_button =tkinter.Button(number_game,
                              height = 5,
                              width = 50,
                              text = "Play Multiplayer",
                              command = multiplayer_game)
multip_button.pack(pady = 50)
quit_button =tkinter.Button(number_game,
                              height = 3,
                              width = 25,                              
                              text = "QUIT",
                              command = quiting)
quit_button.pack(pady = 30 , side = "bottom")
number_game.mainloop()