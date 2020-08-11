import PySimpleGUI as sg

sg.theme('Green')	# Add a touch of color
# All the stuff inside your window.
layout = [  [sg.Text('What is your display name?')],
            [sg.InputText()],
            [sg.Text('What do ya wanna say?')],
            [sg.InputText()],
            [sg.Button('Ok'), sg.Button('Close')] ]

# Create the Window
window = sg.Window('Discord 2.0 - Message Input', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Close':	# if user closes window or clicks cancel
        break
    sg.Print(do_not_reroute_stdout=False, no_titlebar=True)
    print('[',values[0],']', values[1])
    layout = []

window.close()