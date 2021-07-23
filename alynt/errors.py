class AlyntException(Exception):
    """Base class for Alynt.py exceptions."""


class HTTPException(AlyntException):
    """Base class for HTTP exceptions."""


class UnauthorizedError(HTTPException):
    pass
