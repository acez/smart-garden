from machine import Pin
from time import sleep


PIN_PUMP = 5


class Pump:
    def __init__(self, interval_seconds, length_seconds):
        self._interval_seconds = interval_seconds
        self._length_seconds = length_seconds
        self._last_timer = 0
        self._last_interval_timer = 0
        self._state = 0
        self._pin = Pin(PIN_PUMP, Pin.OUT)

    def handle(self, timer):
        interval_timer_diff = timer - self._last_interval_timer
        if interval_timer_diff >= self._interval_seconds and self._state == 0:
            if self._state == 0:
                # start pump
                self._pin.off()
                self._state = 1
                self._last_timer = timer
            self._last_interval_timer = timer
        if self._state == 1:
            timer_diff = timer - self._last_timer
            if timer_diff >= self._length_seconds:
                # stop pump
                self._pin.on()
                self._state = 0


def main():
    timer = 0
    pump = Pump(interval_seconds=4, length_seconds=1)
    while True:
        pump.handle(timer)
        sleep(1)
        timer = timer + 1


main()
