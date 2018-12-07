from gpiozero import LED

class Indicator:
    def __init__(self):
        self.led = LED(17)
    def on(self):
        self.led.on()
    def off(self):
        self.led.off()
