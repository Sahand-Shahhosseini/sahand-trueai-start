import sys
from pathlib import Path
import subprocess

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from sstai.persona import load_persona_text


def test_run_persona_script(tmp_path):
    script = Path(__file__).resolve().parents[1] / "examples" / "run_persona.py"
    result = subprocess.run([sys.executable, str(script)], capture_output=True, text=True)
    assert result.returncode == 0
    persona = load_persona_text()
    assert "🟢 Core online" in result.stdout
    assert persona in result.stdout
