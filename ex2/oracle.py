import os
import sys
from dotenv import load_dotenv

# Load variables from .env if it exists
load_dotenv()


def get_config(name, default=None):
    """Retrieve an environment variable."""
    value = os.getenv(name)

    if value is None:
        return default
    return value


def check_config(name):
    """Display whether a required configuration exists."""
    value = os.getenv(name)

    if value:
        print(f"[OK] {name}: {value}")
        return True

    print(f"[WARNING] {name} is not configured.")
    return False


def main():
    print("ORACLE STATUS: Reading the Matrix...\n")

    mode = get_config("MATRIX_MODE", "development")
    database = get_config("DATABASE_URL")
    api_key = get_config("API_KEY")
    log_level = get_config("LOG_LEVEL", "INFO")
    zion = get_config("ZION_ENDPOINT")

    print("Configuration loaded:")
    print(f"Mode: {mode}")

    if database:
        print(f"Database: {database}")
    else:
        print("Database: Not configured")

    if api_key:
        print("API Access: Authenticated")
    else:
        print("API Access: Missing API key")

    print(f"Log Level: {log_level}")

    if zion:
        print(f"Zion Network: {zion}")
    else:
        print("Zion Network: Offline")

    print("\nEnvironment security check:")

    check_config("DATABASE_URL")
    check_config("API_KEY")
    check_config("ZION_ENDPOINT")

    if mode.lower() == "development":
        print("\nDevelopment mode enabled.")
        print("Verbose debugging is available.")

    elif mode.lower() == "production":
        print("\nProduction mode enabled.")
        print("Debugging disabled.")
        print("Security settings enabled.")

    else:
        print("\nUnknown MATRIX_MODE.")
        sys.exit(1)


if __name__ == "__main__":
    main()
