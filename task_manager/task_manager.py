class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, title, description):
        self.tasks.append({'title': title, 'description': description})

    def get_tasks(self):
        return self.tasks