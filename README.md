# Simple-rpi-power-light
Simple script to switch on four LED's when raspberry pi switches on, to let me know when it is powered up.

## My Setup
I have 4 LED's, each with their anodes connected to one of the 3v3 supply pins and their cathodes conected to BCM pins 4, 17, 18, 27 respectively. If you have a different setup you will need to change `pwr-led.py` accordingly.

## Installation
### Clone
- Clone this repo to your local machine using `git clone https://github.com/avt613/Simple-rpi-power-light.git`
### Clone
- Add script to startup by edit '/etc/rc.local' eg. `sudo nano /etc/rc.local`
- insert `python /home/pi/Simple-rpi-power-light/pwr-led.py &` just before `exit 0`
- If your username is not `pi` or you you did not clone the repo to your home directory then you will need to change the path in the previous line
