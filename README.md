# Deneyap Kart MicroPython Core 
[FOR TURKISH VERSION](docs/others/README_tr.md) ![trflag](docs/others/tr.png)

Deneyap Kart, designed and manufactured in Turkey, is a powerful development board with its strong MCU, robust design and flexible GPIOs. It allows the users in all levels (beginners to professionals) to create, design and develop projects in the fields of Electronics, Internet of Things (IoT) and Artificial Intelligence (AI). 

For more information, please visit [Deneyap Kart Technical Guide](https://docs.deneyapkart.org/#deneyap-kart) and [Deneyap Kart Official Website](https://deneyapkart.org).

## Contents
- [Flashing Instructions](#flashing-instructions)
- [Troubleshooting](#troubleshooting)
- [Deneyap Kart Pinout](#deneyap-kart-pinout)

### Flashing Instructions
- Install [Python 3](https://www.python.org/downloads/).
- With Python 3 installed, open a Terminal window and install the latest stable **esptool** release with pip3:
  `pip3 install esptool`
- Download latest [Deneyap Kart MicroPython firmware](https://github.com/deneyapkart/deneyapkart-micropython-core/releases/download/1.0.0/deneyapkart_micropython_v1.0.0.bin).
- Find the Serial Port Name (**PORT**). You may get port name via Arduino IDE from **Tools > Port**.
- Before flashing the MicroPython firmware, Deneyap Kart flash memory needs to be erased with the following command (change the **PORT** name with the one obtained in the previous step):
```python
esptool --chip esp32 --port <PORT> erase_flash
```
- With flash memory erased, flash the Deneyap Kart MicroPython firmware with the following command (change the **PORT** name and **DIR** based on your details):
```python
esptool --chip esp32 --port <PORT> --baud 460800 write_flash -z 0x1000 <DIR (Deneyap Kart MicroPython firmware path)>
```

### Troubleshooting
To report any issue/bug/problem etc., please make sure you have searched the similar encountered problems first. After that, if you are sure no on else had the same issue, use the [issue template](.github/ISSUE_TEMPLATE/bug_report.md) while reporting.  

### Deneyap Kart Pinout
![PinoutENG](docs/others/DeneyapKartPinoutENG_mpv1.0.png)