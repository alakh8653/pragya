"""Design system tokens and utilities."""

COLOR_TOKENS = {
    "primary": "#1a73e8",
    "secondary": "#e91e63",
    "background": "#ffffff",
}

TYPOGRAPHY = {
    "font_family": "Inter, sans-serif",
    "base_size": 16,
}

def get_color(token: str) -> str:
    """Return color value for a given token."""
    return COLOR_TOKENS.get(token, "#000000")


def font_size(scale: float) -> float:
    """Compute font size using a scaling factor."""
    return TYPOGRAPHY["base_size"] * scale
