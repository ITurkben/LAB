import os

def lock_computer():
    os.system('rundll32.exe user32.dll,LockWorkStation')

lock_computer()
