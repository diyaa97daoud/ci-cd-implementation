Development Guide
=================

This guide covers how to set up a development environment and contribute to TaskLib.

Setup Development Environment
-----------------------------

Clone and Install
~~~~~~~~~~~~~~~~~

.. code-block:: bash

    # Clone repository
    git clone https://github.com/YOUR_USERNAME/tasklib.git
    cd tasklib

    # Create virtual environment
    python -m venv venv
    
    # Activate virtual environment
    # On Windows:
    venv\Scripts\activate
    # On Linux/Mac:
    source venv/bin/activate

    # Install with dev dependencies
    pip install -e ".[dev]"

Running Tests
-------------

Run All Tests
~~~~~~~~~~~~~

.. code-block:: bash

    pytest

Run with Coverage
~~~~~~~~~~~~~~~~~

.. code-block:: bash

    pytest --cov=tasklib --cov-report=html
    
The coverage report will be generated in ``htmlcov/index.html``.

Code Quality
------------

Format Code
~~~~~~~~~~~

.. code-block:: bash

    black src/ tests/

Linting
~~~~~~~

.. code-block:: bash

    # Flake8
    flake8 src/ tests/ --max-line-length=100

    # Pylint
    pylint src/ --max-line-length=100

Type Checking
~~~~~~~~~~~~~

.. code-block:: bash

    mypy src/ --ignore-missing-imports

Security Scanning
~~~~~~~~~~~~~~~~~

.. code-block:: bash

    bandit -r src/

Building Documentation
----------------------

.. code-block:: bash

    cd docs
    make html
    
Documentation will be in ``docs/_build/html/index.html``.

Building Package
----------------

.. code-block:: bash

    python -m build

The built packages will be in the ``dist/`` directory.

CI/CD Pipeline
--------------

This project uses GitHub Actions for continuous integration and deployment.

On Every Commit
~~~~~~~~~~~~~~~

* **Matrix Testing**: Tests run on Python 3.9, 3.10, 3.11 across Linux, Windows, and macOS
* **Code Analysis**: Black, Flake8, Pylint, MyPy, Bandit
* **Coverage Reports**: Generated and uploaded as artifacts

On Tags
~~~~~~~

* Tests and analysis run
* Package is built
* Changelog is auto-generated from git history
* GitHub release is created with artifacts

On Master Branch
~~~~~~~~~~~~~~~~

* Documentation is built with Sphinx
* Published to GitHub Pages

Contributing
------------

1. Fork the repository
2. Create a feature branch (``git checkout -b feature/amazing-feature``)
3. Make your changes
4. Run tests and ensure they pass
5. Run code quality tools
6. Commit your changes with clear messages
7. Push to your fork
8. Open a Pull Request

Commit Message Format
~~~~~~~~~~~~~~~~~~~~~

Use conventional commits:

* ``feat: add new feature``
* ``fix: fix bug in task manager``
* ``docs: update API documentation``
* ``test: add tests for priority filtering``
* ``refactor: improve task search logic``
* ``ci: update GitHub Actions workflow``

Release Process
---------------

1. Update version in ``pyproject.toml``
2. Commit the version change
3. Create and push a tag:

.. code-block:: bash

    git tag -a v0.2.0 -m "Release v0.2.0"
    git push origin v0.2.0

4. GitHub Actions will automatically:
   * Run all tests
   * Build the package
   * Generate changelog
   * Create GitHub release
   * Upload artifacts
