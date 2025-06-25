"""Quality assurance utilities."""


def verify(document: str) -> bool:
    return document.endswith(".pdf")
