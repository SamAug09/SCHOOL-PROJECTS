# STUDENT DETAILS
# NAME: Augustus Samuel Tettey
# ID: 10948149


import PySimpleGUI as psg
import pyttsx3

Speech_Engine = pyttsx3.init()
Speech_Voice = Speech_Engine.getProperty('voices')



layout = [    [psg.Text('Enter Message:',text_color='black',background_color='white',)],
          
    [psg.InputText(key='message'),psg.Button('Speak',button_color='red')],

    [psg.Text('Choose Voice Type:',text_color='red',background_color='white'),psg.Radio('MALE', 'RADIO1', default=True, key='male',background_color='black'),psg.Radio('FEMALE', 'RADIO1', key='female',background_color='black')],
    
]

window = psg.Window('TTS MODULATOR', layout,background_color='blue')

while True:
    event, values = window.read()
    if event == psg.WINDOW_CLOSED:
        break
    elif event == 'Speak':
        text = values['message']
        if values['male']:
            Speech_Engine.setProperty('voice', Speech_Voice[0].id)
        elif values['female']:
           Speech_Engine.setProperty('voice', Speech_Voice[1].id) 
    
        Speech_Engine.say(text)
        Speech_Engine.runAndWait()

window.close()