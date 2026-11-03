import logging

from LoggingPY.ActivityManager.exceptions import InvalidOperationError

from .exceptions import InvalidOperationError

logger = logging.getLogger(__name__)


def calculate():
    """Perform a basic arithmetic calculation."""

    try:
        first_number = float(input("Enter the first number: "))
        second_number = float(input("Enter the second number: "))

        logger.debug(
            "Calculation operands: %s and %s",
            first_number,
            second_number
        )

        print("\n1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")

        choice = input("Choose an operation: ").strip()

        if choice == "1":
            result = first_number + second_number
            operation = "addition"

        elif choice == "2":
            result = first_number - second_number
            operation = "subtraction"

        elif choice == "3":
            result = first_number * second_number
            operation = "multiplication"

        elif choice == "4":
            if second_number == 0:
                logger.warning("Division by zero attempted")
                print("Cannot divide by zero.")
                return

            result = first_number / second_number
            operation = "division"

        else:
            logger.warning("Invalid calculation choice: %s", choice)
            raise InvalidOperationError(
            "Unsupported calculation operation"
            )

        print(f"Result: {result}")

        logger.info("Calculation completed: %s", operation)

    except ValueError:
        logger.warning("Invalid numeric input during calculation")
        print("Please enter valid numbers.")