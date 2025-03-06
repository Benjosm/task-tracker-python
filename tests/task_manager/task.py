#!/usr/bin/env python3
import json
from datetime import datetime

class Task:
    def __init__(self, task_id: int, title: str):
        self.task_id = task_id
        self.title = title
        self.description = None
        self.created_at = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    def __str__(self):
        return f"Task {self.task_id}: {self.title} (Desc: {self.description})"
