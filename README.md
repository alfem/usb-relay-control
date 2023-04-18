# Python script to switch on/off an usb relay board from CFSunbird

## Intro

For my home automation system I bought a little relay board with USB interface.

Seller provides windows software but I need to control this relays with my Linux based minipc (and Home Assistant). 

After some Internet search, I found a couple of projects related to this kind of boards, but they were not compatible with my model.

Seller wrote short instructions about controlling the relays in the item description:

https://www.aliexpress.com/i/1005003781042941.html

I first made a quick test, using bare shell:
```
echo -e '\xA0\x01\01\xA2' > /dev/hidraw6   (switch on first relay)
```
and it worked!

So I cooked a more versatile script to manage my twin relay board.

## Usage

Plug your board in your computer, and check for a new device named like /dev/hidrawN 

Run the script using that file name as first parameter, relay number as second one and command (on or off) as the last one.
```
./usb-relay.py /dev/hidraw1 1 on
```
You should hear an audible click from the activated relay.

If your user does not have write permission on the device file name, you can run the script as root, or use sudo, or add some udev rules.


