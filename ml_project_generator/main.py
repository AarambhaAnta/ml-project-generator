import argparse
import sys
from ml_project_generator.project_creator import create_ml_project_structure, create_virtual_environment


def main():
    """
    Command-line interface for generating a ML project structure.
    """

    parser = argparse.ArgumentParser(description="Create a structured ML project.")
    parser.add_argument("project_name", nargs="?", help="Name of the project directory.")
    parser.add_argument("--venv", action="store_true", help="Create a virtual environment in the project.")

    args = parser.parse_args()

    # Use provided name or prompt interactively
    project_name = args.project_name.strip() if args.project_name else input("Enter project name (default: my_ml_project): ").strip() or "my_ml_project"

    print(f"\n🚀 Setting up ML project: {project_name} ...\n")

    try:
        create_ml_project_structure(project_name)

        if args.venv:
            create_virtual_environment(project_name)

        print(f"\n🎉 Project '{project_name}' is ready to go!")

    except PermissionError:
        print("❌ Permission denied! Try running with elevated privileges.")
        sys.exit(1)
    except Exception as e:
        print(f"❌ An error occured: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()