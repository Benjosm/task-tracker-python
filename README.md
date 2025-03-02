# Task Manager

A simple command-line task management application built with Python.

## Features

- Add tasks with title, description, due date, and priority
- List all tasks (pending or all)
- Mark tasks as completed
- Delete tasks
- View detailed task information
- Get task statistics

## Installation

Clone the repository and install using pip:

```bash
git clone https://github.com/yourusername/task-manager.git
cd task-manager
pip install -e .
```

## Usage

After installation, you can use the `taskman` command from anywhere:

```bash
# Add a new task
taskman add "Implement new feature" -d "Add user authentication" --due 2025-04-01 -p high

# List all pending tasks
taskman list

# List all tasks including completed ones
taskman list -a

# View detailed information
taskman list -v

# Complete a task
taskman complete TASK_ID

# Delete a task
taskman delete TASK_ID

# View a specific task
taskman view TASK_ID

# Show task statistics
taskman stats
```

## Project Structure

- `task.py`: Defines the Task class
- `task_storage.py`: Handles persistence of tasks
- `task_manager.py`: Main logic for managing tasks
- `task_cli.py`: Command-line interface
- `main.py`: Entry point script

## Requirements

- Python 3.8 or higher

## License

MIT