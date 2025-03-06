# task_manager/task_cli.py
import sys
import json
import argparse
from task_manager.task_manager import TaskManager

def main():
    cli = argparse.ArgumentParser(description='Task CLI')
    cli.add_argument('--tasks-file', type=str, default='/tmp/tasks.json', help='Path to the tasks JSON file')
    subparsers = cli.add_subparsers(dest='command')

    # Add task command
    add_parser = subparsers.add_parser('add', help='Add a new task')
    add_parser.add_argument('title', help='Task title')
    add_parser.add_argument('-d', '--description', help='Task description')

    # List tasks command
    list_parser = subparsers.add_parser('list', help='List tasks')

    # Complete task command
    complete_parser = subparsers.add_parser('complete', help='Complete a task')
    complete_parser.add_argument('task_id', type=int, help='Task ID to complete')

    args = cli.parse_args()

    task_manager = TaskManager(args.tasks_file)

    if args.command == 'add':
        task_manager.add_task(args.title, args.description)
        print('Task added successfully.')
    elif args.command == 'list':
        tasks = task_manager.list_tasks()
        if tasks:
            for task in tasks:
                print(task)
        else:
            print('No tasks found.')
    elif args.command == 'complete':
        task_id = args.task_id
        try:
            task_manager.complete_task(task_id)
            print(f'Task {task_id} completed successfully.')
        except ValueError as e:
            print(f'Error completing task {task_id}: {e}')
    elif args.command is None:
        cli.print_help()
    else:
        print('Unknown command.')

if __name__ == '__main__':
    main()"