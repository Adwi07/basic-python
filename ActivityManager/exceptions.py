class ApplicationError(Exception):
    """Base exception for application-specific errors."""


class AuthenticationError(ApplicationError):
    """Raised when an authentication operation fails."""


class InvalidOperationError(ApplicationError):
    """Raised when an unsupported operation is requested."""