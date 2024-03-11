import unittest
from unittest.mock import patch, Mock
from battery_notifier import get_battery_percentage, send_notification

class TestBatteryNotifier(unittest.TestCase):

    @patch('psutil.sensors_battery')
    def test_get_battery_percentage(self, mock_sensors_battery):
        mock_sensors_battery.return_value.percent = 75
        result = get_battery_percentage()
        self.assertEqual(result, 75)

    @patch('plyer.notification.notify')
    def test_send_notification(self, mock_notify):
        send_notification('Test Notification')
        mock_notify.assert_called_once_with(
            title='Battery Notifier',
            message='Test Notification',
            app_name='Battery Notifier',
            timeout=10
        )

if __name__ == '__main__':
    unittest.main()
