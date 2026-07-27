"""Project-wide pytest fixtures shared across the test suite."""

import os

import pytest


@pytest.fixture(name="user")
def user_() -> str:
    """Local USER string read from the USER pytest.ini variable."""
    return os.environ["USER"]


@pytest.fixture(name="project_id")
def project_id_() -> str:
    """Google Cloud Project ID string read from the PROJECT_ID pytest.ini variable."""
    return os.environ["PROJECT_ID"]


@pytest.fixture(name="location")
def location_() -> str:
    """GCP region/location string read from the LOCATION pytest.ini variable."""
    return os.environ["LOCATION"]


@pytest.fixture(name="env")
def env_() -> str:
    """Deployment environment string read from the ENVIRONMENT pytest.ini variable."""
    return os.environ["ENVIRONMENT"]
