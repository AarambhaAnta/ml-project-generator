import os

def create_ml_project_structure(project_name="my_ml_project"):
    """
    Creates a standard machine learning project file structure.
    
    Args:
        project_name (str): The name of the project directory.
    """
    
    # Define the directories to create
    dirs = [
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

    # Create the directories
    for dir_path in dirs:
        os.makedirs(dir_path, exist_ok=True)
    
    # Create essential files
    files = {
        os.path.join(project_name, "requirements.txt"): "# Project dependencies\n",
        os.path.join(project_name, "README.md"): f"# {project_name}\n\nProject Description:\n\nInstallation:\n\nUsage:\n",
        os.path.join(project_name, "src", "__init__.py"): "# src package initializer\n",
        os.path.join(project_name, "src", "main.py"): "# Main project script\n"
    }

    for file_path, content in files.items():
        with open(file_path, "w") as f:
            f.write(content)
    
    print(f"Project structure '{project_name}' created successfully.")
