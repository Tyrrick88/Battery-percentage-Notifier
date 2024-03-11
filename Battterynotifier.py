import psutil
from plyer import notification
import time

def get_battery_percentage():
    battery = psutil.sensors_battery()
    return battery.percent

def send_notification(message):
    notification.notify(
        title='Battery Notifier',
        message=message,
        app_name='Battery Notifier',
        timeout=10
    )

def main():
    # Set the threshold for the battery percentage
    threshold_percentage = 30

    while True:
        battery_percentage = get_battery_percentage()
        print(f'Battery Percentage: {battery_percentage}%')

        if battery_percentage <= threshold_percentage:
            message = f'Warning: Battery is low! ({battery_percentage}%)'
            send_notification(message)

        # Check the battery every 5 minutes (300 seconds)
        time.sleep(300)

if __name__ == "__main__":
    main()
