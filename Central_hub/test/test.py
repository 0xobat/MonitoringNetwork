import board, digitalio
from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306, time

# Dimensions of the display!
WIDTH = 128
HEIGHT = 32  
BORDER = 5

oled_reset = digitalio.DigitalInOut(board.D4)
i2c = board.I2C()  # uses board.SCL and board.SDA
# Initialize oled object
oled = adafruit_ssd1306.SSD1306_I2C(WIDTH, HEIGHT, i2c, addr=0x3C, reset=oled_reset)

oled_reset.direction = digitalio.Direction.OUTPUT

# Reset the display
oled_reset.value = False
time.sleep(0.1)
oled_reset.value = True
