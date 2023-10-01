# Central Hub
### Writen by Obatosin Obat-Olowu

This directory contains the code for the central hub of a Monitoring Sensor Network. The central hub is responsible for collecting data from all the sensors and storing it in a central location. It also provides an application interface for users to view the data and control the sensors.

## Installation

To install the central hub, follow these steps:

1. Clone this repository to your local machine.
2. Install the required dependencies by running:
```bash
 pip install -r requirements.txt
```
3. Run the `main.py` script to start the central hub.

## Usage

Once the central hub is running, you can access the web interface by navigating to `http://localhost:5000` in your web browser. From there, you can view the data from all the sensors and control the sensors.

## Central Hub Functionality

The central hub serves as the core component in our system, responsible for several key functions:

- **Communication with Sensor Nodes:** The hub establishes communication with the sensor nodes to collect real-time data.
- **Data Storage:** It stores data from each sensor node for up to 6 months, ensuring historical records are readily available.
- **Data Transfer to App:** The hub sends 24-hour aggregated data to the mobile application for user access.
- **CSV File Access:** It provides access to CSV files containing sensor log data through the app.

## Files and Components

The central hub comprises several files and components that contribute to its functionality:

- **main.py:** This file contains the primary functionality of the central hub, coordinating its operations.
- **store.py:** The storage functionality of the central hub is handled by this module, ensuring data persistence.
- **display.py:** This module controls the functionality of the OLED display, providing a visual interface for the hub's status and data.
- **node1.csv:** This CSV file stores sensor log data collected from node 1.
- **node2.csv:** Similar to node1.csv, this file stores sensor log data, but for node 2.
- **fault_log:** The fault log is a record of system faults and issues encountered, helping with troubleshooting and maintenance.

## Configuration

The `main.py` file can be configured by adjusting the following variables:

- `sensor_type`: The type of sensor module being used. Currently, only the DHT22 temperature and humidity sensor is supported.
- `sensor_pin`: The GPIO pin that the sensor module is connected to.
- `data_file`: The name of the CSV file that sensor data will be stored in.

## Dependencies

The `main.py` file requires the following dependencies:

- `Adafruit_rfm9x`: A Python library for controlling RFM9x LoRa radio modules, enabling long-range wireless communication.
- `RPi.GPIO`: A Python library for controlling the GPIO pins on a Raspberry Pi. 
- `Adafruit_ssd1306`:  A Python library for controlling SSD1306 OLED displays, allowing you to display graphics and text on OLED screens.
- `PIL`:  A Python library for working with images, including opening, manipulating, and saving various image formats.

## Contributing

If you'd like to contribute to the central hub, please follow these steps:

1. Fork this repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit them.
4. Push your changes to your fork.
5. Submit a pull request to this repository.

## License

This code is licensed under the MIT License. See the `LICENSE` file for more information.
