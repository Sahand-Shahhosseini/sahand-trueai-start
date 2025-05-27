"""Utility to connect to a WiFi network using nmcli."""
import subprocess
from typing import Optional


def connect_wifi(ssid: str, password: str, interface: Optional[str] = None) -> None:
    """Connect to a WiFi network using NetworkManager (nmcli)."""
    cmd = ["nmcli", "device", "wifi", "connect", ssid, "password", password]
    if interface:
        cmd.extend(["ifname", interface])
    subprocess.run(cmd, check=True)


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Connect to WiFi")
    parser.add_argument("ssid", help="WiFi network SSID")
    parser.add_argument("password", help="WiFi password")
    parser.add_argument("--interface", help="WiFi interface name")
    args = parser.parse_args()

    connect_wifi(args.ssid, args.password, args.interface)
