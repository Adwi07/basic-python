import logging

logger = logging.getLogger(__name__)


def login():
    """Log in a user using a non-empty username."""

    username = input("Enter your username: ").strip()

    if not username:
        logger.warning("Login attempted with an empty username")
        print("Username cannot be empty.")
        return None

    logger.info("User logged in: %s", username)
    print(f"Welcome, {username}!")

    return username


def logout(username):
    """Log out the current user."""

    logger.info("User logged out: %s", username)
    print(f"Goodbye, {username}!")