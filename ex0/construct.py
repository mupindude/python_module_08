import sys
import os
import site


def main():
    inside: bool = sys.prefix != sys.base_prefix

    if inside:
        print("Virtual environment detected.")
    else:
        print("No virtual environment detected.")

    print("\nPython executable:")
    print(sys.executable)

    print("\nPython version:")
    print(sys.version)

    print("\nCurrent prefix:")
    print(sys.prefix)

    print("Base prefix:")
    print(sys.base_prefix)

    print("Package locations:")
    for path in site.getsitepackages():
        print(path)

    if not inside:
        print("\nMATRIX STATUS: You're still plugged in")
        print("\nTo enter the construct run:")
        print("python3 -m venv matrix_env")
        print("Activate it:")
        print("source matrix_env/bin/activate")
    else:
        print("\nEnvironment name:")
        print(os.path.basename(sys.prefix))


if __name__ == "__main__":
    main()
