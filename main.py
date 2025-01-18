import math
import random
import os

dir_path = os.path.dirname(os.path.abspath(__file__))
class character:
    def __init__(self, name):
        self.name = name
        self.con_rank = "F"
        self.weapon_rank = "F"
        self.love_rank = "F"
        self.intellect_rank = "F"
stats = [
    character("Edmond"),
    character("Sekibanki")
    ]
class save:
    def __init__(self):
        self.actions = 0
        self.actions_max = 4
        self.day_counter = 0
        self.current_location = "Sekibanki's and Rin's Room"
        self.character_save = stats
empty = save()
state = save()

def box(text):
    boxSize = 120
    print(f'{"":-^{boxSize+2}}')
    rows = len(text)
    for x in range(0,rows):
        if not text[x]:
            continue
        columns = len(text[x])
        margin = boxSize//columns
        print("|",end="")
        for y in text[x]:
            y = str(y)
            print(f'{y: ^{margin}}',end="")
        print("|")
    print(f'{"":-^{boxSize+2}}')

def ask (lowRange,highRange):
    while True:
        try:
            result = int(input("Select:"))
        except:
            continue
        if lowRange <= result <= highRange:
            return result

def main_menu():
    while True:
        box([["Project Edmond"],["1. New Game"],["2. Quit"]])
        menu = ask(1,2)
        if menu == 1:
            play_menu()
        if menu == 2:
            break

def play_menu():
    while True:
        display()

def info():
    pass

def display():
    actions = ["Act","Plan","Stats"]
    box([[state.current_location,f"Focus left {state.actions}/{state.actions_max}",f"Day {state.day_counter}"],
        [""],
        ["------------------------------------------------------------------------------------------------------------------------"],
        [info()],
        ["------------------------------------------------------------------------------------------------------------------------"],
        [str(actions.index(x)+1)+ ". " + x for x in actions]])
    ask(1, len(actions))
    pass

    
main_menu()