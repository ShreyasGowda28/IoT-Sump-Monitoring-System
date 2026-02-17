# IoT Sump Monitoring System using ESP32, MQTT, and Django

## Overview

This IoT-based Sump Monitoring System is a real-time monitoring and control application designed to supervise sump tank conditions using an ESP32 microcontroller and a Django backend. The system continuously monitors water level, mud level, leakage current, and motor status, and displays the readings on a live web dashboard.

Sensor data is transmitted using the MQTT protocol and stored in a database for monitoring and analysis.



## Features

* **Real-Time Sensor Monitoring**: Monitors water level, mud level, and leakage current.
* **Automatic Motor Control**: Motor status is controlled based on predefined safety conditions.
* **MQTT Communication**: Uses MQTT protocol for lightweight IoT data transmission.
* **Django Backend Integration**: Subscribes to MQTT topic and stores data in SQLite database.
* **Live Dashboard**: Displays latest sump readings with auto-refresh.
* **Admin Panel**: Django admin interface for viewing and managing stored data.
* **REST API Support**: Endpoint available for receiving sump data.



## Project Structure

```
├── monitoring/                  # Django application
│   ├── migrations/
│   ├── templates/
│   │   └── dashboard.html       # Live monitoring dashboard
│   ├── admin.py
│   ├── apps.py
│   ├── models.py                # SumpReading model
│   ├── mqtt_client.py           # MQTT subscriber logic
│   ├── serializers.py           # REST serializer
│   ├── views.py                 # API and dashboard views
│   └── tests.py
│
├── sump_project/                # Django project configuration
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── db.sqlite3                   # Database
├── manage.py                    # Django management script
└── README.md                    # Project documentation
```

ESP32 Firmware (Wokwi Simulation):

```
sketch.ino                       # ESP32 MQTT publisher code
```



## Prerequisites

* Python 3.8+
* pip
* Git
* Internet connection (for MQTT public broker)
* Wokwi Simulator (for ESP32 testing)



## Installation

1. **Clone the repository**:

```bash
git clone https://github.com/ShreyasGowda28/IoT-Sump-Monitoring-System.git
cd IoT-Sump-Monitoring-System
```

2. **Create and activate virtual environment**:

```bash
python -m venv venv
venv\Scripts\activate    # Windows
```

3. **Install dependencies**:

```bash
pip install django djangorestframework paho-mqtt
```

4. **Run migrations**:

```bash
python manage.py makemigrations
python manage.py migrate
```

5. **Create superuser (optional)**:

```bash
python manage.py createsuperuser
```



## Usage

### 1. Run Django Server

```bash
python manage.py runserver
```

### 2. Access Web Application

Dashboard:

```
http://127.0.0.1:8000/dashboard/
```

Admin Panel:

```
http://127.0.0.1:8000/admin/
```



### 3. Run ESP32 Simulation

Open the project in **Wokwi** and start simulation.

The ESP32 will:

* Connect to WiFi
* Connect to MQTT broker
* Publish JSON sensor data to topic:

```
sump/data
```



## MQTT Configuration

* **Broker**: broker.hivemq.com
* **Port**: 1883
* **Topic**: sump/data
* **Protocol**: MQTT



## Data Format

The ESP32 publishes sensor data in JSON format:

```json
{
  "water_level": 955,
  "mud_level": 503,
  "leakage_current": 3,
  "motor_status": true
}
```

Each record is saved with a timestamp in the database.



## Motor Control Logic

The motor turns **ON** when:

* Water Level > 800
* Mud Level < 1200
* Leakage Current < 5

If any condition fails, the motor turns **OFF**.

This ensures automated and safe sump operation.


## Technologies Used

* ESP32 (Wokwi Simulation)
* Python
* Django
* Django REST Framework
* Paho-MQTT
* SQLite
* MQTT Protocol
* HTML & CSS



## Applications

* Smart water tank monitoring
* Automated sump management
* Industrial liquid monitoring
* IoT-based safety systems



## How to Run

After installation:

```
python manage.py runserver
```

Open:

```
http://127.0.0.1:8000/dashboard/
```

Start ESP32 simulation to see live updates.



## Author

Shreyas Gowda S
M.Tech – IoT & Embedded Systems
IoT Sump Monitoring System Project



## Acknowledgements

* Django for backend framework
* Paho-MQTT for MQTT integration
* HiveMQ public broker
* Wokwi IoT Simulator

