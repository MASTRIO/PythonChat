import PySimpleGUI as sg
import main

layout = [  [sg.Text('What is Your Name?')],
            [sg.InputText(main.display_name,do_not_clear=True, tooltip='This is your display name!')]
            ]