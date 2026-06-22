# ---This is from where you start the game---

#To be able to run this with pygame, colorama and other modules you will need to use python 3.12.10 or lower, because the newer versions don't support pygame and colorama
# You can do this using pip (for version 3.12.10 of python):
# py -3.12 -m pip install pygame
# py -3.12 -m pip install colorama

import pygame
import colorama
from src.role_select import role
from src.story import story
from src.menu import menu

story(1)
inventory, stats = role()
menu(inventory, stats)
