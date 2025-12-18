import ctypes
import time
INTERVALLE = 60

while True :
    ctypes.windll.user32.LockWorkStation()
    time.sleep(INTERVALLE)
