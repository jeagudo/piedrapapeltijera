clase = ""
radio.set_group(100)
serial.redirect(SerialPin.USB_TX, SerialPin.USB_RX, BaudRate.BAUD_RATE9600)
basic.show_icon(IconNames.YES)

def on_forever():
    global clase
    clase = serial.read_string()
    if clase != "":
        basic.show_string(clase)
        if clase == "0":
            radio.send_number(0)
        elif clase == "1":
            radio.send_number(1)
        elif clase == "2":
            radio.send_number(2)
        elif clase == "3":
            radio.send_number(3)
        else:
            radio.send_number(5)
basic.forever(on_forever)
