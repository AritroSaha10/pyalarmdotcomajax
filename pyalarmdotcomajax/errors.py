"""Exceptions."""
from __future__ import annotations


class UnsupportedDevice(Exception):
    """pyalarmdotcomajax encountered a device not currently supported by the package."""


class AuthenticationFailed(Exception):
    """Alarm.com authentication failure."""


class DataFetchFailed(Exception):
    """General or connection error encountered when fetching data."""


class UnexpectedDataStructure(Exception):
    """Successfully received JSON object, but format is not as expected."""