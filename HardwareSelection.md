# Hardware Selection
A breakdown of the hardware selected, as well as the rationale for each selection.

## Motors
Feetech FT90R
- Servos rotate as a slower rate than DC motors
- Can be more easily controlled without needed a complex motor control board handling PWM and transient protection
- Quick and easy to source on Amazon.ca for cross-country parallel building
- Adequate performance without breaking the budget ($29.98CAD for 4)

## Microcontroller
Raspberry Pi Pico
- Jellybean part (~$4USD from raspberrypi.com)
- Adequate GPIO and ADC inputs for project
- MicroPython has more human-readable code for understandability outside of the technological field
- Accepts 5VDC input without needing stepping-down from an external circuit

## Power Cleaning
### Capacitors
Transients from servos when PWM triggers movement can drop the power rail voltage

#### Bulk Input Capacitor
Softens the startup, spec'd for a worst-case scenario of all motors stalling and the Pico at max power consumption (very unrealistic).

Three servos with spec'd stalling currents of $700mA @ 4.8V$ and $800mA @ 6V$, linearly interpolating:

$700 + \frac{800 - 700}{6 - 4.8}(5 - 4.8) = 716.7mA$

$3 \times 716.7mA = 2150mA$

Worst-case scenario spec for Raspberry Pi Pico @ 5V is 95.5 mA,

$I_{T} = I_{Servos} + I_{Pico}$

$I_{T} = 2150mA + 95.5mA = 2245.5mA$

Assuming a $100 \mu s$ response from the power supply and a goal voltage change of less than 5%,

$C = \frac{2.25 A \times 0.0001 s}{5V \times 0.05} = 900 \mu F $

Indicating a minimum $1000 \mu F$ capacitor would be appropriate for the bulk input capacitor.

#### Servo Decoupling Capacitors
Handles transients per-motor going back to the power rail.

$C = \frac{0.7167 \times 0.0001 s}{5V \times 0.05} = 286.7 \mu F$

Since the bulk capacitor will also handle transients, we can rely on $100-220 \mu F$ capacitors instead.

#### Servo Noise Abatement
Expected noise from PWM servo control is in the 10s of MHz range. Adding $100nF$ ceramic capacitors in parallel to the decoupling capacitors will help mitigate high-frequency switching noise from making its way to the power rail.