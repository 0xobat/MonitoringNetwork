# Node.py

**node.py** is a Python script that runs on a sensor node and transmits sensor data to a central hub using a LoRa radio module. The script is designed to run on a Raspberry Pi with a LoRa radio module connected via SPI.

## Features
- Sends sensor data to a central hub using LoRa radio communication
- Supports automatic channel selection and retry on failure
- Logs transmission failures to a fault log
- Configurable parameters for frequency, GPIO pins, node ID, and more

## Requirements
- Python 3
- RPi.GPIO
- spidev
- adafruit-circuitpython-rfm9x

## Installation
1. Install Python 3 on your Raspberry Pi if it is not already installed.
2. Install the required Python libraries by running the following command in your terminal:
```bash
    pip3 install RPi.GPIO spidev adafruit-circuitpython-rfm9x
```
3. Download **node.py** to your Raspberry Pi.

## Usage
1. Connect your LoRa radio module to your Raspberry Pi via SPI.
2. Open a terminal and navigate to the directory where **node.py** is located.
3. Run the following command to start the script:
```bash
    python3 node.py
```
4. The script will start running and will transmit sensor data to the central hub using the LoRa radio module.

## Configuration
You can configure the following parameters in **node.py**:

- `FREQ`: The frequency (in MHz) to use for LoRa communication. Default is 915.0.
- `CS`: The GPIO pin to use for the chip select (CS) signal. Default is 25.
- `RESET`: The GPIO pin to use for the reset signal. Default is 17.
- `CHANNEL`: The LoRa channel to use for communication. Default is 0.
- `NODE_ID`: The ID of the sensor node. Default is 1.
- `HUB_ID`: The ID of the central hub. Default is 255.
- `INTERVAL`: The interval (in seconds) between sensor readings. Default is 30.

You can modify these parameters in the `setup()` function at the beginning of the script.

## License
**node.py** is licensed under the MIT License. See [LICENSE](LICENSE) for more information.

## Acknowledgements
**node.py** was created by John Doe for the XYZ project. Special thanks to Jane Smith for her contributions to the project.
