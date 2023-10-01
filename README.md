# Monitoring Network

This repository contains the code for an IoT system that monitors temperature and soil moisture levels in a garden. The system consists of several sensors that collect data and a central hub that stores the data and provides an Android application interface for users to view the data and control the sensors.


## Components

1. **Sensor Nodes:** These are the devices placed in the garden to collect data. They are responsible for measuring temperature and soil moisture levels.
2. **Central Hub:** The central hub serves as the system's core component. It performs the following functions:
   - **Data Aggregation:** Collects and stores data from the sensor nodes.
   - **Communication:** Facilitates communication between the sensor nodes and the Android application.
   - **Data Storage:** Stores historical data for analysis and user access.
   - **Fault Logging:** Records system faults and issues for troubleshooting.
3. **Android Application:** The Android application provides users with a user-friendly interface to:
   - **View Data:** Users can access real-time and historical data on temperature and soil moisture levels.
   - **Control Sensors:** Users can remotely control the sensor nodes, such as adjusting measurement frequencies or turning sensors on/off.

This repository contains the code and documentation for each of these components, enabling you to set up your own garden monitoring network. Explore the individual folders and documentation for more details on each component's functionality and installation instructions.

## Installation

To install the system, follow these steps:

1. Clone this repository to your local machine(s).
  - **Central_hub:** runs on a Raspberry Pi or a workstation within the range of the sensor(s)
  - **Node:** runs on the microcontroller attached to the sensor. In this case, it is a raspberry pico.
  - **SensorApp** is the Android APK that can be installed using Android Studio on your device/emulator.
2. Install the required dependencies by running `pip install -r requirements.txt`.
3. Create your sensor network in a star topology with the Raspberry Pi at the centre.
4. Run the `node.py` and `main.py` script to start the system.

## Usage

Once the system runs, you can access the API by navigating to `http://localhost:5000` in the android application. From there, you can view the data from all the sensors and control the sensors.

## Contributing

If you'd like to contribute to the system, please follow these steps:

1. Fork this repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit them.
4. Push your changes to your fork.
5. Submit a pull request to this repository.

## License

This code is licensed under the MIT License. See the `LICENSE` file for more information.
