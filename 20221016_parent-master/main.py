def on_received_number(receivedNumber):
    global a, b, pinstatus
    
    赤外線リモコン.ライトを点ける()
    if receivedNumber == 0:
        a = 2 * a
        赤外線リモコン.色を変える(Color.GREEN)
    if receivedNumber == 1:
        a = 3 * a
        赤外線リモコン.色を変える(Color.ORANGE)
    if receivedNumber == 2:
        a = 5 * a
        赤外線リモコン.色を変える(Color.EMERALD)
    if receivedNumber == 3:
        a = 7 * a
        赤外線リモコン.色を変える(Color.PURPLE)
    if receivedNumber == 4:
        赤外線リモコン.色を変える(Color.SKY)
        b += 1
    if receivedNumber == 5:
        赤外線リモコン.色を変える(Color.PINK)
        b += 1
    status = []
    status.append(receivedNumber)
    pin = [0, 1, 2, 3]
    if status == pin:
        pinstatus = 1
radio.on_received_number(on_received_number)

def on_button_pressed_a():
    radio.set_group(10)
    radio.send_number(1)
    music.play_tone(262, music.beat(BeatFraction.WHOLE))
    radio.set_group(me)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global a, b, pinstatus
    if a == 210 or b >= 2:
        if pinstatus == 1
            赤外線リモコン.色を変える(Color.BLUE)
            music.play_tone(659, music.beat(BeatFraction.DOUBLE))
            radio.set_group(10)
            radio.send_number(2)
            radio.set_group(me)
    else:
        for index in range(3):
            赤外線リモコン.色を変える(Color.RED)
            赤外線リモコン.ライトを消す()
            music.play_tone(208, music.beat(BeatFraction.WHOLE))
        a = 1
        b = 0
input.on_button_pressed(Button.B, on_button_pressed_b)

me = 0
b = 0
a = 1
c = 0
pinstatus = 0
me = 613
radio.set_group(me)
