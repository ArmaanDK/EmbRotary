# Wiring / Pin Assignments

Pin assignments for the Raspberry Pi Pico. See [PI-PICO_PINOUT.png](PI-PICO_PINOUT.png) for the physical pin diagram.

## Potentiometers (Speed Control)

All three potentiometers share the same 3V3 and GND rails (connected in parallel).

| Potentiometer   | Wiper → Pico Pin  | Notes       |
|-----------------|-------------------|-------------|
| Pot 1 (Servo 1) | GP26 — ADC0       |             |
| Pot 2 (Servo 2) | GP27 — ADC1       |             |
| Pot 3 (Servo 3) | GP28 — ADC2       |             |
| All pots VCC    | 3V3 (pin 36)      | Shared rail |
| All pots GND    | GND               | Shared rail |

## Servos (Feetech FT90R Continuous Rotation)

| Servo   | Signal → Pico Pin | Power   | Ground |
|---------|-------------------|---------|--------|
| Servo 1 | GP0 — PWM0A       | 5V rail | GND    |
| Servo 2 | GP2 — PWM1A       | 5V rail | GND    |
| Servo 3 | GP4 — PWM2A       | 5V rail | GND    |

## Power

| Connection   | Detail                                           |
|--------------|--------------------------------------------------|
| Input        | USB-C PD (5V/3A) directly into device            |
| Pico supply  | VSYS (pin 39) from 5V rail; Pico regulates to 3V3 internally |
| Servo supply | 5V rail directly                                 |
| Pot supply   | 3V3 from Pico (pin 36)                           |
