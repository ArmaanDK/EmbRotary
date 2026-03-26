# EmbRotary - MicroPython controller for Raspberry Pi Pico
#
# Three continuous rotation servos (Feetech FT90R) driven by three
# potentiometers. Each pot controls one servo bidirectionally:
#   - Pot fully CCW  -> full speed one direction   (~1000us pulse)
#   - Pot center     -> stopped                    (~1500us pulse)
#   - Pot fully CW   -> full speed other direction (~2000us pulse)
#
# Wiring:
#   Pot wipers  -> GP26 (ADC0), GP27 (ADC1), GP28 (ADC2)
#   Servo signal-> GP0,         GP2,          GP4
#   Pots        -> 3V3 and GND (in parallel)
#   Servos      -> 5V power rail and GND

from machine import ADC, Pin, PWM
import time

# ---------------------------------------------------------------------------
#                              Configuration
# ---------------------------------------------------------------------------

SERVO_FREQ_HZ   = 50      # Standard servo PWM frequency
PULSE_MIN_US    = 1000    # Full speed, one direction
PULSE_STOP_US   = 1500    # Stopped (neutral)
PULSE_MAX_US    = 2000    # Full speed, other direction

# Width of the center deadband in ADC counts (0-65535).
# Pot values within +/- this amount of center output a stop pulse,
# preventing creep from pot wobble or mechanical center imprecision.
ADC_DEADBAND    = 1200

# ---------------------------------------------------------------------------
#                                Pin setup
# ---------------------------------------------------------------------------

pots = [
    ADC(Pin(26)),   # Pot 1 -> ADC0
    ADC(Pin(27)),   # Pot 2 -> ADC1
    ADC(Pin(28)),   # Pot 3 -> ADC2
]

servos = [
    PWM(Pin(0)),    # Servo 1
    PWM(Pin(2)),    # Servo 2
    PWM(Pin(4)),    # Servo 3
]

for servo in servos:
    servo.freq(SERVO_FREQ_HZ)

# ---------------------------------------------------------------------------
#                             Helper functions
# ---------------------------------------------------------------------------

_PERIOD_US = 1_000_000 // SERVO_FREQ_HZ   # 20000 us at 50 Hz
_ADC_CENTER = 32767

def us_to_duty_u16(pulse_us):
    """Convert a pulse width in microseconds to a 16-bit duty cycle value."""
    return pulse_us * 65535 // _PERIOD_US

def adc_to_pulse_us(adc_val):
    """
    Map a 16-bit ADC reading to a servo pulse width in microseconds.
    A deadband around the center ADC value maps to the stop pulse so
    the servo does not creep when the pot is near center.
    """
    if abs(adc_val - _ADC_CENTER) < ADC_DEADBAND:
        return PULSE_STOP_US
    return PULSE_MIN_US + (adc_val * (PULSE_MAX_US - PULSE_MIN_US)) // 65535

# ---------------------------------------------------------------------------
#                                Main loop
# ---------------------------------------------------------------------------

while True:
    for pot, servo in zip(pots, servos):
        pulse_us = adc_to_pulse_us(pot.read_u16())
        servo.duty_u16(us_to_duty_u16(pulse_us))
    time.sleep_ms(20)   # Update rate matches servo PWM period (50 Hz)
