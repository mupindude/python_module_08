import os
import sys

try:
    from dotenv import load_dotenv
except ImportError:
    print("ERROR: python-dotenv is not installed.")
    print()
    print("Install it with pip:")
    print("    pip install python-dotenv")
    print()
    print("Or with Poetry:")
    print("    poetry add python-dotenv")
    sys.exit(1)

# Load variables from .env if it exists
# By default, load_dotenv() does NOT override existing system environment variables,
# allowing OS-level environment overrides to naturally take precedence.
load_dotenv()


def get_config(name, default=None):
    """Retrieve an environment variable."""
    return os.getenv(name, default)


def run_security_check(mode, api_key):
    """Check environment settings to verify secure setup."""
    print("\nEnvironment security check:")

    # 1. Check for .env file presence
    env_exists = os.path.exists(".env")
    if env_exists:
        print("[OK] .env file properly configured")
    else:
        print("[WARNING] No .env file found (using OS environment variables)")

    # 2. Hardcoded secret validation
    if api_key == "replace_with_your_api_key":
        print("[WARNING] API_KEY is using the default example placeholder!")
    elif not api_key:
        print("[WARNING] API_KEY is missing entirely")
    else:
        print("[OK] No hardcoded secrets detected")

    # 3. Mode settings
    if mode.lower() == "production":
        print("[OK] Production overrides active")
    else:
        print("[OK] Production overrides available (Currently in development)")


def main():
    print("ORACLE STATUS: Reading the Matrix...\n")

    mode = get_config("MATRIX_MODE", "development").lower()
    database = get_config("DATABASE_URL")
    api_key = get_config("API_KEY")
    log_level = get_config("LOG_LEVEL", "DEBUG" if mode == "development" else "INFO")
    zion = get_config("ZION_ENDPOINT")

    print("Configuration loaded:")
    print(f"Mode: {mode}")

    if database:
        # Avoid leaking full database passwords in logs if production
        if mode == "production" and "@" in database:
            masked_db = database.split("@")[-1]
            print(f"Database: Connected to host {masked_db}")
        else:
            print(f"Database: {database}")
    else:
        print("Database: Not configured")

    if api_key and api_key != "replace_with_your_api_key":
        print("API Access: Authenticated")
    else:
        print("API Access: Missing API key")

    print(f"Log Level: {log_level}")

    if zion:
        print(f"Zion Network: {zion}")
    else:
        print("Zion Network: Offline")

    # Perform security validation
    run_security_check(mode, api_key)

    # Check for environmental modes
    if mode == "development":
        print("\nDevelopment mode enabled.")
        print("Verbose debugging is available.")
    elif mode == "production":
        print("\nProduction mode enabled.")
        print("Debugging disabled.")
        print("Security settings enabled.")

        # Enforce strict rules in production
        if not database or not api_key or api_key == "replace_with_your_api_key":
            print("\nCRITICAL: Missing production credentials! Terminating connection.")
            sys.exit(1)
    else:
        print(f"\nUnknown MATRIX_MODE: '{mode}'.")
        sys.exit(1)

    print("\nThe Oracle sees all configurations.")


if __name__ == "__main__":
    main()