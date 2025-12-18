import ctypes
import time

while True :
    ctypes.windll.user32.LockWorkStation()
    time.sleep(10)