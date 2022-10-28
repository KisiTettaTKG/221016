radio.onReceivedNumber(function (receivedNumber) {
    赤外線リモコン.ライトを点ける()
    if (receivedNumber == 0) {
        a = 2 * a
        赤外線リモコン.色を変える(Color.Green)
    }
    if (receivedNumber == 1) {
        a = 3 * a
        赤外線リモコン.色を変える(Color.Orange)
    }
    if (receivedNumber == 2) {
        a = 5 * a
        赤外線リモコン.色を変える(Color.Emerald)
    }
    if (receivedNumber == 3) {
        a = 7 * a
        赤外線リモコン.色を変える(Color.Purple)
    }
    if (receivedNumber == 4) {
        赤外線リモコン.色を変える(Color.Sky)
        b += 1
    }
    if (receivedNumber == 5) {
        赤外線リモコン.色を変える(Color.Pink)
        b += 1
    }
})
input.onButtonPressed(Button.A, function () {
    radio.setGroup(10)
    radio.sendNumber(1)
    music.playTone(262, music.beat(BeatFraction.Whole))
    radio.setGroup(me)
})
input.onButtonPressed(Button.B, function () {
    if (a == 210 || b >= 2) {
        赤外線リモコン.色を変える(Color.Blue)
        music.playTone(659, music.beat(BeatFraction.Double))
        radio.setGroup(10)
        radio.sendNumber(2)
        radio.setGroup(me)
    } else {
        for (let index = 0; index < 3; index++) {
            赤外線リモコン.色を変える(Color.Red)
            赤外線リモコン.ライトを消す()
            music.playTone(208, music.beat(BeatFraction.Whole))
        }
        a = 1
        b = 0
    }
})
let me = 0
let b = 0
let a = 0
a = 1
b = 0
me = 613
radio.setGroup(me)
