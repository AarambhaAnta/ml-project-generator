"""
ML Project Generator - A tool to generate structured ML project templates
"""

__version__ = "0.1.1"

from .project_creator import create_ml_project_structure, create_virtual_environment

__all__ = ["create_ml_project_structure", "create_virtual_environment"]
