def on_received_number(receivedNumber):
    global buttontime, score
    buttontime = 0
    score = 0
    if receivedNumber == 1:
        score += 1
        buttontime += 1
radio.on_received_number(on_received_number)

def on_button_pressed_a():
    next2 = 0
    radio.set_group(next2)
    radio.send_number(1)
    radio.set_group(me)
input.on_button_pressed(Button.A, on_button_pressed_a)

score = 0
buttontime = 0
me = 0
me = 613
radio.set_group(me)