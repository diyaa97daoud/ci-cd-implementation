"""
Example usage of the TaskLib library.

This script demonstrates the basic functionality of the library.
"""

from tasklib import TaskManager, Priority, Status
from datetime import datetime, timedelta


def main():
    """Main example function."""
    print("=" * 60)
    print("TaskLib - Example Usage")
    print("=" * 60)
    
    # Create a task manager
    manager = TaskManager(storage_path="example_tasks.json")
    print("\n✓ Created TaskManager")
    
    # Add some tasks
    print("\n📝 Adding tasks...")
    
    task1 = manager.add_task(
        title="Complete CI/CD implementation",
        description="Set up GitHub Actions for automated testing and deployment",
        priority=Priority.HIGH,
        due_date=(datetime.now() + timedelta(days=7)).isoformat()
    )
    print(f"  ✓ Added task: Complete CI/CD implementation (ID: {task1[:8]}...)")
    
    task2 = manager.add_task(
        title="Write documentation",
        description="Create comprehensive Sphinx documentation",
        priority=Priority.MEDIUM,
        due_date=(datetime.now() + timedelta(days=5)).isoformat()
    )
    print(f"  ✓ Added task: Write documentation (ID: {task2[:8]}...)")
    
    task3 = manager.add_task(
        title="Code review",
        description="Review pull requests from team members",
        priority=Priority.LOW,
        due_date=(datetime.now() + timedelta(days=2)).isoformat()
    )
    print(f"  ✓ Added task: Code review (ID: {task3[:8]}...)")
    
    # Display all tasks
    print("\n📋 All tasks:")
    for task in manager.get_tasks():
        print(f"  • {task.title} [{task.priority.value}] - {task.status.value}")
    
    # Update a task
    print("\n🔄 Updating task status...")
    manager.update_task(task1, status=Status.IN_PROGRESS)
    task = manager.get_task(task1)
    print(f"  ✓ Task '{task.title}' is now {task.status.value}")
    
    # Filter tasks
    print("\n🔍 Filtering high priority tasks:")
    high_priority = manager.filter_tasks(priority=Priority.HIGH)
    for task in high_priority:
        print(f"  • {task.title}")
    
    # Search tasks
    print("\n🔎 Searching for 'documentation':")
    results = manager.search_tasks("documentation")
    for task in results:
        print(f"  • {task.title}: {task.description}")
    
    # Complete a task
    print("\n✅ Completing a task...")
    manager.update_task(task3, status=Status.COMPLETED)
    task = manager.get_task(task3)
    print(f"  ✓ Task '{task.title}' marked as completed")
    
    # Display summary
    print("\n📊 Summary:")
    all_tasks = manager.get_tasks()
    print(f"  Total tasks: {len(all_tasks)}")
    print(f"  TODO: {len(manager.filter_tasks(status=Status.TODO))}")
    print(f"  In Progress: {len(manager.filter_tasks(status=Status.IN_PROGRESS))}")
    print(f"  Completed: {len(manager.filter_tasks(status=Status.COMPLETED))}")
    
    print("\n" + "=" * 60)
    print("Example completed! Tasks saved to example_tasks.json")
    print("=" * 60)


if __name__ == "__main__":
    main()
