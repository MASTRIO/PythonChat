# Import Stuff
import PySimpleGUI as sg
import time

# Variables
display_name = 'HaydenC'
has_join_marked = False

sg.theme('Green')
# All the stuff inside the GUI.
layout = [  [sg.Text('What do you want to say?')],
            [sg.InputText(do_not_clear=False, tooltip='This is what you want to say!')],
            [sg.Button('Ok'), sg.Button('Close')] ]

# Create the Message Input gui
window = sg.Window('Discord 2.0 - Message Input', layout)
# Runs events when specific buttons are pressed
while True:
    if has_join_marked == False:
        has_join_marked = True
        sg.Print(display_name, 'has joined the chat', do_not_reroute_stdout=False, no_titlebar=True, no_button=True, grab_anywhere=True)
    event, values = window.read()
    # Runs when program is closed
    if event == sg.WIN_CLOSED or event == 'Close':
        print(display_name, 'has left the chat')
        time.sleep(1)
        break
    # Runs when OK is pressed
    print('[', display_name,']', values[0])

# Close the Window
window.close()