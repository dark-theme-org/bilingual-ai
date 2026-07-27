"""Tests for app.health."""

from app.health import ping


def test_ping() -> None:
    """ping returns the liveness string."""
    assert ping() == "pong"
