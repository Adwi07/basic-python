import logging
from pathlib import Path

logger = logging.getLogger(__name__)


def read_file():
    """Read and display the contents of a text file."""

    file_name = input("Enter the file path to read: ").strip()

    if not file_name:
        logger.warning("Read operation requested with an empty path")
        print("File path cannot be empty.")
        return

    try:
        file_path = Path(file_name)

        with file_path.open("r", encoding="utf-8") as file:
            content = file.read()

        if not content.strip():
            logger.warning("File was empty: %s", file_path)
            print("The file is empty.")
            return

        print("\n--- File Contents ---")
        print(content)

        logger.info("File read successfully: %s", file_path)

    except FileNotFoundError:
        logger.error("File could not be found: %s", file_name)
        print("Error: File does not exist.")

    except PermissionError:
        logger.error("Permission denied while reading: %s", file_name)
        print("Error: Permission denied.")

    except OSError:
        logger.exception("Operating system error while reading: %s", file_name)
        print("Error: Unable to read the file.")


def write_file():
    """Write user-provided text to a file."""

    file_name = input("Enter the file path to write: ").strip()

    if not file_name:
        logger.warning("Write operation requested with an empty path")
        print("File path cannot be empty.")
        return

    content = input("Enter the content to save: ")

    try:
        file_path = Path(file_name)

        with file_path.open("w", encoding="utf-8") as file:
            file.write(content)

        logger.info("File written successfully: %s", file_path)
        print("File written successfully.")

    except FileNotFoundError:
        logger.error("Destination directory does not exist: %s", file_name)
        print("Error: The destination directory does not exist.")

    except PermissionError:
        logger.error("Permission denied while writing: %s", file_name)
        print("Error: Permission denied.")

    except OSError:
        logger.exception("Operating system error while writing: %s", file_name)
        print("Error: Unable to write the file.")