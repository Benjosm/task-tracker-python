"""
Task Manager CLI - Command-line interface for the Task Manager application.

This module provides the command-line interface for interacting with the
Task Manager application.
"""
import argparse
import datetime
import sys
from task_manager import TaskManager


def format_task_output(task, verbose=False):
    """Format a task for display.

    Args:
        task: The task to format
        verbose (bool): Whether to show detailed information

    Returns:
        str: Formatted task string
    """
    status = "✓" if task.completed else "☐"
    
    if verbose:
        result = f"{status} [{task.id}] {task.title} (Priority: {task.priority})\n"
        result += f"  Created: {task.created_date}"
        
        if task.completed:
            result += f" | Completed: {task.completed_date}"
            
        if task.due_date:
            result += f" | Due: {task.due_date}"
            
        if task.description:
            result += f"\n  Description: {task.description}"
            
        return result
    else:
        due_str = f"Due: {task.due_date}" if task.due_date else ""
        return f"{status} {task.title} ({task.priority}) {due_str}"


def list_tasks_command(args):
    """Handle the list tasks command.

    Args:
        args: Command line arguments
    """
    manager = TaskManager(task_file='/tmp/task_manager_tests/test_tasks.json')
    tasks = manager.list_tasks(show_completed=args.all)
    
    if not tasks:
        print("No tasks found.")
        return
    
    print(f"Found {len(tasks)} tasks:")
    for task in tasks:
        print(format_task_output(task, args.verbose))


def add_task_command(args):
    """Handle the add task command.

    Args:
        args: Command line arguments
    """
    manager = TaskManager(task_file='/tmp/task_manager_tests/test_tasks.json')
    try:
        task = manager.add_task(
            title=args.title,
            description=args.description,
            due_date=args.due,
            priority=args.priority
        )
        print(f"Task added with ID: {task.id}")
    except ValueError as e:
        print(f"Error: {e}")


def complete_task_command(args):
    """Handle the complete task command.

    Args:
        args: Command line arguments
    """
    manager = TaskManager(task_file='/tmp/task_manager_tests/test_tasks.json')
    if manager.complete_task(args.id):
        print(f"Task {args.id} marked as completed")
    else:
        print(f"Task with ID {args.id} not found")


def delete_task_command(args):
    """Handle the delete task command.

    Args:
        args: Command line arguments
    """
    manager = TaskManager(task_file='/tmp/task_manager_tests/test_tasks.json')
    if manager.delete_task(args.id):
        print(f"Task {args.id} deleted")
    else:
        print(f"Task with ID {args.id} not found")


def view_task_command(args):
    """Handle the view task command.

    Args:
        args: Command line arguments
    """
    manager = TaskManager(task_file='/tmp/task_manager_tests/test_tasks.json')
    task = manager.get_task_by_id(args.id)
    if task:
        print(format_task_output(task, verbose=True))
    else:
        print(f"Task with ID {args.id} not found")


def stats_command(args):
    """Handle the stats command.

    Args:
        args: Command line arguments
    """
    manager = TaskManager(task_file='/tmp/task_manager_tests/test_tasks.json')
    stats = manager.get_statistics()
    
    print("Task Statistics:")
    print(f"Total tasks: {stats['total']}")
    print(f"Completed: {stats['completed']}")
    print(f"Pending: {stats['pending']}")
    print("Priorities:")
    for priority, count in stats['priorities'].items():
        print(f"  - {priority}: {count}")


def main():
    """Main entry point for the CLI application."""
    parser = argparse.ArgumentParser(description='Task Manager CLI')
    subparsers = parser.add_subparsers(dest='command', help='Command')
    
    # List command
    list_parser = subparsers.add_parser('list', help='List tasks')
    list_parser.add_argument('-a', '--all', action='store_true', help='Show all tasks including completed')
    list_parser.add_argument('-v', '--verbose', action='store_true', help='Show detailed task information')
    
    # Add command
    add_parser = subparsers.add_parser('add', help='Add a new task')
    add_parser.add_argument('title', help='Task title')
    add_parser.add_argument('-d', '--description', default='', help='Task description')
    add_parser.add_argument('--due', help='Due date (YYYY-MM-DD)')
    add_parser.add_argument('-p', '--priority', default='medium', choices=['low', 'medium', 'high'], help='Task priority')
    
    # Complete command
    complete_parser = subparsers.add_parser('complete', help='Mark a task as completed')
    complete_parser.add_argument('id', help='Task ID')
    
    # Delete command
    delete_parser = subparsers.add_parser('delete', help='Delete a task')
    delete_parser.add_argument('id', help='Task ID')
    
    # View command
    view_parser = subparsers.add_parser('view', help='View task details')
    view_parser.add_argument('id', help='Task ID')
    
    # Stats command
    subparsers.add_parser('stats', help='Show task statistics')
    
    args = parser.parse_args()
    
    if args.command == 'list':
        list_tasks_command(args)
    elif args.command == 'add':
        add_task_command(args)
    elif args.command == 'complete':
        complete_task_command(args)
    elif args.command == 'delete':
        delete_task_command(args)
    elif args.command == 'view':
        view_task_command(args)
    elif args.command == 'stats':
        stats_command(args)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
