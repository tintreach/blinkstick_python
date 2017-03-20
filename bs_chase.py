import time
import math
import colorsys
from random import randint

from blinkstick import blinkstick

class Main(blinkstick.BlinkStickPro):
    def run(self):
        self.send_data_all()
        # Set start of index
        x = 0

        sign = 1
        try:
            while True:
                # Set Color R,G,B
                self.bstick.set_color(0, x, 255, 0, 0)
                # Adding this to see what is going on
                print x
                # Set light on time
                time.sleep(0.05)
                # Set off color "black"
                self.bstick.set_color(0, x, 0, 0, 0)
                # Set off time
                time.sleep(0.0005)

                x += sign
                # Ping Pong effect
                # If the index reaches the end of led count, start at the end and go backwards from the end.  Ping Pong
                #if x == self.r_led_count - 1:
                #    sign = -1

                # Chase loop effect
                # Must add +1 to led count or last led will fall off the count * Need to fix
                if x == self.r_led_count - 1:
                    x = 0
                    sign = 1

                elif x == 0:
                    sign = 1


        except KeyboardInterrupt:
            self.off()
            return

# Change the number of LEDs for r_led_count, add + 1 for chase loop
main = Main(r_led_count=8, b_led_count=1, g_led_count=1, max_rgb_value=256)
if main.connect():
    main.run()

else:
    print "No BlinkSticks found"