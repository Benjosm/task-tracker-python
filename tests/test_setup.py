# tests/test_setup.py

import os
import re

def test_setup_file_exists():
    assert os.path.exists('setup.py')

def test_setup_file_content():
    with open('setup.py', 'r') as f:
        setup_content = f.read()

    assert 'name="task_manager"' in setup_content
    assert 'version="0.1.0"' in setup_content
    assert 'description=' in setup_content
    assert 'packages=find_packages()' in setup_content
    assert 'entry_points={' in setup_content
    assert 'install_requires' not in setup_content # Verify no dependencies are listed
