import argparse
import os
from ml_project_generator.project_creator import create_ml_project_structure


def main():
    """
    Command-line interface for generating an ML project structure.
    """
    parser = argparse.ArgumentParser(description="Create a machine learning project structure.")
    parser.add_argument("project_name", nargs="?", default="my_ml_project", help="Name of the project directory.")
    args = parser.parse_args()
    project_name = args.project_name.strip() if args.project_name else "my_ml_project"
    
    create_ml_project_structure(project_name)


if __name__ == "__main__":
    main()
