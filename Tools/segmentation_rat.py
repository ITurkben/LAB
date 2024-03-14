import shutil
import glob
import ctypes
import sys
import webbrowser
import re
import pyautogui
import cv2
import urllib.request
import json
from pynput.keyboard import Listener
from pynput.mouse import Controller
import time
import keyboard

user32 = ctypes.WinDLL('user32')
kernel32 = ctypes.WinDLL('kernel32')

print(user32)
print(kernel32)