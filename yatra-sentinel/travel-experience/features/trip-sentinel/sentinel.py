"""Trip sentinel alerts."""

from typing import List


class AlertCenter:
    def __init__(self):
        self.alerts: List[str] = []

    def add_alert(self, msg: str) -> None:
        self.alerts.append(msg)

    def latest(self) -> str:
        return self.alerts[-1] if self.alerts else ""
