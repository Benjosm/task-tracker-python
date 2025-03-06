# tests/test_readme.py
import os

def test_readme_contains_installation_instructions():
    readme_path = "README.md"
    assert os.path.exists(readme_path), "README.md file not found"
    with open(readme_path, "r") as f:
        readme_content = f.read()
    assert "## Installation" in readme_content, "README.md does not contain installation instructions"

def test_readme_contains_usage_instructions():
    readme_path = "README.md"
    assert os.path.exists(readme_path), "README.md file not found"
    with open(readme_path, "r") as f:
        readme_content = f.read()
    assert "## Usage" in readme_content, "README.md does not contain usage instructions"
