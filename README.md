# TaskLib - Task Management Library

[![CI](https://github.com/diyaa97daoud/ci-cd-implementation/workflows/CI/badge.svg)](https://github.com/diyaa97daoud/ci-cd-implementation/actions)
[![Python Versions](https://img.shields.io/badge/python-3.9%20|%203.10%20|%203.11-blue)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A simple yet powerful task management library demonstrating modern CI/CD practices for TFSD Lecture 8.

---

## Features

- ✅ Create, update, and manage tasks with priorities and due dates
- ✅ Filter tasks by status, priority, and date
- ✅ Persistent JSON storage
- ✅ Type-safe with full type hints
- ✅ Comprehensive test coverage
- ✅ Full CI/CD automation

## Installation

```bash
pip install tasklib
```

## Quick Start

```python
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

# Filter tasks
high_priority = manager.filter_tasks(priority=Priority.HIGH)
```

## 📊 CI/CD Pipeline Details

### 1️⃣ Matrix Testing (Every Commit) - 1 Point

**File:** `.github/workflows/ci.yml` (lines 5-34)

- Tests on **Python 3.9, 3.10, 3.11**
- Tests on **Ubuntu, Windows, macOS**
- **9 jobs** run automatically (3 Python × 3 OS)
- **30+ test cases** with 80% coverage requirement

### 2️⃣ Code Analysis (Every Commit) - 1 Point

**File:** `.github/workflows/ci.yml` (lines 47-82)

| Tool       | Purpose                                      |
| ---------- | -------------------------------------------- |
| **Black**  | Code formatting                              |
| **Flake8** | PEP 8 style checking                         |
| **Pylint** | Code quality & code smells                   |
| **MyPy**   | Static type checking                         |
| **Bandit** | Security vulnerabilities & secrets detection |

### 3️⃣ Automated Releases (On Tags) - 2 Points

**File:** `.github/workflows/release.yml`

- **Trigger:** When you create a tag (e.g., `v0.1.0`)
- **Auto-generates changelog** from git commit history
- **Groups commits** by type (feat, fix, docs, other)
- **Creates GitHub release** with:
  - Auto-generated changelog as description
  - Build artifacts (wheel, tar.gz)
  - Coverage reports
  - Security scan reports

### 4️⃣ Documentation Publishing (Master Branch) - 1 Point

**File:** `.github/workflows/docs.yml`

- **Trigger:** Push to main/master branch only
- **Builds:** Sphinx documentation from RST files
- **Deploys:** Automatically to GitHub Pages
- **URL:** `https://diyaa97daoud.github.io/ci-cd-implementation/`

---

## 🧪 Local Testing

### Manual Testing

```bash
# Install dependencies
python -m venv venv
.\venv\Scripts\activate  # Windows
pip install -e ".[dev]"

# Run tests
pytest --cov=tasklib --cov-report=html

# Run analysis
black --check src/ tests/
flake8 src/ tests/ --max-line-length=100
pylint src/ --max-line-length=100
mypy src/ --ignore-missing-imports
bandit -r src/
```

---

## 🔗 After Deployment URLs

deployed project URLs:

- **Repository:** `https://github.com/diyaa97daoud/ci-cd-implementation`
- **Actions:** `https://github.com/diyaa97daoud/ci-cd-implementation/actions`
- **Releases:** `https://github.com/diyaa97daoud/ci-cd-implementation/releases`
- **Documentation:** `https://diyaa97daoud.github.io/ci-cd-implementation/`

---

## 📊 What Happens After Push

### Every Commit:

1. ✅ Tests run on 9 configurations (3 Python × 3 OS)
2. ✅ 5 analysis tools validate code quality
3. ✅ Coverage reports generated (80% minimum enforced)
4. ✅ Build artifacts created

### Every Tag (e.g., v0.1.0):

1. ✅ Full test suite runs
2. ✅ Changelog auto-generated from git history
3. ✅ GitHub release created automatically
4. ✅ Build artifacts attached to release
5. ✅ Coverage and security reports included

### Master Branch Push:

1. ✅ Sphinx documentation built
2. ✅ Auto-deployed to GitHub Pages
3. ✅ Available at custom URL

---

## 📖 Documentation

Full API documentation is auto-generated and available at GitHub Pages after deployment.

Includes:

- API Reference (auto-generated from docstrings)
- Quick Start Guide
- Development Guide
- Changelog

---

## 📜 License

MIT License
