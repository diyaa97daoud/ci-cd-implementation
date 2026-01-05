Quick Start Guide
=================

Installation
------------

Install TaskLib using pip:

.. code-block:: bash

    pip install tasklib

Basic Usage
-----------

Creating a Task Manager
~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    from tasklib import TaskManager

    # Create a task manager with default storage
    manager = TaskManager()

    # Or specify a custom storage path
    manager = TaskManager(storage_path="my_tasks.json")

Adding Tasks
~~~~~~~~~~~~

.. code-block:: python

    from tasklib import TaskManager, Priority

    manager = TaskManager()

    # Add a simple task
    task_id = manager.add_task(title="Buy groceries")

    # Add a task with details
    task_id = manager.add_task(
        title="Complete project",
        description="Finish the CI/CD implementation",
        priority=Priority.HIGH,
        due_date="2026-01-15"
    )

Managing Tasks
~~~~~~~~~~~~~~

.. code-block:: python

    from tasklib import Status

    # Get a specific task
    task = manager.get_task(task_id)

    # Get all tasks
    all_tasks = manager.get_tasks()

    # Update a task
    manager.update_task(
        task_id,
        title="Updated title",
        status=Status.IN_PROGRESS
    )

    # Delete a task
    manager.delete_task(task_id)

Filtering Tasks
~~~~~~~~~~~~~~~

.. code-block:: python

    from tasklib import Priority, Status

    # Get all high priority tasks
    high_priority = manager.filter_tasks(priority=Priority.HIGH)

    # Get all completed tasks
    completed = manager.filter_tasks(status=Status.COMPLETED)

    # Get overdue tasks
    overdue = manager.filter_tasks(overdue_only=True)

Searching Tasks
~~~~~~~~~~~~~~~

.. code-block:: python

    # Search tasks by title or description
    results = manager.search_tasks("project")

Task Properties
---------------

Priority Levels
~~~~~~~~~~~~~~~

* ``Priority.LOW``
* ``Priority.MEDIUM``
* ``Priority.HIGH``
* ``Priority.CRITICAL``

Task Statuses
~~~~~~~~~~~~~

* ``Status.TODO``
* ``Status.IN_PROGRESS``
* ``Status.COMPLETED``
* ``Status.CANCELLED``

Next Steps
----------

* Check out the :doc:`api` documentation for detailed API reference
* Learn about :doc:`development` if you want to contribute
