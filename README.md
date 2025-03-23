# ML Project Generator

🚀 **ml-project-generator** is a Python package that automates the creation of a structured file system for machine learning projects. This ensures consistency, improves organization, and helps you focus on development rather than setup.

## 📌 Features
- Automatically generates an ML project folder structure.
- Includes essential directories such as `data`, `models`, `notebooks`, `src`, etc.
- Creates key files: `README.md`, `requirements.txt`, `__init__.py`, and `main.py`.
- Easy-to-use CLI command: `ml-gen <project_name>`.

## 📥 Installation

You can install the package directly from GitHub (Recomended):
```sh
pip install git+https://github.com/AarambhaAnta/ml-project-generator.git
```
Or, clone the repository and install manually:
```sh
git clone https://github.com/AarambhaAnta/ml-project-generator.git
cd ml-project-generator
pip install .
```

## 🚀 Usage

To generate an ML project structure, simply run:
```sh
ml-gen my_new_ml_project
```
This will create a structured directory like:
```
my_new_ml_project/
│── data/
│   ├── raw/
│   ├── processed/
│── models/
│── notebooks/
│── src/
│   ├── data/
│   ├── models/
│   ├── utils/
│── config/
│── reports/
│── tests/
│── README.md
│── requirements.txt
│── src/main.py
```

## 🛠 Development & Contribution

1. Clone the repository:
   ```sh
   git clone https://github.com/AarambhaAnta/ml-project-generator.git
   ```
2. Create a virtual environment:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On macOS/Linux
   venv\Scripts\activate  # On Windows
   ```
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
4. Run the project in development mode:
   ```sh
   python src/main.py
   ```
5. Submit a pull request if you improve or add features! 🚀

## 📜 License
This project is licensed under the **MIT License**. See [LICENSE](LICENSE) for details.

---

🙌 **Contributions are welcome!** Feel free to submit PRs, open issues, or suggest improvements. Happy coding! 🚀