import math
import random
import time
import os
# import string

pause = 0.2
endTurnPause = 0.8
dir_path = os.path.dirname(os.path.abspath(__file__))
save = 0

# User Interface
def box(text):
    # boxSize = os.get_terminal_size().columns - 2
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

def percentage(part, whole, size):
    return size * float(part) / float(whole)

def healthbar(HP,maxHP,size):
    if maxHP <= size:
        bar = ('|'*HP)
        result = (f'[{bar: <{maxHP}}]')
    elif maxHP > size:
        percent = math.ceil(percentage(HP,maxHP,size))
        bar = ('|'*percent)
        result = (f'[{bar: <{size}}]')
    return result

def ask (lowRange,highRange):
    while True:
        try:
            result = int(input("Choose a number: "))
        except:
            continue
        if lowRange <= result <= highRange:
            return result
        
def askList (numberList):
    while True:
        try:
            result = int(input("Choose a number: "))
        except:
            continue
        if result in numberList:
            return result

def garble(s, prob=0.5):
    # Create a list of garbled characters | string.ascii_letters
    garbled_chars = [random.choice([" "]) if random.random() < prob else c for c in s]

    # Join the garbled characters back into a string
    garbled_s = ''.join(garbled_chars)
    
    return garbled_s

def startStory (file):
    # Need to add a way to use the bax function.
    x = open(f"{dir_path}/txt/story/{file}.txt","r",encoding='utf-8')
    y = x.readlines()
    for z in y:
        z = z.replace("\n","")
        if z == "WIP":
            return
        print(z, end='')
        a = input(" ")
        if a == "skip":
            return
        if a == "menu":
            return "menu"

# Save Data
def newSave():
    txt_dir = os.path.join(dir_path, "txt", "save")

    if not os.path.exists(txt_dir):
        os.makedirs(txt_dir)

    # Get a list of all the txt files in the directory
    txt_files = [f for f in os.listdir(txt_dir) if f.endswith('.txt')]

    # If there are no txt files, create a new file with name '0.txt'
    if not txt_files:
        filename = os.path.join(txt_dir, '0.txt')
    else:
        # Otherwise, get the highest numbered file and add 1 to it
        max_num = max([int(f[:-4]) for f in txt_files])
        filename = os.path.join(txt_dir, f"{max_num+1}.txt")

    # Create the new file with the calculated name
    with open(filename, 'w') as f:
        f.write('0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')

    # Extract the number from the filename and return it
    file_number = int(os.path.splitext(os.path.basename(filename))[0])
    return file_number

def readSave(position):
    txt_dir = os.path.join(dir_path, "txt", "save")
    filename = os.path.join(txt_dir, f"{save}.txt")

    if not os.path.exists(filename):
        raise ValueError(f"File {filename} does not exist")

    with open(filename, 'r') as f:
        content = f.read()

    try:
        value = int(content[position])
    except (ValueError, IndexError):
        raise ValueError(f"Invalid position {position} for file {filename}")

    return value

def updateSave(position):
    txt_dir = os.path.join(dir_path, "txt", "save")
    filename = os.path.join(txt_dir, f"{save}.txt")

    if not os.path.exists(filename):
        raise ValueError(f"File {filename} does not exist")

    with open(filename, 'r') as f:
        content = list(f.read())

    # Check if the position is valid
    if position >= len(content):
        raise ValueError(f"Invalid position {position} for file {filename}")

    # Update the content at the specified position
    if content[position] == '0':
        content[position] = '1'
    else:
        content[position] = '0'

    # Write the updated content back to the file
    with open(filename, 'w') as f:
        f.write(''.join(content))

def listSaveFiles():
    txt_dir = os.path.join(dir_path, "txt", "save")
    
    if not os.path.exists(txt_dir):
        return []
    
    # Get a list of all the txt files in the directory
    txt_files = [f for f in os.listdir(txt_dir) if f.endswith('.txt')]

    # Extract the number from the filename for each txt file
    file_numbers = [int(os.path.splitext(f)[0]) for f in txt_files]

    # Sort the file numbers in ascending order
    file_numbers.sort()

    # Check for gaps in the file numbers and add them to the list
    save_files = []
    last_num = -1
    for num in file_numbers:
        if num != last_num + 1:
            for missing_num in range(last_num + 1, num):
                save_files.append(missing_num)
        save_files.append(num)
        last_num = num

    return save_files

# Title Screen
def mainMenu():
    while True:
        box([["-- Project Labyrinth --"],
            ["0. Continue"],
            ["1. New Game"],
            ["2. Quit"]])
        global save
        select = ask(0,2)
        if select == 0:
            l = listSaveFiles()
            if l == []:
                select = 1
                print("No save files detected, starting a new game.")
            else:
                box([["-- Choose a save file --"],[l]])
                save = askList(l)
                restPoint()
        if select == 1:
            save = newSave()
            startStory("newgame")
            restPoint()
        if select == 2:
            break
        
mainMenu()


