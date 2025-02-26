from ST7735 import TFT, TFTColor
from sysfont import sysfont
from machine import SPI,Pin
import time
import math
spi = SPI(2, baudrate=20000000, polarity=0, phase=0, sck=Pin(14), mosi=Pin(13), miso=Pin(12))
tft=TFT(spi,16,17,18)
tft.initr()
tft.rgb(True)

tft.rotation(1)






some_data = {
    'title': ' Aquarium Monitor',
    'line': '--------------------- ----',
    'temp': '',
    'ph': '',
    'tbd': '',
    'sol': '',
    'do': '',
    'sal': ''
}

tft.fill(TFT.BLACK)

def test_main(some_data):
    # tft.text((0, 0), "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Curabitur adipiscing ante sed nibh tincidunt feugiat. Maecenas enim massa, fringilla sed malesuada et, malesuada sit amet turpis. Sed porttitor neque ut ante pretium vitae malesuada nunc bibendum. Nullam aliquet ultrices massa eu hendrerit. Ut sed nisi lorem. In vestibulum purus a tortor imperdiet posuere. ", TFT.GREEN, sysfont, 1)
    # time.sleep_ms(1000)
    tft.text((0,5), some_data['title'], TFT.GREEN, sysfont, 1)
    # tft.text((3,17), some_data['line'], TFT.GREEN, sysfont, 1)

    # for x in range(0, tft.size()[0], 6):
    tft.line((0,18),(160,18), TFT.GREEN)
        
    tft.text((0,25), some_data['temp'], TFT.GREEN, sysfont, 1)
    tft.text((0,35), some_data['ph'], TFT.GREEN, sysfont, 1)
    tft.text((0,45), some_data['tbd'], TFT.GREEN, sysfont, 1)
    tft.text((0,55), some_data['sol'], TFT.GREEN, sysfont, 1)
    tft.text((0,65), some_data['do'], TFT.GREEN, sysfont, 1)
    tft.text((0,75), some_data['sal'], TFT.GREEN, sysfont, 1)

    tft.line((0,120),(160,120), TFT.GREEN)

    # tft.text((3,123), some_data['line'], TFT.GREEN, sysfont, 1)

test_main(some_data)

i = 0
while True:
    i += 1

    temp = 3.45
    ph = 32.53
    tbd = 81.34
    sol = 64.76
    do = 3421.55
    sal = 54.32

    d = i ** 1.53
    
    # some_data['line'] = f'----------------------'
    some_data['temp'] =   f' Temperature {temp*d:9.2f} C'
    some_data['ph'] =     f' PH          {ph*d:9.2f} m/c'
    some_data['tbd'] =    f' Turbidity   {tbd*d:9.2f} m/c'
    some_data['sol'] =    f' Solidity    {sol*d:9.2f} m/c'
    some_data['do'] =     f' DissolvedO2 {do*d:9.2f} m/c'
    some_data['sal'] =    f' Salinity    {sal*d:9.2f} m/c'
    # some_data['temp'] = f'----------------------'

    time.sleep(2)

    test_main(some_data)
    