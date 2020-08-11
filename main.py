# Import Stuff
import PySimpleGUI as sg
import time

core_name = 'HaydenC'
user1 = core_name
display_name = core_name

sg.theme('Green')
# All the stuff inside the GUI.
layout = [  [sg.Text('What is Your Name?')],
            [sg.InputText(display_name,do_not_clear=True, tooltip='This is your display name!')],
            [sg.Text('What do you want to say?')],
            [sg.InputText(do_not_clear=False, tooltip='This is what you want to say!')],
            [sg.Button('Ok'), sg.Button('Close')] ]

# Announce that the User has joined the chat


# Create the Message Input gui
window = sg.Window('Discord 2.0 - Message Input', layout)
# Runs events when specific buttons are pressed
while True:
    event, values = window.read()
    # Runs when program is closed
    if event == sg.WIN_CLOSED or event == 'Close':
        time.sleep(2)
        f= open("PythonChat/data_storage/UserData.txt","w+")
        f.write('Display Name =', display_name)
        f.close()
        break
    # Runs when OK is pressed
    sg.Print('[',values[0],']', values[1], do_not_reroute_stdout=False, no_titlebar=True, grab_anywhere=True)
    display_name = values[0]
# Close the Window
window.close()