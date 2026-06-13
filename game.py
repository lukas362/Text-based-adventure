#To be able to run this with pygame, colorama and other modules you will need to use python 3.12.10 or lower, because the newer versions don't support pygame and colorama
# You can do this using pip (for version 3.12.10 of python):
# py -3.12 -m pip install pygame
# py -3.12 -m pip install colorama

import pygame
import colorama
from role_select import role
from story import story
from menu import menu

story()
role()
menu()
