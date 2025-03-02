"""
Setup script for the Task Manager package.
"""
from setuptools import setup, find_packages

setup(
    name="task_manager",
    version="0.1.0",
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'taskman=task_cli:main',
        ],
    },
    author="Your Name",
    author_email="your.email@example.com",
    description="A simple command-line task management application",
    keywords="task, todo, management",
    url="https://github.com/yourusername/task-manager",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    python_requires=">=3.8",
)
