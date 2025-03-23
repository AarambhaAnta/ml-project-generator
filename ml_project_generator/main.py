import argparse
from ml_project_generator.project_creator import create_ml_project_structure

def main():
    """
    Command-line interface for the ML project generator.
    """
    parser = argparse.ArgumentParser(description="Create a structured ML project.")
    parser.add_argument("project_name", nargs="?", default="my_ml_project", help="Project directory name.")
    args = parser.parse_args()

    create_ml_project_structure(args.project_name)

if __name__ == "__main__":
    main()
