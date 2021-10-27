# HX711

This code is for Rasperry Pi Zero, 2, 3 and 4 written in Python 3.
Distributed from https://github.com/gandalf15/HX711

[Description]
- Raspberry Pi sometimes reads invalid data because the pin pd_sck is high for 60 micro seconds or longer. To eliminate this problem I implemented simple filter which solves this problem. Therefore it provides better and more precise readings.
- It does not require additional libraries only Python 3.6 or higher.
- If data is invalid (Max and Min values of HX711) it detects it.
- It can quickly switch between channels and gains.
- It raises exceptions if wrong input provided.
- It has debug mode.
- It has separate offset and scale ratio for each channel and gain.
- It remembers last valid raw data for each channel and gain.
- It detects if pin pd_sck is high for longer than 60 micro seconds and therefore evalueates reading as Faulty. (only for Python 3 class)(60 us is important. Read Datasheet for more info.)

I recommend to connect pin 15(RATE) of HX711 to VCC (+3.3V) in order to get 80 samples per second. By default it is only 10.
If you have a cheap green breakout board as I have, you have to desolder and bend the pin 15(RATE) upwards. Then solder short wire to VCC.

Great explanation of strain gauges: https://www.allaboutcircuits.com/textbook/direct-current/chpt-9/strain-gauges/


## Installation

```sh
cd ~/Downloads/ && sudo rm -rf hx711 
git clone https://github.com/everylumi/hx711.git
cd hx711/  
sudo python3 setup.py install #Python3  
```

## Uninstallation

```sh
sudo pip3 uninstall hx711 #Python3  
```


## Usage example

```python
import RPi.GPIO as GPIO                # import GPIO
from hx711 import HX711                # import the class HX711
      
GPIO.setmode(GPIO.BCM)                 # set GPIO pin mode to BCM numbering
hx = HX711(dout_pin=5, pd_sck_pin=6)
```    


## License

This project is licensed under the terms of BSD 3-Clause license.
