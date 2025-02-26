
Display code source: https://github.com/boochow/MicroPython-ST7735


esptool.py --port /dev/ttyUSB0 erase_flash

esptool.py --port /dev/ttyUSB0 write_flash -z 0x1000 bin/ESP32_GENERIC-20241025-v1.24.0.bin


Pin connections for ESP32:

LCD |ESP32-DevKitC
----|----
VLED|3V3
RST |IO17
A0  |IO16(DC)
SDA |IO13(MOSI)
SCK |IO14(CLK)
VCC |3V3
CS  |IO18
GND |GND


