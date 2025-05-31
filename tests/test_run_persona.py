import sys
from pathlib import Path
import subprocess

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from sstai.persona import load_persona_text


def test_run_persona_script():
    script = Path(__file__).resolve().parents[1] / "examples" / "run_persona.py"
    assert script.exists()
    result = subprocess.run(
        [sys.executable, str(script)], capture_output=True, text=True
    )
    assert result.returncode == 0
    output = result.stdout
    assert "Core online" in output
    assert load_persona_text() in output
