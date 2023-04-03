# STUDENT DETAILS
# NAME: Augustus Samuel Tettey
# ID: 10948149


import PySimpleGUI as psg
import qrcode


layout = [
    [psg.Text('Enter text or URL:',text_color='black',background_color='white',)],
    [psg.InputText(key='text'),psg.Button('Create',button_color='red')],

    [psg.Image(key='image')]

]

window = psg.Window('QR CODE GENERATOR', layout,background_color='blue')

while True:
    event, values = window.read()
    if event == psg.WINDOW_CLOSED:
        break
    elif event == 'Create':
        text = values['text']
        qr = qrcode.QRCode(version=1, box_size=10, border=5)
        qr.add_data(text)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        img.save("qrcode.png")
        window['image'].update("qrcode.png")


window.close()