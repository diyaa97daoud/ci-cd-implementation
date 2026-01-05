TaskLib Documentation
====================

Welcome to TaskLib's documentation!

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   quickstart
   api
   development
   changelog

TaskLib is a simple yet powerful task management library demonstrating modern CI/CD practices.

Features
--------

* Create, update, and manage tasks with priorities and due dates
* Filter tasks by status, priority, and date
* Persistent JSON storage
* Type-safe with full type hints
* Comprehensive test coverage
* Full CI/CD automation

Quick Example
-------------

.. code-block:: python

    from tasklib import TaskManager, Priority, Status

    # Create a task manager
    manager = TaskManager()

    # Add a task
    task_id = manager.add_task(
        title="Complete project",
        description="Finish CI/CD implementation",
        priority=Priority.HIGH,
        due_date="2026-01-15"
    )

    # Get all tasks
    tasks = manager.get_tasks()

    # Update task status
    manager.update_task(task_id, status=Status.IN_PROGRESS)

Installation
------------

Install TaskLib using pip:

.. code-block:: bash

    pip install tasklib

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
