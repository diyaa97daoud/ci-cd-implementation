"""Task manager implementation."""

import json
from pathlib import Path
from typing import List, Optional
from datetime import datetime
from dateutil import parser as date_parser

from tasklib.models import Task, Priority, Status


class TaskManager:
    """
    Manages a collection of tasks with persistent storage.

    Provides methods to create, read, update, and delete tasks,
    as well as filter and search functionality.
    """

    def __init__(self, storage_path: str = "tasks.json"):
        """
        Initialize the task manager.

        Args:
            storage_path: Path to JSON file for persistent storage
        """
        self.storage_path = Path(storage_path)
        self.tasks: List[Task] = []
        self.load()

    def load(self) -> None:
        """Load tasks from storage file."""
        if self.storage_path.exists():
            try:
                with open(self.storage_path, "r", encoding="utf-8") as f:
                    data = json.load(f)
                    self.tasks = [Task.from_dict(task_data) for task_data in data]
            except (json.JSONDecodeError, KeyError, ValueError):
                self.tasks = []
        else:
            self.tasks = []

    def save(self) -> None:
        """Save tasks to storage file."""
        with open(self.storage_path, "w", encoding="utf-8") as f:
            data = [task.to_dict() for task in self.tasks]
            json.dump(data, f, indent=2)

    def add_task(
        self,
        title: str,
        description: str = "",
        priority: Priority = Priority.MEDIUM,
        due_date: Optional[str] = None,
    ) -> str:
        """
        Add a new task.

        Args:
            title: Task title
            description: Task description
            priority: Task priority
            due_date: Due date as ISO string or parseable date

        Returns:
            The ID of the created task
        """
        due_date_obj = None
        if due_date:
            due_date_obj = date_parser.parse(due_date)

        task = Task(title=title, description=description, priority=priority, due_date=due_date_obj)
        self.tasks.append(task)
        self.save()
        return task.id

    def get_task(self, task_id: str) -> Optional[Task]:
        """Get a task by ID."""
        for task in self.tasks:
            if task.id == task_id:
                return task
        return None

    def get_tasks(self) -> List[Task]:
        """Get all tasks."""
        return self.tasks.copy()

    def update_task(
        self,
        task_id: str,
        title: Optional[str] = None,
        description: Optional[str] = None,
        priority: Optional[Priority] = None,
        status: Optional[Status] = None,
        due_date: Optional[str] = None,
    ) -> bool:
        """
        Update an existing task.

        Args:
            task_id: ID of task to update
            title: New title (optional)
            description: New description (optional)
            priority: New priority (optional)
            status: New status (optional)
            due_date: New due date (optional)

        Returns:
            True if task was updated, False if not found
        """
        task = self.get_task(task_id)
        if not task:
            return False

        if title is not None:
            task.title = title
        if description is not None:
            task.description = description
        if priority is not None:
            task.priority = priority
        if status is not None:
            task.status = status
        if due_date is not None:
            task.due_date = date_parser.parse(due_date)

        task.updated_at = datetime.now()
        self.save()
        return True

    def delete_task(self, task_id: str) -> bool:
        """
        Delete a task.

        Args:
            task_id: ID of task to delete

        Returns:
            True if task was deleted, False if not found
        """
        task = self.get_task(task_id)
        if not task:
            return False

        self.tasks.remove(task)
        self.save()
        return True

    def filter_tasks(
        self,
        status: Optional[Status] = None,
        priority: Optional[Priority] = None,
        overdue_only: bool = False,
    ) -> List[Task]:
        """
        Filter tasks by criteria.

        Args:
            status: Filter by status
            priority: Filter by priority
            overdue_only: Only return overdue tasks

        Returns:
            List of matching tasks
        """
        filtered = self.tasks.copy()

        if status is not None:
            filtered = [t for t in filtered if t.status == status]

        if priority is not None:
            filtered = [t for t in filtered if t.priority == priority]

        if overdue_only:
            filtered = [t for t in filtered if t.is_overdue()]

        return filtered

    def search_tasks(self, query: str) -> List[Task]:
        """
        Search tasks by title or description.

        Args:
            query: Search query string

        Returns:
            List of matching tasks
        """
        query_lower = query.lower()
        return [
            task
            for task in self.tasks
            if query_lower in task.title.lower() or query_lower in task.description.lower()
        ]
