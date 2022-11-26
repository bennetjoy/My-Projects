from time import sleep
import PySimpleGUI as sg
import threading
import os
TXTT=" "
layout = [[sg.Text(size=(12,1), key='-TEXT-')]]
window = sg.Window('Window', layout, finalize=True,size=(500,500))
def UI():
    
    while True:
        TXTT=TXTT+"\n "
        if(TXTT=='close'):
            window.close()
            exit()
        window['-TEXT-'].update(TXTT)
        sleep(1)



        






