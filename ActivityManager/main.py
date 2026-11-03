import logging

from .logging_config import configure_logging
from .menu import run_menu



def main():
    """Initialize and start the application."""

    configure_logging()

    logger = logging.getLogger(__name__)
    logger.info("Application started")

    try:
        run_menu()

    except KeyboardInterrupt:
        logger.warning("Application interrupted by the user")
        print("\nApplication interrupted.")

    except Exception:
        logger.critical(
            "Unexpected application failure",
            exc_info=True
        )
        print("A critical error occurred. Check the log files.")

    finally:
        logger.info("Application shutting down")
        print("Application closed.")


if __name__ == "__main__":
    main()