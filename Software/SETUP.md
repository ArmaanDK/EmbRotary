# Software Setup

How to flash MicroPython onto the Raspberry Pi Pico and deploy the EmbRotary script.

## 1. Flash MicroPython Firmware

1. Download the latest MicroPython UF2 firmware for the Pico from [micropython.org/download/RPI_PICO](https://micropython.org/download/RPI_PICO/)
2. Hold the **BOOTSEL** button on the Pico, then connect it to your computer via USB
3. Release BOOTSEL — the Pico will appear as a mass storage device called **RPI-RP2**
4. Drag and drop the downloaded `.uf2` file onto the RPI-RP2 drive
5. The Pico will reboot automatically into MicroPython (the drive will disappear)

## 2. Deploy main.py

Choose either Thonny (beginner-friendly GUI) or `mpremote` (command line).

### Option A — Thonny

1. Install [Thonny](https://thonny.org/)
2. In Thonny, go to **Tools → Options → Interpreter** and select **MicroPython (Raspberry Pi Pico)**
3. Open `Software/main.py`
4. Click **File → Save As**, choose **Raspberry Pi Pico** as the location, and save as `main.py`
5. The script will run automatically on every power-up

### Option B — mpremote (command line)

```bash
pip install mpremote
mpremote connect auto cp Software/main.py :main.py
```

## 3. Verify

Power cycle the Pico (unplug and replug USB, or disconnect and reconnect the 5V rail).
The servos should respond to the potentiometers immediately on startup — no further interaction needed.
