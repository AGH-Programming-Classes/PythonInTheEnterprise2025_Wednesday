# Hello World Project

A starting template for your project, following a modern Python project structure.

## Project Layout

```
hello_world_project/
├── src/hello_world_project/
│   ├── main.py
│   ├── utils.py
│   ├── example_module.py
│   └── __init__.py
├── tests/
│   └── test_example_module.py
├── pyproject.toml
├── requirements.txt
├── setup.cfg
└── README.md
```

## Quick Start

### 1. Create and activate a virtual environment
```bash
python -m venv venv
source venv/bin/activate     # macOS/Linux
```

### 2. Install the project to make it visible to Python
```bash
pip install -e .
```
Alternatively, you can temporarily point PYTHONPATH to src.

### 2. Run the application
```bash
python -m hello_world_project.main
```

## Running Tests

Run all tests:
```bash
python -m unittest discover -s tests
```