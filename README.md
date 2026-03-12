# EmbRotary
Designing a motorized base that can turn embroidery hoops at variable rates.

## Design Criteria
- Hold three embroidery hoops upright
- Spin embroidery hoops at distinct rotational speeds
- Easy to build
- Use 3D printed hoops that max-out the printbed of a Creality Ender 3 V2
- Complete by the third week of March (less than 1 month from start date)

## Plan
A 3D printed base that houses three continuous servo motors, a Raspberry Pi Pico, and three rotary potentiometers for speed control.
The hoops will slide into crevases from the top of the box, interfacing with a bearing or smooth surface and a rubberized wheel attached to a continuous servo.
A 5VDC/3A power supply will power the device through a barrel jack on the back, supplying a 5VDC power rail for the three continuous servos and Raspberry Pi Pico.
Three potentiometers will connect, in parallel, between the Pico's 3V3 output and GND, with their wipers connected to three ADC pins on the Pico.

## Hardware
- Servo Motors
  - [4PCS Feetech FT90R](https://www.amazon.ca/dp/B07JDR2HH5)
- Microcontroller
  - [Raspberry Pi Pico](https://www.raspberrypi.com/products/raspberry-pi-pico/) ([Datasheet](https://pip-assets.raspberrypi.com/categories/610-raspberry-pi-pico/documents/RP-008307-DS-1-pico-datasheet.pdf?disposition=inline))

## Documentation
- [Hardware Selection](Hardware/HardwareSelection.md) — component choices and rationale
- [Wiring / Pin Assignments](Hardware/Wiring.md) — GPIO pin assignments and power connections
