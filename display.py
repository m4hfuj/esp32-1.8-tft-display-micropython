from ST7735 import TFT, TFTColor
from sysfont import sysfont
from machine import SPI,Pin
import time
import math
spi = SPI(2, baudrate=20000000, polarity=0, phase=0, sck=Pin(14), mosi=Pin(13), miso=Pin(12))
tft=TFT(spi,16,17,18)
tft.initr()
tft.rgb(True)








some_data = {
    'title': 'Aquarium Monitor',
    'line': '---------------------',
    'temp': '',
    'ph': '',
    'tbd': '',
    'sol': '',
}

tft.fill(TFT.BLACK)

def test_main(some_data):
    # tft.text((0, 0), "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Curabitur adipiscing ante sed nibh tincidunt feugiat. Maecenas enim massa, fringilla sed malesuada et, malesuada sit amet turpis. Sed porttitor neque ut ante pretium vitae malesuada nunc bibendum. Nullam aliquet ultrices massa eu hendrerit. Ut sed nisi lorem. In vestibulum purus a tortor imperdiet posuere. ", TFT.GREEN, sysfont, 1)
    # time.sleep_ms(1000)
    tft.text((0,10), some_data['title'], TFT.GREEN, sysfont, 1)
    tft.text((0,20), some_data['line'], TFT.GREEN, sysfont, 1)
    tft.text((0,30), some_data['temp'], TFT.GREEN, sysfont, 1)
    tft.text((0,40), some_data['ph'], TFT.GREEN, sysfont, 1)
    tft.text((0,50), some_data['tbd'], TFT.GREEN, sysfont, 1)
    tft.text((0,60), some_data['sol'], TFT.GREEN, sysfont, 1)
    tft.text((0,150), some_data['line'], TFT.GREEN, sysfont, 1)

test_main(some_data)

i = 0
while True:
    i += 1

    temp = 23.45
    ph = 32.53
    tbd = 81.34
    sol = 64.76

    d = 2.5 * i
    
    # some_data['line'] = f'----------------------'
    some_data['temp'] = f'Temp     |{temp+d} C'
    some_data['ph'] =   f'PH       |{ph+d} m/c'
    some_data['tbd'] =  f'Turbidity|{tbd+d} m/c'
    some_data['sol'] =  f'Solidity |{sol+d} m/c'
    # some_data['temp'] = f'----------------------'

    time.sleep(2)

    test_main(some_data)