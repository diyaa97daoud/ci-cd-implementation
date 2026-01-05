"""Data models for task management."""

from dataclasses import dataclass, field, asdict
from datetime import datetime
from enum import Enum
from typing import Optional
import uuid


class Priority(Enum):
    """Task priority levels."""
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"


class Status(Enum):
    """Task status values."""
    TODO = "todo"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    CANCELLED = "cancelled"


@dataclass
class Task:
    """
    Represents a task with title, description, priority, status, and dates.
    
    Attributes:
        id: Unique identifier for the task
        title: Task title
        description: Detailed task description
        priority: Task priority level
        status: Current task status
        due_date: Optional due date for the task
        created_at: Timestamp when task was created
        updated_at: Timestamp when task was last updated
    """
    
    title: str
    description: str = ""
    priority: Priority = Priority.MEDIUM
    status: Status = Status.TODO
    due_date: Optional[datetime] = None
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
    created_at: datetime = field(default_factory=datetime.now)
    updated_at: datetime = field(default_factory=datetime.now)
    
    def to_dict(self) -> dict:
        """Convert task to dictionary for JSON serialization."""
        data = asdict(self)
        data['priority'] = self.priority.value
        data['status'] = self.status.value
        data['created_at'] = self.created_at.isoformat()
        data['updated_at'] = self.updated_at.isoformat()
        if self.due_date:
            data['due_date'] = self.due_date.isoformat()
        return data
    
    @classmethod
    def from_dict(cls, data: dict) -> 'Task':
        """Create task from dictionary."""
        data = data.copy()
        data['priority'] = Priority(data['priority'])
        data['status'] = Status(data['status'])
        data['created_at'] = datetime.fromisoformat(data['created_at'])
        data['updated_at'] = datetime.fromisoformat(data['updated_at'])
        if data.get('due_date'):
            data['due_date'] = datetime.fromisoformat(data['due_date'])
        return cls(**data)
    
    def is_overdue(self) -> bool:
        """Check if task is overdue."""
        if not self.due_date:
            return False
        return self.status != Status.COMPLETED and datetime.now() > self.due_date
