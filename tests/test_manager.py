"""Tests for task manager."""

import pytest
import tempfile
from pathlib import Path
from datetime import datetime, timedelta
from tasklib.manager import TaskManager
from tasklib.models import Priority, Status


class TestTaskManager:
    """Test cases for TaskManager class."""

    @pytest.fixture
    def temp_storage(self):
        """Create a temporary storage file."""
        with tempfile.NamedTemporaryFile(mode="w", delete=False, suffix=".json") as f:
            temp_path = f.name
        yield temp_path
        Path(temp_path).unlink(missing_ok=True)

    @pytest.fixture
    def manager(self, temp_storage):
        """Create a TaskManager instance with temporary storage."""
        return TaskManager(storage_path=temp_storage)

    def test_manager_initialization(self, manager):
        """Test TaskManager initialization."""
        assert isinstance(manager, TaskManager)
        assert manager.tasks == []

    def test_add_task(self, manager):
        """Test adding a task."""
        task_id = manager.add_task(
            title="Test Task", description="Test Description", priority=Priority.HIGH
        )

        assert task_id is not None
        assert len(manager.tasks) == 1

        task = manager.get_task(task_id)
        assert task is not None
        assert task.title == "Test Task"
        assert task.description == "Test Description"
        assert task.priority == Priority.HIGH

    def test_add_task_with_due_date(self, manager):
        """Test adding a task with due date."""
        task_id = manager.add_task(title="Task with deadline", due_date="2026-12-31")

        task = manager.get_task(task_id)
        assert task.due_date is not None
        assert task.due_date.year == 2026
        assert task.due_date.month == 12
        assert task.due_date.day == 31

    def test_get_task_not_found(self, manager):
        """Test getting a non-existent task."""
        task = manager.get_task("nonexistent-id")
        assert task is None

    def test_get_all_tasks(self, manager):
        """Test getting all tasks."""
        manager.add_task(title="Task 1")
        manager.add_task(title="Task 2")
        manager.add_task(title="Task 3")

        tasks = manager.get_tasks()
        assert len(tasks) == 3
        assert tasks[0].title == "Task 1"
        assert tasks[1].title == "Task 2"
        assert tasks[2].title == "Task 3"

    def test_update_task(self, manager):
        """Test updating a task."""
        task_id = manager.add_task(title="Original Title")

        success = manager.update_task(
            task_id,
            title="Updated Title",
            description="New Description",
            priority=Priority.CRITICAL,
            status=Status.IN_PROGRESS,
        )

        assert success

        task = manager.get_task(task_id)
        assert task.title == "Updated Title"
        assert task.description == "New Description"
        assert task.priority == Priority.CRITICAL
        assert task.status == Status.IN_PROGRESS

    def test_update_nonexistent_task(self, manager):
        """Test updating a non-existent task."""
        success = manager.update_task("nonexistent-id", title="New Title")
        assert not success

    def test_delete_task(self, manager):
        """Test deleting a task."""
        task_id = manager.add_task(title="Task to delete")

        assert len(manager.tasks) == 1

        success = manager.delete_task(task_id)
        assert success
        assert len(manager.tasks) == 0

    def test_delete_nonexistent_task(self, manager):
        """Test deleting a non-existent task."""
        success = manager.delete_task("nonexistent-id")
        assert not success

    def test_filter_by_status(self, manager):
        """Test filtering tasks by status."""
        manager.add_task(title="Todo Task 1")
        manager.add_task(title="Todo Task 2")

        task_id = manager.add_task(title="In Progress Task")
        manager.update_task(task_id, status=Status.IN_PROGRESS)

        todo_tasks = manager.filter_tasks(status=Status.TODO)
        in_progress_tasks = manager.filter_tasks(status=Status.IN_PROGRESS)

        assert len(todo_tasks) == 2
        assert len(in_progress_tasks) == 1
        assert in_progress_tasks[0].title == "In Progress Task"

    def test_filter_by_priority(self, manager):
        """Test filtering tasks by priority."""
        manager.add_task(title="Low Priority", priority=Priority.LOW)
        manager.add_task(title="High Priority 1", priority=Priority.HIGH)
        manager.add_task(title="High Priority 2", priority=Priority.HIGH)

        high_priority = manager.filter_tasks(priority=Priority.HIGH)

        assert len(high_priority) == 2
        assert all(t.priority == Priority.HIGH for t in high_priority)

    def test_filter_overdue(self, manager):
        """Test filtering overdue tasks."""
        past_date = (datetime.now() - timedelta(days=1)).isoformat()
        future_date = (datetime.now() + timedelta(days=1)).isoformat()

        manager.add_task(title="Overdue Task", due_date=past_date)
        manager.add_task(title="Future Task", due_date=future_date)

        overdue_tasks = manager.filter_tasks(overdue_only=True)

        assert len(overdue_tasks) == 1
        assert overdue_tasks[0].title == "Overdue Task"

    def test_search_tasks(self, manager):
        """Test searching tasks."""
        manager.add_task(title="Python Project", description="Learn Python")
        manager.add_task(title="Java Project", description="Learn Java")
        manager.add_task(title="Web Development", description="Learn Python Django")

        python_tasks = manager.search_tasks("Python")

        assert len(python_tasks) == 2
        assert any("Python" in t.title for t in python_tasks)

    def test_persistence(self, temp_storage):
        """Test that tasks are persisted to storage."""
        # Create manager and add tasks
        manager1 = TaskManager(storage_path=temp_storage)
        task_id = manager1.add_task(title="Persistent Task", priority=Priority.HIGH)

        # Create new manager with same storage
        manager2 = TaskManager(storage_path=temp_storage)

        # Verify task was loaded
        assert len(manager2.tasks) == 1
        task = manager2.get_task(task_id)
        assert task is not None
        assert task.title == "Persistent Task"
        assert task.priority == Priority.HIGH
