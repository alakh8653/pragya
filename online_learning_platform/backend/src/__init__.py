
"""Expose API submodules for easy router inclusion."""

from . import (
    analytics,
    assessments,
    assignments,
    auth,
    courses,
    messaging,
    notifications,
    payments,
    users,
)

__all__ = [
    "analytics",
    "assessments",
    "assignments",
    "auth",
    "courses",
    "messaging",
    "notifications",
    "payments",
    "users",
]

