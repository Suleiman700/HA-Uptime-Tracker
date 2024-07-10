
# Uptime Tracker

## Overview

The Uptime Tracker custom component for Home Assistant provides sensors that monitor the duration of server offline periods. It includes three sensors:

1. `Last Offline Time`: Shows the exact date and time when the server went offline.
2. `Last Offline Duration`: Displays the duration in seconds since the server last went offline & came online.
3. `Last Online Time`: Shows the exact date and time when the server is online.

![img.png](img.png)

---

## Installation

1. Download the Component:
   - Clone or download the repository.

2. Install in Home Assistant
   - Copy the `uptime_tracker` directory into the `custom_components` directory in your Home Assistant config directory.
   ```bash
    /config/
    ├── configuration.yaml
    └── custom_components/
      └── uptime_tracker/
        ├── __init__.py
        ├── manifest.json
        └── sensor.py
   ```
3. Restart Home Assistant
   1. Navigate to the `Developer Tools`
   2. Quick restart Home Assistant

4. Configure in `configuration.yaml`:
   - Add the following lines to your `configuration.yaml` file:
   ```yaml
   sensor:
      - platform: uptime_tracker
   ```

5. Restart Home Assistant
    1. Navigate to the `Developer Tools`
    2. Quick restart Home Assistant

---

## How It Works

1. The component continuously updates the `last online time` whenever the server is operational.
2. When server goes offline and returns online, the component calculates the duration of the outage by subtracting the last online time from the current time.

---

## Example Scenario
1. Server is online, It keep logging the last online time.
2. Server goes offline.
3. Server goes back online.
4. Server gets the last online time - the current time => offline duration in seconds