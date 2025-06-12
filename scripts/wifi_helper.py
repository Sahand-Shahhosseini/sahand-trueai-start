"""Simple wrapper around `nmcli` for connecting to WiFi."""

import subprocess
import argparse


def connect_wifi(ssid: str, password: str) -> None:
    """Connect to a WiFi network using nmcli."""
    subprocess.run([
        "nmcli",
        "device",
        "wifi",
        "connect",
        ssid,
        "password",
        password,
    ], check=True)


def main() -> None:
    parser = argparse.ArgumentParser(description="Connect to WiFi using nmcli")
    parser.add_argument("--ssid", required=True, help="WiFi SSID")
    parser.add_argument("--password", required=True, help="WiFi password")
    args = parser.parse_args()
    connect_wifi(args.ssid, args.password)


if __name__ == "__main__":  # pragma: no cover - CLI entry point
    main()
