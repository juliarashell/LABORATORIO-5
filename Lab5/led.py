import pyfirmata

import time

board = pyfirmata.Arduino('COM3')


while True:
    
    #Led Rojo
    board.digital [12]. write (1)
    time.sleep(3)
    board.digital [12]. write (0)
    time.sleep(1)

    #Led Amarillo
    board.digital [10]. write (1)
    time.sleep(3)
    board.digital [10]. write (0)
    time.sleep(1)

    #led verde
    board.digital [8]. write (1)
    time.sleep(3)
    board.digital [8]. write (0)
    time.sleep(3)