from setuptools import setup, find_packages

setup(
    name="ml_project_generator",
    version="0.1.0",
    description="A tool to generate ML project structures",
    author="@AarambhaAnta",
    author_email="aarambha108@gmail.com",
    license="MIT",
    packages=find_packages(),
    install_requires=[
        "numpy",
        "pandas",
        "scikit-learn"
    ],
    python_requires=">=3.6",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={
        "console_scripts": [
            "ml-gen = ml_project_generator.main:main"
        ]
    }
)
