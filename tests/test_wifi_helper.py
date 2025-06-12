import subprocess
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from scripts import wifi_helper


def test_connect_wifi_runs_nmcli(monkeypatch):
    calls = []

    def fake_run(cmd, check):
        calls.append((cmd, check))

    monkeypatch.setattr(subprocess, "run", fake_run)
    wifi_helper.connect_wifi("MySSID", "secret")
    assert calls == [
        (
            [
                "nmcli",
                "device",
                "wifi",
                "connect",
                "MySSID",
                "password",
                "secret",
            ],
            True,
        )
    ]
