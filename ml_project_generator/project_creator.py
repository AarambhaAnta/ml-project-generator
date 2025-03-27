import os
import sys
import subprocess
import logging

def create_ml_project_structure(project_name="my_ml_project"):
    """
    Creates a standard machine learning project file structure and sets up a virtual environment.    
    Args:
        project_name (str): The name of the project directory.
    """
    
    logging.basicConfig(level=logging.INFO, format="%(message)s")

    # Define the directories to create
    dirs = [
        os.path.join(project_name, "data", "raw"),
        os.path.join(project_name, "data", "processed"),
        os.path.join(project_name, "data", "external"),
        os.path.join(project_name, "data", "interim"),
        os.path.join(project_name, "models","logs"),
        os.path.join(project_name, "notebooks"),
        os.path.join(project_name, "src", "data"),
        os.path.join(project_name, "src", "models"),
        os.path.join(project_name, "src", "utils"),
        os.path.join(project_name, "reports","figures"),
        os.path.join(project_name, "config"),
        os.path.join(project_name, "tests"),
        os.path.join(project_name, "scripts"),
        os.path.join(project_name, "docker"),
    ]

    try:
        # Create the directories
        for dir_path in dirs:
            os.makedirs(dir_path, exist_ok=True)
    
        # Create essential files
        files = {
            os.path.join(project_name, "requirements.txt"): "# Project dependencies\n",
            os.path.join(project_name, "README.md"): f"# {project_name}\n\n## Project Description:\n\n## Installation:\n\n## Usage:\n",
            os.path.join(project_name, ".gitignore"): "# Ignore unnecessary files\nvenv/\n__pycache__/\n.DS_Store",
            os.path.join(project_name, "pyproject.toml"): "# Project metadata & config\n",
            os.path.join(project_name, ".env"): "# Environment variables\n",
            os.path.join(project_name, "src", "__init__.py"): "# src package initializer\n",
            os.path.join(project_name, "src", "main.py"): "# Main pipeline execution script\n",
            os.path.join(project_name, "src", "config.py"): "# Configuration settings\n",
            os.path.join(project_name, "src", "data", "load_data.py"): "# Data loading functions\n",
            os.path.join(project_name, "src", "data", "preprocess.py"): "# Data cleaning & feature engineering\n",
            os.path.join(project_name, "src", "data", "split_data.py"): "# Train-test split\n",
            os.path.join(project_name, "src", "models", "train.py"): "# Model training script\n",
            os.path.join(project_name, "src", "models", "evaluate.py"): "# Model evaluation\n",
            os.path.join(project_name, "src", "models", "predict.py"): "# Making predictions\n",
            os.path.join(project_name, "src", "models", "save_model.py"): "# Save & load models\n",
            os.path.join(project_name, "src", "models", "model_config.py"): "# Model hyperparameters\n",
            os.path.join(project_name, "src", "utils", "logger.py"): "# Logging utilities\n",
            os.path.join(project_name, "src", "utils", "metrics.py"): "# Custom metric functions\n",
            os.path.join(project_name, "src", "utils", "visualization.py"): "# Data & model visualizations\n",
            os.path.join(project_name, "notebooks", "01_data_exploration.ipynb"): "{}",
            os.path.join(project_name, "notebooks", "02_feature_engineering.ipynb"): "{}",
            os.path.join(project_name, "notebooks", "03_model_training.ipynb"): "{}",
            os.path.join(project_name, "notebooks", "04_model_evaluation.ipynb"): "{}",
            os.path.join(project_name, "notebooks", "05_predictions.ipynb"): "{}",
            os.path.join(project_name, "tests", "__init__.py"): "# Tests package initializer\n",
            os.path.join(project_name, "tests", "test_data.py"): "# Unit tests for data processing\n",
            os.path.join(project_name, "tests", "test_models.py"): "# Unit tests for model training & evaluation\n",
            os.path.join(project_name, "tests", "test_utils.py"): "# Unit tests for utility functions\n",
            os.path.join(project_name, "scripts", "train.sh"): "# Training automation script\n",
            os.path.join(project_name, "scripts", "preprocess.sh"): "# Preprocessing automation script\n",
            os.path.join(project_name, "scripts", "run_pipeline.sh"): "# Full pipeline execution script\n",
            os.path.join(project_name, "docker", "Dockerfile"): "# Docker configuration\n",
            os.path.join(project_name, "docker", "docker-compose.yml"): "# Docker Compose configuration\n",
            os.path.join(project_name, "reports", "summary.md"): "# Project Summary\n",
        }
        
        # Create files
        for file_path, content in files.items():
            with open(file_path, "w") as f:
                f.write(content)

        logging.info(f"✅ Project structure '{project_name}' created successfully.")

        # Create virtual environment
        create_virtual_environment(project_name)
    
    except Exception as e:
        logging.error(f"❌ Error creating project: {e}")
        sys.exit(1)

def create_virtual_environment(project_name):
    """Creates a virtual environment inside the project directory."""
    venv_path = os.path.join(project_name, "venv")

    try:
        subprocess.run([sys.executable, "-m", "venv", venv_path], check=True)
        logging.info(f"✅ Virtual environment created at '{venv_path}'.")
        logging.info(f"💡 Activate it using: \n -Windows: `{venv_path}\\scripts\\activate`\n -macOS/Linux: `source {venv_path}/bin/activate`")
    except subprocess.CalledProcessError as e:
        logging.error(f"❌ Failed to create virtual environment: {e}")


