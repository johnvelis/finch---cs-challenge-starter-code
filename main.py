def on_button_pressed_a():
    basic.pause(1000)
    while finch.get_distance() > 20:
        finch.start_motors(25, 25)
    finch.set_beak(50, 0, 0)
    finch.start_motors(0, 0)
input.on_button_pressed(Button.A, on_button_pressed_a)

finch.start_finch()
basic.show_leds("""
        . . # . .
        . . # . .
        # # # # #
        . . # . .
        . . # . .
""")
finch.set_beak(0, 100, 0)