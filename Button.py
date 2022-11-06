import RPi.GPIO as GPIO

class Button():
    down = False
    iopin = 0
    pressed = False

    def __init__(self, ioPin):
        self.iopin = ioPin
        GPIO.setup(ioPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 10 to be an input pin and set initial value to be pulled low (off)

    def update(self):
        buttDown = GPIO.input(self.iopin)
        if self.down:
            self.pressed = False
            if not buttDown: 
                self.down = False
                #print("Button up: ")
        else:
            if buttDown: 
                self.down = True
                self.pressed = True
                #print("Button down: ")
            else:
                self.pressed = False
 

