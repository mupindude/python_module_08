import sys
import importlib

# Standard metadata for checking dependencies
REQUIRED_PKGS = {
    "pandas": "Data manipulation ready",
    "numpy": "Numerical computation ready",
    "matplotlib": "Visualization ready"
}

# Optional packages
OPTIONAL_PKGS = {
    "requests": "Network access ready"
}


def check_pkg(name, description):
    """Safely check if a package is installed and get its version."""
    try:
        module = importlib.import_module(name)
        version = getattr(module, "__version__", "unknown")
        print(f"[OK] {name} ({version}) - {description}")
        return module
    except ImportError:
        print(f"[MISSING] {name} - {description}")
        return None


def installation_help():
    """Display help details for installing dependencies."""
    print("\nOne or more required packages are missing.\n")
    print("Install using pip:")
    print("    pip install -r requirements.txt\n")
    print("Or install using Poetry:")
    print("    poetry install")


def compare_package_management():
    """Display a direct comparison showing the differences between pip and Poetry."""
    print("\n" + "=" * 40)
    print("      PIP vs POETRY COMPARISON")
    print("=" * 40)
    print("pip:")
    print("  - Dependency file: requirements.txt (Flat list of packages)")
    print("  - Scope: Installs globally or to the active environment")
    print("  - Lockfile: None by default (must manually freeze)")
    print("\nPoetry:")
    print("  - Dependency file: pyproject.toml (Structured project config)")
    print("  - Scope: Automatically creates and isolated virtual environments")
    print("  - Lockfile: poetry.lock (Guarantees deterministic builds)")
    print("=" * 40 + "\n")


def main():
    print("LOADING STATUS: Loading programs...")
    print("Checking dependencies:")

    # Verify required packages
    loaded_pkgs = {}
    missing_required = False

    for pkg, desc in REQUIRED_PKGS.items():
        mod = check_pkg(pkg, desc)
        if mod is None:
            missing_required = True
        else:
            loaded_pkgs[pkg] = mod

    # Verify optional packages (requests)
    loaded_requests = check_pkg("requests", OPTIONAL_PKGS["requests"])

    # If critical dependencies are missing, stop here
    if missing_required:
        installation_help()
        sys.exit(1)

    # If clean, proceed with displaying package manager comparison
    compare_package_management()

    # Dynamic binding to avoid top-level unresolved import warnings in static checkers
    pd = loaded_pkgs["pandas"]
    np = loaded_pkgs["numpy"]

    try:
        # Load matplotlib backend safely
        plt = importlib.import_module("matplotlib.pyplot")
    except ImportError:
        print("[MISSING] matplotlib.pyplot visualization library is broken.")
        installation_help()
        sys.exit(1)

    print("Analyzing Matrix data...")
    # Generate data cleanly using numpy
    time = np.arange(1000)
    signal = np.sin(time / 50) + np.random.normal(0, 0.2, 1000)

    print(f"Processing {len(time)} data points...")

    # Create DataFrame
    df = pd.DataFrame({"Time": time, "Signal": signal})

    print("\nMatrix Statistics Summary:")
    print(df.describe())

    print("\nGenerating visualization...")
    plt.figure(figsize=(10, 5))
    plt.plot(df["Time"], df["Signal"], color="#00FF00", label="Matrix Signal")
    plt.title("Matrix Signal Analysis", fontsize=14)
    plt.xlabel("Time (ticks)", fontsize=11)
    plt.ylabel("Signal Strength", fontsize=11)
    plt.grid(True, linestyle="--", alpha=0.6)
    plt.legend()

    filename = "matrix_analysis.png"
    plt.savefig(filename)
    plt.close()  # Clean up memory resource

    print("Analysis complete!")
    print(f"Results saved to: {filename}")


if __name__ == "__main__":
    main()