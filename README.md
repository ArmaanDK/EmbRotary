# EmbRotary
Designing a motorized base that can turn embroidery hoops at variable rates.

## Design Criteria
- Hold three embroidery hoops upright
- Spin embroidery hoops at distinct rotational speeds
- Easy to build
- Use 3D printed hoops that max-out the printbed of a Creality Ender 3 V2

## Plan
A 3D printed base that houses three continuous servo motors, a Raspberry Pi Pico, and three rotary potentiometers for speed control.
The hoops will slide into crevices from the top of the box, interfacing with a bearing-mounted pinion gear and a driving pinion gear attached to a continuous servo.
A USB-C PD power supply (5VDC/3A) powers the device, supplying a 5VDC power rail for the three continuous servos and Raspberry Pi Pico.
Three potentiometers connect, in parallel, between the Pico's 3V3 output and GND, with their wipers connected to three ADC pins on the Pico.

## Mechanical Description
A shaftless, vertical oriented, gravity-preloaded, free-floating spur gear is supported by meshing with two pinion gears below it.
One pinion gear is motor-driven, applying a tangential force to spin the spur gear.
The second pinion gear is a bearing-supported idler pinion which is positioned contralaterally to the driven pinion so the spur gear rotates around its own center axis.
Currently exploring a tapered retaining double-flange design for the pinion gears to provide a lateral restoring force to oppose axial migration of the spur gear.

## Documentation
- [Hardware Selection](Hardware/HardwareSelection.md) - component choices and rationale
- [Bill of Materials](Hardware/BOM.md) - parts list with quantities
- [Wiring / Pin Assignments](Hardware/Wiring.md) - GPIO pin assignments and power connections
- [Software Setup](Software/SETUP.md) - flashing MicroPython and deploying the script
