radio.onReceivedNumber(function (receivedNumber) {
    if (receivedNumber == 1) {
        score = receivedNumber
        basic.showIcon(IconNames.Heart)
    }
    if (receivedNumber == 2) {
        score = 0
        basic.clearScreen()
    }
})
input.onButtonPressed(Button.A, function () {
    if (score == 1) {
        music.playTone(262, music.beat(BeatFraction.Whole))
        radio.setGroup(613)
        radio.sendNumber(0)
        radio.setGroup(me)
    }
})
let score = 0
let me = 0
me = 10
radio.setGroup(me)
score = 0
