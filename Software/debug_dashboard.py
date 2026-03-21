# EmbRotary - Debug Logger
#
# Compact one-liner debug output for Thonny's shell.
# Columns: raw ADC counts for all three pots, then pulse widths for all three servos.
#
# Run this instead of main.py when diagnosing hardware issues.
# Servos are driven normally throughout — non-intrusive.

from machine import ADC, Pin, PWM
import time

# ---------------------------------------------------------------------------
#                      Configuration (matches main.py)
# ---------------------------------------------------------------------------

SERVO_FREQ_HZ = 50
PULSE_MIN_US  = 1000
PULSE_STOP_US = 1500
PULSE_MAX_US  = 2000
ADC_DEADBAND  = 1200

# ---------------------------------------------------------------------------
#                               Pin setup
# ---------------------------------------------------------------------------

pots   = [ADC(Pin(26)), ADC(Pin(27)), ADC(Pin(28))]
servos = [PWM(Pin(0)),  PWM(Pin(2)),  PWM(Pin(4)) ]

for s in servos:
    s.freq(SERVO_FREQ_HZ)

# ---------------------------------------------------------------------------
#                      Helpers (identical to main.py)
# ---------------------------------------------------------------------------

_PERIOD_US  = 1_000_000 // SERVO_FREQ_HZ
_ADC_CENTER = 32767

def us_to_duty_u16(pulse_us):
    return pulse_us * 65535 // _PERIOD_US

def adc_to_pulse_us(adc_val):
    if abs(adc_val - _ADC_CENTER) < ADC_DEADBAND:
        return PULSE_STOP_US
    return PULSE_MIN_US + (adc_val * (PULSE_MAX_US - PULSE_MIN_US)) // 65535

# ---------------------------------------------------------------------------
#                                Main loop
# ---------------------------------------------------------------------------

print("P1      P2      P3      S1      S2      S3")

while True:
    adc_vals   = []
    pulse_vals = []

    for pot, servo in zip(pots, servos):
        raw      = pot.read_u16()
        pulse_us = adc_to_pulse_us(raw)
        servo.duty_u16(us_to_duty_u16(pulse_us))
        adc_vals.append(raw)
        pulse_vals.append(pulse_us)

    print("{:<8}{:<8}{:<8}{:<8}{:<8}{:<8}".format(*adc_vals, *pulse_vals))
    time.sleep_ms(200)