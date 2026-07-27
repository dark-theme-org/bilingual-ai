"""Liveness probe for the BIlingual AI application."""


def ping() -> str:
    """Return a liveness signal."""
    return "pong"
