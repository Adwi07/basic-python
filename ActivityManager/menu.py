import logging

from .auth import login, logout
from .calculator import calculate
from .file_operations import read_file, write_file
from .exceptions import InvalidOperationError

logger = logging.getLogger(__name__)


def display_menu():
    """Display the main application menu."""

    print("\n" + "=" * 40)
    print("       LOGGING ACTIVITY MANAGER")
    print("=" * 40)
    print("1. Login")
    print("2. Calculate")
    print("3. Read a File")
    print("4. Write a File")
    print("5. Logout")
    print("=" * 40)


def run_menu():
    """Run the menu until the user logs out."""

    current_user = None

    logger.info("Application menu started")

    while True:
        display_menu()
        choice = input("Enter your choice: ").strip()

        try:
            if choice == "1":
                if current_user is not None:
                    logger.warning("Login attempted while already logged in")
                    print("You are already logged in.")
                    continue

                current_user = login()

            elif choice == "2":
                if current_user is None:
                    logger.warning("Calculation attempted without login")
                    print("Please log in first.")
                    continue

                calculate()

            elif choice == "3":
                if current_user is None:
                    logger.warning("File read attempted without login")
                    print("Please log in first.")
                    continue

                read_file()

            elif choice == "4":
                if current_user is None:
                    logger.warning("File write attempted without login")
                    print("Please log in first.")
                    continue

                write_file()

            elif choice == "5":
                if current_user is not None:
                    logout(current_user)
                    current_user = None
                else:
                    logger.info("Application exited without an active session")
                    print("No user was logged in.")

                logger.info("Application menu stopped")
                break

            else:
                logger.warning("Invalid menu choice: %s", choice)
                print("Invalid choice. Please select 1 to 5.")

        except InvalidOperationError as error:
            logger.warning("Calculation operation rejected: %s", error)
            print(f"Invalid operation: {error}")

        except Exception:
            logger.critical(
           "Unexpected application failure during menu operation",
            exc_info=True
            )
        print("An unexpected error occurred. Check the log files.")
        print("The application will continue.")