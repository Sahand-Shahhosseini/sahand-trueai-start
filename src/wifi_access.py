"""Utilities for managing WiFi connections using ``nmcli``.

The helper functions are thin wrappers around ``nmcli`` so that tests can mock
out the command execution.  They do not attempt to parse the output in detail
but provide a minimal Python API for common tasks used throughout the docs.
"""

import subprocess
from typing import Optional


def list_networks(interface: Optional[str] = None) -> None:
    """List available WiFi networks."""
    cmd = ["nmcli", "device", "wifi", "list"]
    if interface:
        cmd.extend(["ifname", interface])
    subprocess.run(cmd, check=True)


def connect_wifi(ssid: str, password: str, interface: Optional[str] = None) -> None:
    """Connect to a WiFi network using NetworkManager (nmcli)."""
    cmd = ["nmcli", "device", "wifi", "connect", ssid, "password", password]
    if interface:
        cmd.extend(["ifname", interface])
    subprocess.run(cmd, check=True)
    # Display active connections so the user can verify the result
    subprocess.run(["nmcli", "connection", "show", "--active"], check=True)


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="WiFi helper using nmcli")
    sub = parser.add_subparsers(dest="command")

    list_p = sub.add_parser("list", help="List available networks")
    list_p.add_argument("--interface", help="WiFi interface name")

    conn_p = sub.add_parser("connect", help="Connect to a network")
    conn_p.add_argument("ssid", help="WiFi network SSID")
    conn_p.add_argument("password", help="WiFi password")
    conn_p.add_argument("--interface", help="WiFi interface name")

    args = parser.parse_args()

    if args.command == "list":
        list_networks(args.interface)
    elif args.command == "connect":
        connect_wifi(args.ssid, args.password, args.interface)
    else:
        parser.print_help()
