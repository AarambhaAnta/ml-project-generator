import os

def create_ml_project_structure(project_name="my_ml_project"):
    """
    Creates a structured folder layout for ML projects.
    
    Args:
        project_name (str): Name of the root project folder.
    """

    # Define required directories
    directories = [
        os.path.join(project_name, "data", "raw"),
        os.path.join(project_name, "data", "processed"),
        os.path.join(project_name, "models"),
        os.path.join(project_name, "notebooks"),
        os.path.join(project_name, "src", "data"),
        os.path.join(project_name, "src", "models"),
        os.path.join(project_name, "src", "utils"),
        os.path.join(project_name, "reports"),
        os.path.join(project_name, "config"),
        os.path.join(project_name, "tests"),
    ]

    # Create directories
    for directory in directories:
        os.makedirs(directory, exist_ok=True)

    # Create essential files
    files = {
        "README.md": f"# {project_name}\n\nProject Description:\n\nInstallation:\n\nUsage:\n",
        "requirements.txt": "# List your dependencies here",
        "src/__init__.py": "# Initialize the src package",
        "src/main.py": "# Main script entry point",
    }

    for file_path, content in files.items():
        full_path = os.path.join(project_name, file_path)
        with open(full_path, "w") as f:
            f.write(content)

    print(f"✅ Project structure '{project_name}' created successfully.")
