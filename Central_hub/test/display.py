import board, digitalio
from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306, time


# Dimensions of the display!
WIDTH = 128
HEIGHT = 32  
BORDER = 5

# Define the Pins of the OLED
oled_reset = digitalio.DigitalInOut(board.D4)
i2c = board.I2C()  # uses board.SCL and board.SDA

# Initialize oled object
oled = adafruit_ssd1306.SSD1306_I2C(WIDTH, HEIGHT, i2c, addr=0x3c, reset=oled_reset)

# Create blank image for drawing.
image1 = Image.new("1", (oled.width, oled.height))
image2 = Image.new("1", (oled.width, oled.height))

# Get drawing object to draw on image.
draw1 = ImageDraw.Draw(image1)
draw2 = ImageDraw.Draw(image2)

#draw1.rectangle((0, 0, oled.width, oled.height), outline=0, fill=0)
#draw2.rectangle((0, 0, oled.width, oled.height), outline=0, fill=0)

# Load default font.
font = ImageFont.load_default()

def Display(page, temp, moist):
    draw = draw1 if page == 1 else draw2
    # Clear display and set background
    oled.fill(0)
    oled.show()

    # Draw the time
    current_time = time.strftime("%H:%M")
    draw.text((0, 0), current_time, font=font, fill=255)
    
    # Draw sensor #
    sens = "Sensor " +str(page)
    (font_width, font_height) = font.getsize(sens)
    draw.text((oled.width - font_width, 0), sens, font=font, fill=255)
    
    # Draw the temperature
    text = "Temperature: {:.1f} °C".format(temp)
    (font_width, font_height) = font.getsize(text)
    draw.text(((oled.width - font_width) // 2, ((font_height + 2 )* 2) // 2),
        text,
        font=font,
        fill=255)
    # Draw Soil Moisture 
    text = "Moisture: {:.1f}".format(moist)
    (font_width, font_height) = font.getsize(text)
    draw.text(((oled.width - font_width) // 2, (oled.height - font_height)),
        text,
        font=font,
        fill=255)

    # Display image
    if page == 1:
        oled.image(image1)
    else:
        oled.image(image2)
    
    oled.show()


while True:
    Display(1,60, 50)
    time.sleep(10)