# WiFi Access Guide

This guide explains how to connect Sahand's device to a WiFi network on Linux using NetworkManager's command line tool `nmcli`.

## Requirements

- NetworkManager installed and running.
- Proper permissions to control network interfaces (may require `sudo`).

## Steps

1. List available networks:
   ```bash
   nmcli device wifi list
   ```
2. Connect to a network (replace `SSID` and `PASSWORD`):
   ```bash
   nmcli device wifi connect "SSID" password "PASSWORD"
   ```
3. Verify connection:
   ```bash
   nmcli connection show --active
   ```

You can also perform these steps using the helper script in `src/wifi_access.py`:

```bash
python src/wifi_access.py list --interface wlan0     # list networks
python src/wifi_access.py connect SSID PASSWORD --interface wlan0
```

If your system does not use NetworkManager, consult your distribution's documentation for the appropriate tool (e.g., `wpa_supplicant`, `iwconfig`).
