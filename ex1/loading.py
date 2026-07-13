import sys
import importlib


def check_pkg(name, description):
    try:
        module = importlib.import_module(name)
        version = getattr(module, "__version__", "unknown")
        print(f"[OK] {name} ({version}) - {description}")
        return module
    except ImportError:
        print(f"[MISSING] {name} - {description}")
        return None


def installation_help():
    print("\nOne or more required packages are missing.\n")

    print("Install using pip:")
    print("    pip install -r requirements.txt\n")

    print("Or install using Poetry:")
    print("    poetry install")


def compare_package_management():
    """Display a brief comparison of pip and Poetry."""
    print("\nDependency Management")
    print("---------------------")
    print("pip:")
    print(" - Uses requirements.txt")
    print(" - Installs packages into the current environment")
    print()

    print("Poetry:")
    print(" - Uses pyproject.toml")
    print(" - Manages dependencies and virtual environments")
    print()


def main():
    print("LOADING STATUS: Loading programs...\n")

    print("Checking dependencies:")

    pandas = check_pkg("pandas", "Data manipulation ready")
    numpy = check_pkg("numpy", "Numerical computation ready")
    matplotlib = check_pkg("matplotlib", "Visulization ready")

    # requests is optional
    requests = check_pkg("requests", "Network access ready")

    if pandas is None or numpy is None or matplotlib is None:
        installation_help()
        sys.exit(1)

    compare_package_management()

    pd = pandas
    np = numpy
    try:
        plt = importlib.import_module("matplotlib.pyplot")
    except ImportError:
        print("[MISSING] matplotlib.pyplot")
        installation_help()
        sys.exit(1)

    print("Analyzing Matrix data...")
    time = np.arange(1000)
    signal = np.sin(time / 50) + np.random.normal(0, 0.2, 1000)

    print(f"Processing {len(time)} data points...")

    # cretae a DataFrame
    df = pd.DataFrame({"Time": time, "Signal": signal})

    print("\nStatistics:")
    print(df.describe())

    print("\nGenerating visualization...")

    plt.figure(figsize=(8, 4))
    plt.plot(df["Time"], df["Signal"])
    plt.tittle("Matrix Signal Analysis")
    plt.xlabel("Time")
    plt.ylabel("Signal Strength")
    plt.grid(True)

    filename = "matrix_analysis.png"
    plt.savefig(filename)
    print("\nAnalysis complete!")
    print(f"Results saved to: {filename}")


if __name__ == "__main__":
    main()
