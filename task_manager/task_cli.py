# task_manager/task_cli.py
import sys
import json
import argparse
from task_manager.task_manager import TaskManager

def main():
    cli = argparse.ArgumentParser(description='Task CLI')
    cli.add_argument('--tasks-file', type=str, default='/tmp/test_tasks.json', help='Path to the tasks JSON file')
    subparsers = cli.add_subparsers(dest='command')

    # Add task command
    add_parser = subparsers.add_parser('add', help='Add a new task')
    add_parser.add_argument('title', help='Task title')
    add_parser.add_argument('-d', '--description', help='Task description')

    # List tasks command
    list_parser = subparsers.add_parser('list', help='List tasks')

    # Complete task command
    complete_parser = subparsers.add_parser('complete', help='Complete a task')
    complete_parser.add_argument('task_id', type=str, help='Task ID to complete')

    # Delete task command
    delete_parser = subparsers.add_parser('delete', help='Delete a task')
    delete_parser.add_argument('task_id', type=str, help='Task ID to delete')

    args = cli.parse_args()

    task_manager = TaskManager(args.tasks_file)

    if args.command == 'add':
        if not args.description:
            sys.stderr.write("Error: Description is required when adding a task using 'add' command.\n")
            sys.exit(2)
        task = task_manager.add_task(args.title, args.description)
        print('Task added successfully.')
        print(f'Task ID: {task.id}') # Print Task ID, using task.id
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
            completed = task_manager.complete_task(task_id)
            if completed:
                print(f'Task {task_id} completed successfully.')
            else:
                sys.stderr.write(f'Error completing task {task_id}: Task not found.\n') # stderr
                sys.exit(1) # Exit with error code if task not found
        except ValueError as e:
            sys.stderr.write(f'Error completing task {task_id}: {e}\n') # stderr
            sys.exit(1) # Exit with error code for complete
    elif args.command == 'delete':
        task_id = args.task_id
        try:
            deleted = task_manager.delete_task(task_id)
            if deleted:
                print(f'Task {task_id} deleted successfully.')
            else:
                sys.stderr.write(f'Error deleting task {task_id}: Task not found.\n') # stderr
                sys.exit(1)
        except ValueError as e:
            sys.stderr.write(f'Error deleting task {task_id}: {e}\n') # stderr
            sys.exit(1)
    elif args.command is None:
        cli.print_help()
    else:
        print('Unknown command.')

if __name__ == '__main__':
    main()