"""
TaskLib - A simple task management library.

This module provides a TaskManager class for managing tasks with priorities,
statuses, and due dates.
"""

from tasklib.models import Task, Priority, Status
from tasklib.manager import TaskManager

__version__ = "0.1.0"
__all__ = ["Task", "Priority", "Status", "TaskManager"]
