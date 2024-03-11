# Battery Notifier

Battery Notifier is a Python script that monitors the battery percentage of your PC and sends a notification if it falls below a specified threshold.

## Features

- Monitors battery percentage using the `psutil` library.
- Sends notifications using the `plyer` library.
- Customizable threshold for low battery notifications.

## Prerequisites

- Python 3.x
- Install required libraries using: `pip install psutil plyer`

## Usage

1. Save the script as `battery_notifier.py`.
2. Run the script using a Python interpreter: `python battery_notifier.py`.

The script will continuously monitor the battery percentage, and if it falls below the specified threshold (default is 30%), it will send a notification.

## Configuration

- Adjust the `threshold_percentage` variable in the script according to your preferences.

## Unit Tests

The unit tests for the script are available in `test_battery_notifier.py`. Run the tests using:

```bash
python test_battery_notifier.py
