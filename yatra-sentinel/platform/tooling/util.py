"""Developer tooling utilities."""

import subprocess
from typing import Sequence


def run(cmd: Sequence[str]) -> str:
    """Run a shell command and capture output."""
    return subprocess.check_output(cmd, text=True)
