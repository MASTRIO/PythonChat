# Import Stuff
import PySimpleGUI as sg
import time

core_name = 'HaydenC'
user1 = core_name
display_name = 0

sg.theme('Green')
# All the stuff inside the GUI.
layout = [  [sg.Text('What is Your Name?')],
            [sg.InputText(do_not_clear=True, tooltip='This is your display name!')],
            [sg.Text('What do you want to say?')],
            [sg.InputText(do_not_clear=False, tooltip='This is what you want to say!')],
            [sg.Button('Ok'), sg.Button('Close')] ]

# Create the Window
window = sg.Window('Discord 2.0 - Message Input', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Close':	# if you close the window or press the close button
        time.sleep(2) ; break
    # Insert Text into chat area
    sg.Print('[',values[0],']', values[1], do_not_reroute_stdout=False, no_titlebar=True, grab_anywhere=True)
# Close the Window
window.close()