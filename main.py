import board
from digitalio import DigitalInOut, Direction
from analogio import AnalogIn
from time import sleep

# setup pins
microphone = AnalogIn(board.IO1)

status = DigitalInOut(board.IO17)
status.direction = Direction.OUTPUT

led_pins = [
    board.IO21,
    board.IO26, # type: ignore
    board.IO47,
    board.IO33, # type: ignore
    board.IO34, # type: ignore
    board.IO48,
    board.IO35,
    board.IO36,
    board.IO37,
    board.IO38,
    board.IO39,
    board.IO40,
]

leds = [DigitalInOut(pin) for pin in led_pins]

for led in leds:
    led.direction = Direction.OUTPUT

# main loop
while True:
    volume = microphone.value

    print(volume)
    if volume > 23500:
        leds[0].value = 1
    elif volume < 23000:
        leds[0].value = 0


    if volume > 23750:
        leds[1].value = 1
    elif volume < 22500:
        leds[1].value = 0


    if volume > 24000:
        leds[2].value = 1
    elif volume < 23000:
        leds[2].value = 0


    if volume > 24250:
        leds[3].value = 1
    elif volume < 23000:
        leds[3].value = 0


    if volume > 24500:
        leds[4].value = 1
    elif volume < 23000:
        leds[4].value = 0


    if volume > 24750:
        leds[5].value = 1
    elif volume < 23000:
        leds[5].value = 0


    if volume > 25000:
        leds[6].value = 1
    elif volume < 23000:
        leds[6].value = 0


    if volume > 26500:
        leds[7].value = 1
    elif volume < 23000:
        leds[7].value = 0


    if volume > 27250:
        leds[8].value = 1
    elif volume < 23000:
        leds[8].value = 0


    if volume > 29000:
        leds[9].value = 1
    elif volume < 23000:
        leds[9].value = 0


    if volume > 31000:
        leds[10].value = 1
    elif volume < 23000:
        leds[10].value = 0



    sleep(.05)

    # instead of blinking,
    # how can you make the LEDs
    # turn on like a volume meter?
