"""Tests for task models."""

from datetime import datetime, timedelta
from tasklib.models import Task, Priority, Status


class TestTask:
    """Test cases for Task class."""

    def test_task_creation(self):
        """Test basic task creation."""
        task = Task(title="Test Task", description="Test description")

        assert task.title == "Test Task"
        assert task.description == "Test description"
        assert task.priority == Priority.MEDIUM
        assert task.status == Status.TODO
        assert task.id is not None
        assert isinstance(task.created_at, datetime)
        assert isinstance(task.updated_at, datetime)

    def test_task_with_priority(self):
        """Test task creation with specific priority."""
        task = Task(title="High Priority Task", priority=Priority.HIGH)

        assert task.priority == Priority.HIGH

    def test_task_with_due_date(self):
        """Test task with due date."""
        due_date = datetime.now() + timedelta(days=7)
        task = Task(title="Task with deadline", due_date=due_date)

        assert task.due_date == due_date

    def test_task_to_dict(self):
        """Test task serialization to dictionary."""
        task = Task(
            title="Test Task",
            description="Description",
            priority=Priority.HIGH,
            status=Status.IN_PROGRESS,
        )

        data = task.to_dict()

        assert data["title"] == "Test Task"
        assert data["description"] == "Description"
        assert data["priority"] == "high"
        assert data["status"] == "in_progress"
        assert "id" in data
        assert "created_at" in data
        assert "updated_at" in data

    def test_task_from_dict(self):
        """Test task deserialization from dictionary."""
        original = Task(
            title="Original Task",
            description="Original Description",
            priority=Priority.CRITICAL,
            status=Status.COMPLETED,
        )

        data = original.to_dict()
        restored = Task.from_dict(data)

        assert restored.title == original.title
        assert restored.description == original.description
        assert restored.priority == original.priority
        assert restored.status == original.status
        assert restored.id == original.id

    def test_task_is_overdue_false(self):
        """Test is_overdue returns False for future tasks."""
        future_date = datetime.now() + timedelta(days=1)
        task = Task(title="Future Task", due_date=future_date)

        assert not task.is_overdue()

    def test_task_is_overdue_true(self):
        """Test is_overdue returns True for past tasks."""
        past_date = datetime.now() - timedelta(days=1)
        task = Task(title="Overdue Task", due_date=past_date, status=Status.TODO)

        assert task.is_overdue()

    def test_task_is_overdue_completed(self):
        """Test is_overdue returns False for completed tasks."""
        past_date = datetime.now() - timedelta(days=1)
        task = Task(title="Completed Task", due_date=past_date, status=Status.COMPLETED)

        assert not task.is_overdue()

    def test_task_is_overdue_no_date(self):
        """Test is_overdue returns False when no due date."""
        task = Task(title="No Deadline Task")

        assert not task.is_overdue()


class TestPriority:
    """Test cases for Priority enum."""

    def test_priority_values(self):
        """Test all priority values exist."""
        assert Priority.LOW.value == "low"
        assert Priority.MEDIUM.value == "medium"
        assert Priority.HIGH.value == "high"
        assert Priority.CRITICAL.value == "critical"


class TestStatus:
    """Test cases for Status enum."""

    def test_status_values(self):
        """Test all status values exist."""
        assert Status.TODO.value == "todo"
        assert Status.IN_PROGRESS.value == "in_progress"
        assert Status.COMPLETED.value == "completed"
        assert Status.CANCELLED.value == "cancelled"
