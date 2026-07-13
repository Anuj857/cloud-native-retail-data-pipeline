"""
Custom Exceptions
"""


class APIException(Exception):
    """Raised when API call fails."""


class ValidationException(Exception):
    """Raised when data validation fails."""


class StorageException(Exception):
    """Raised when upload fails."""


class TransformationException(Exception):
    """Raised during transformation."""