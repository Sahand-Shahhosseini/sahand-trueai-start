# WiFi Access

This project includes utilities for connecting Sahand's device to a WiFi network. The easiest method uses the `nmcli` command-line tool. The same logic is also available via a small Python helper for scripted use.

## Connecting with nmcli

1. List available networks:
   ```bash
   nmcli device wifi list
   ```
2. Connect to a network:
   ```bash
   nmcli device wifi connect <SSID> password <PASSWORD>
   ```

## Python Helper

A convenience function wrapping `nmcli` is provided in `scripts/wifi_helper.py`. Run it with your network credentials:

```bash
python scripts/wifi_helper.py --ssid <SSID> --password <PASSWORD>
```

This script simply calls `nmcli` under the hood, so it requires NetworkManager to be installed and active on the target machine.
