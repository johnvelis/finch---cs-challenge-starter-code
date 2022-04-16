input.onButtonPressed(Button.A, function () {
    basic.pause(1000)
    while (finch.getDistance() > 20) {
        finch.startMotors(25, 25)
    }
    finch.setBeak(50, 0, 0)
    finch.startMotors(0, 0)
})
finch.startFinch()
basic.showLeds(`
    . . # . .
    . . # . .
    # # # # #
    . . # . .
    . . # . .
    `)
finch.setBeak(0, 100, 0)
