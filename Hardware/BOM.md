# Bill of Materials

Complete parts list for one EmbRotary unit.

---

## Power Path 

| | Path A — USB-C | Path B — DC Barrel Jack |
|---|---|---|
| **Soldering required?** | No | Yes |
| **Best for** | Prototyping / artist build | Permanent enclosure build |

Items marked **[A]** or **[B]** below apply only to that path. Unmarked items are required for both.

---

## Electronics

| Qty | Part | Value / Notes | Source |
|-----|------|---------------|--------|
| 3 | Feetech FT90R Continuous Rotation Servo | Sold in 4-packs; 1 spare | [Amazon.ca][servo] |
| 1 | Raspberry Pi Pico | Pre-soldered headers recommended | [Amazon.ca][pico] |
| 3 | Rotary Potentiometer | 10kΩ linear taper, 15mm shaft (WH148) | [Amazon.ca][pots] |
| 3 | Potentiometer Knob | 6mm knurled shaft, 15×17mm — fits WH148 | [Amazon.ca][knobs] |
| 1 | Electrolytic Capacitor, 1000µF 25V | Bulk input decoupling | [Amazon.ca][ecaps] |
| 3 | Electrolytic Capacitor, 220µF 25V | Per-servo decoupling | [Amazon.ca][ecaps] |
| 3 | Ceramic Capacitor, 100nF | Per-servo high-frequency noise filter | [Amazon.ca][ccaps] |
| 1 | Schottky Diode | D1 — reverse polarity protection; 1N5819 | [Amazon.ca][diodes] |
| 4 | Rectifier Diode | D2–D5; 1N4001 or equivalent | [Amazon.ca][diodes] |
| 1 | Zener Diode | 3.3V BZX55C3V3 — ADC input clamping | [Amazon.ca][zener] |
| 1 | TVS Diode | P6KE6.8A, 600W — transient suppression | [Amazon.ca][tvs] |
| 3 | Resistor, 1kΩ | R4, R5, R6 — current limiting on ADC lines | [Amazon.ca][resistors] |

> Capacitors, diodes, and resistors are sold in assortment kits containing far more than one unit requires. Surplus can be shared between builds.

---

## Power

| Qty | Part | Value / Notes | Source |
|-----|------|---------------|--------|
| 1 | USB-C Power Supply **[A]** | 5V/3A — plug-in, no soldering | [Amazon.ca][usbc-supply] |
| 1 | DC Wall Adapter **[B]** | 5V/3A, 5.5×2.1mm barrel jack output | [Amazon.ca][dc-supply] |
| 1 | Panel-Mount USB-C Socket **[B]** | 6-pin flush mount, PD 65W — soldered to hookup wire, nut-mounted to enclosure | [Amazon.ca][usbc-panel] |
| 1 | Hookup Wire Kit | 22 AWG, 7 colours, 26ft/spool | [Amazon.ca][wire] |
| 1 | Breadboard + Jumper Wire Kit **[A]** | 830+400pt boards, 200+ jumper wires | [Amazon.ca][breadboard] |

---

## Mechanical

| Qty | Part | Notes | Source |
|-----|------|-------|--------|
| 1 | 3D Printed Parts | Base, pinion gears, hoops — print files in `/Design` | See `/Design` |
| 6 | 625ZZ Ball Bearing | 5×16×5mm — drive and idler pinion per hoop (2× per hoop) | [Amazon.ca][bearings] |
| 1 | M2/M3/M4/M5 Screw Assortment | Alloy steel, black oxide — all printed assembly hardware | [Amazon.ca][screws] |
| 1 | Wood PLA Filament Bundle | 1.75mm, 30%+ real wood fibre, 4×200g — current print material | [Amazon.ca][filament] |

---

[servo]: https://www.amazon.ca/dp/B07JDR2HH5
[pico]: https://www.amazon.ca/Freenove-Raspberry-Compatible-Pre-Soldered-Development/dp/B09X33TBY3/
[pots]: https://www.amazon.ca/dp/B09XDR799P
[knobs]: https://www.amazon.ca/dp/B0C14MGL4B
[ecaps]: https://www.amazon.ca/dp/B0C1VBXCQM
[ccaps]: https://www.amazon.ca/dp/B08DNF191P
[diodes]: https://www.amazon.ca/dp/B08F2LHDZ7
[zener]: https://www.amazon.ca/dp/B07WDR4DBN
[tvs]: https://www.amazon.ca/dp/B0FRMZ2G2X
[resistors]: https://www.amazon.ca/ELEGOO-Resistor-Assortment-Compliant-Respberry/dp/B072BL2VX1/
[screws]: https://www.amazon.ca/dp/B0D6347484
[bearings]: https://www.amazon.ca/dp/B0CJFSBRTJ
[usbc-supply]: https://www.amazon.ca/Miuzei-Raspberry-Pi-Power-Supply/dp/B09WYRFWMW/
[dc-supply]: https://www.amazon.ca/BTF-LIGHTING-Certified-Transformer-Converter-SK6812RGBW/dp/B0G8JQ1FJ7/
[usbc-panel]: https://www.amazon.ca/dp/B0DL5JJS5T
[breadboard]: https://www.amazon.ca/Breadboards-Include-Solderless-Jumper-Tweezer/dp/B0BMFXPSVG/
[wire]: https://www.amazon.ca/dp/B083DN5R61
[filament]: https://www.amazon.ca/dp/B0C85SS6FT
