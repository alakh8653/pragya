"""Micro-lending module."""


def monthly_payment(amount: float, months: int, rate: float) -> float:
    return round((amount * (1 + rate)) / months, 2)
