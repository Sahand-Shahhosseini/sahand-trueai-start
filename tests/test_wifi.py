from unittest.mock import patch

from wifi_access import list_networks, connect_wifi


def test_list_networks_builds_command():
    with patch('subprocess.run') as run_mock:
        list_networks(interface='wlan0')
        run_mock.assert_called_once_with(
            ['nmcli', 'device', 'wifi', 'list', 'ifname', 'wlan0'],
            check=True
        )


def test_connect_wifi_builds_commands():
    with patch('subprocess.run') as run_mock:
        connect_wifi('MySSID', 'pwd123', interface='wlan0')
        run_mock.assert_any_call(
            ['nmcli', 'device', 'wifi', 'connect', 'MySSID', 'password', 'pwd123', 'ifname', 'wlan0'],
            check=True
        )
        run_mock.assert_any_call(
            ['nmcli', 'connection', 'show', '--active'],
            check=True
        )
        assert run_mock.call_count == 2

