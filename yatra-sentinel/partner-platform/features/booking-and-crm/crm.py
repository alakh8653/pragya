"""Booking and CRM management."""

from dataclasses import dataclass
from typing import Dict


@dataclass
class Booking:
    user: str
    booking_id: str


class CRM:
    def __init__(self):
        self.bookings: Dict[str, Booking] = {}

    def add_booking(self, booking: Booking) -> None:
        self.bookings[booking.booking_id] = booking
