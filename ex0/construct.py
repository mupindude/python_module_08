import os
import sys
import site


def main():
    # Detect if we are inside a virtual environment
    # Fallback to sys.real_prefix for older virtualenv tools
    inside = hasattr(sys, "real_prefix") or (
        hasattr(sys, "base_prefix") and sys.prefix != sys.base_prefix
    )

    if not inside:
        # --- OUTSIDE THE MATRIX ---
        print("MATRIX STATUS: You're still plugged in")
        print(f"Current Python: {sys.executable}")
        print("Virtual Environment: None detected")
        print("\nWARNING: You're in the global environment!")
        print("The machines can see everything you install.\n")
        print("To enter the construct, run:")
        print("python -m venv matrix_env")
        print("source matrix_env/bin/activate # On Unix")
        print("matrix_env\\Scripts\\activate # On Windows\n")
        print("Then run this program again.")

    else:
        # --- INSIDE THE CONSTRUCT ---
        env_path = sys.prefix
        env_name = os.path.basename(env_path)

        # Safely extract the site-packages path for the active venv
        site_packages = "Not found"
        try:
            for path in site.getsitepackages():
                if path.startswith(env_path):
                    site_packages = path
                    break
        except AttributeError:
            # Fallback if getsitepackages() is unavailable in this environment
            for path in sys.path:
                if "site-packages" in path and path.startswith(env_path):
                    site_packages = path
                    break

        print("MATRIX STATUS: Welcome to the construct")
        print(f"Current Python: {sys.executable}")
        print(f"Virtual Environment: {env_name}")
        print(f"Environment Path: {env_path}")
        print("\nSUCCESS: You're in an isolated environment!")
        print("Safe to install packages without affecting\nthe global system.\n")
        print("Package installation path:")
        print(site_packages)


if __name__ == "__main__":
    main()
