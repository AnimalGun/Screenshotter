import time
import keyboard
import pyautogui
from tkinter import *
from tkinter import filedialog
import os
from termcolor import colored

root = Tk()
root.withdraw()

print(colored('Please select the path you want to store your screenshots: ' , 'red'))
time.sleep(2)
chosendir = filedialog.askdirectory()
screenshotspath = os.chdir(chosendir)
print("Path you chose is: ", chosendir + '\n')

print(colored("Please choose the amount of screenshots you want to make: ", 'red'))
chosenloops = input()

print(colored("Script is starting in 5 seconds!\nEnjoy!", 'green'))
time.sleep(5)

def all_script():
    for f in range(int(chosenloops)):
        time.sleep(1)
        keyboard.press('page_down')
        if keyboard.is_pressed('page_down'):
            time.sleep(1)
            break
        Screenshot = pyautogui.screenshot()
        Screenshot.save(chosendir + '//screenshot' + str(f) + '.png')

all_script()