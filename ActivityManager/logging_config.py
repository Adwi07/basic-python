import logging
from pathlib import Path


# Find the directory containing this Python file.
BASE_DIR = Path(__file__).resolve().parent

# Create the logs directory path.
LOG_DIR = BASE_DIR / "logs"

# Define the two log file paths.
APPLICATION_LOG = LOG_DIR / "application.log"
ERROR_LOG = LOG_DIR / "error.log"


def configure_logging():
    """Configure application-wide logging."""

    # Create logs/ if it does not exist.
    LOG_DIR.mkdir(parents=True, exist_ok=True)

    # Define the format of each log message.
    log_format = (
        "%(asctime)s | %(levelname)-8s | "
        "%(name)s | %(message)s"
    )

    # Get the root logger.
    root_logger = logging.getLogger()

    # Prevent duplicate handlers if configuration runs again.
    if root_logger.handlers:
        return

    root_logger.setLevel(logging.DEBUG)

    # Handler for all application messages.
    application_handler = logging.FileHandler(
        APPLICATION_LOG,
        encoding="utf-8"
    )
    application_handler.setLevel(logging.DEBUG)

    # Handler for errors and critical failures only.
    error_handler = logging.FileHandler(
        ERROR_LOG,
        encoding="utf-8"
    )
    error_handler.setLevel(logging.ERROR)

    # Apply the same message format to both handlers.
    formatter = logging.Formatter(log_format)
    application_handler.setFormatter(formatter)
    error_handler.setFormatter(formatter)

    # Attach both handlers to the root logger.
    root_logger.addHandler(application_handler)
    root_logger.addHandler(error_handler)