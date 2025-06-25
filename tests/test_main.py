import subprocess
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]


def test_main_output():
    result = subprocess.run(
        [sys.executable, str(PROJECT_ROOT / "main.py")],
        capture_output=True,
        text=True,
        check=True,
    )
    assert result.stdout.strip() == "Hello, Pragya!"
