from machine import Pin
import time

# LEDs (saída)
led_red = Pin(0, Pin.OUT)
led_green = Pin(1, Pin.OUT)
led_blue = Pin(2, Pin.OUT)

# Botões com pull-up interno (entrada, nível baixo quando pressionado)
btn_red = Pin(3, Pin.IN, Pin.PULL_UP)
btn_green = Pin(4, Pin.IN, Pin.PULL_UP)
btn_blue = Pin(5, Pin.IN, Pin.PULL_UP)

def all_off():
    led_red.off()
    led_green.off()
    led_blue.off()

DEBOUNCE_MS = 200
last_press = 0

while True:
    if btn_red.value() == 0:
        if time.ticks_diff(time.ticks_ms(), last_press) > DEBOUNCE_MS:
            all_off()
            led_red.on()
            last_press = time.ticks_ms()
    if btn_green.value() == 0:
        if time.ticks_diff(time.ticks_ms(), last_press) > DEBOUNCE_MS:
            all_off()
            led_green.on()
            last_press = time.ticks_ms()
    if btn_blue.value() == 0:
        if time.ticks_diff(time.ticks_ms(), last_press) > DEBOUNCE_MS:
            all_off()
            led_blue.on()
            last_press = time.ticks_ms()
    time.sleep(0.01)