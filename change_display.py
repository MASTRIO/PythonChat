import PySimpleGUI as sg
import PythonChat

sg.theme(Green)

layout = [  [sg.Text('What is Your New Name?')],
            [sg.InputText(PythonChat.display_name,do_not_clear=True, tooltip='This is your new display name!')]
            ]