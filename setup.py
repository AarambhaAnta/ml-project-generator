from setuptools import setup, find_packages

setup(
    name='ml-project-generator',
    version='0.1.0',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'ml-gen = ml_project_generator.main:main',
        ],
    },
    install_requires=[],
    author="@AarambhaAnta",
    description="A Python package for quickly setting up ML project structures.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/AarambhaAnta/ml-project-generator",  # Change to your GitHub
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
