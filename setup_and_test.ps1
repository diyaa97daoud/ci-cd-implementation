# Setup and Test Script for TaskLib
# This script will set up the environment and run basic tests

Write-Host "=" -NoNewline; Write-Host ("=" * 59)
Write-Host "TaskLib - Setup and Test Script"
Write-Host "=" -NoNewline; Write-Host ("=" * 59)

# Change to project directory
$ProjectDir = "d:\CPS2\M1\First sem\TFSD\lecture 8"
Set-Location $ProjectDir

Write-Host "`n📦 Step 1: Setting up virtual environment..."
if (Test-Path "venv") {
    Write-Host "  ℹ️  Virtual environment already exists"
} else {
    python -m venv venv
    Write-Host "  ✓ Created virtual environment"
}

Write-Host "`n🔧 Step 2: Activating virtual environment..."
& ".\venv\Scripts\Activate.ps1"
Write-Host "  ✓ Virtual environment activated"

Write-Host "`n📥 Step 3: Installing dependencies..."
python -m pip install --upgrade pip -q
pip install -e ".[dev]" -q
Write-Host "  ✓ Dependencies installed"

Write-Host "`n🧪 Step 4: Running tests..."
pytest --cov=tasklib --cov-report=term-missing -v

Write-Host "`n🔍 Step 5: Running code analysis..."

Write-Host "`n  📝 Black (formatting check)..."
black --check src/ tests/ 2>&1 | Out-Null
if ($LASTEXITCODE -eq 0) {
    Write-Host "    ✓ Code formatting is correct"
} else {
    Write-Host "    ⚠️  Code needs formatting (run: black src/ tests/)"
}

Write-Host "`n  📝 Flake8 (style check)..."
flake8 src/ tests/ --max-line-length=100 --extend-ignore=E203,W503 --count
if ($LASTEXITCODE -eq 0) {
    Write-Host "    ✓ No style issues found"
}

Write-Host "`n  📝 Pylint (code quality)..."
pylint src/ --max-line-length=100 --disable=C0114,C0115,C0116

Write-Host "`n  📝 MyPy (type checking)..."
mypy src/ --ignore-missing-imports
if ($LASTEXITCODE -eq 0) {
    Write-Host "    ✓ Type checking passed"
}

Write-Host "`n  🔒 Bandit (security scan)..."
bandit -r src/ -ll -q
if ($LASTEXITCODE -eq 0) {
    Write-Host "    ✓ No security issues found"
}

Write-Host "`n📚 Step 6: Building documentation..."
Set-Location docs
& .\make.bat html 2>&1 | Out-Null
Set-Location ..
if (Test-Path "docs\_build\html\index.html") {
    Write-Host "  ✓ Documentation built successfully"
    Write-Host "    📄 Open: docs\_build\html\index.html"
}

Write-Host "`n📦 Step 7: Building package..."
python -m build 2>&1 | Out-Null
if (Test-Path "dist") {
    $WheelFile = Get-ChildItem "dist\*.whl" | Select-Object -First 1
    $TarFile = Get-ChildItem "dist\*.tar.gz" | Select-Object -First 1
    Write-Host "  ✓ Package built successfully"
    Write-Host "    📦 $($WheelFile.Name)"
    Write-Host "    📦 $($TarFile.Name)"
}

Write-Host "`n🎯 Step 8: Running example..."
python example.py

Write-Host "`n" + ("=" -join ("=" * 59))
Write-Host "✅ All checks completed!"
Write-Host ("=" -join ("=" * 59))

Write-Host "`n📋 Next Steps:"
Write-Host "  1. Initialize git repository:"
Write-Host "     git init"
Write-Host "     git add ."
Write-Host "     git commit -m `"feat: initial project setup with full CI/CD pipeline`""
Write-Host ""
Write-Host "  2. Create GitHub repository and push:"
Write-Host "     git remote add origin https://github.com/YOUR_USERNAME/tasklib.git"
Write-Host "     git branch -M main"
Write-Host "     git push -u origin main"
Write-Host ""
Write-Host "  3. Enable GitHub Pages in repository settings"
Write-Host ""
Write-Host "  4. Create a release tag:"
Write-Host "     git tag -a v0.1.0 -m `"Release v0.1.0`""
Write-Host "     git push origin v0.1.0"
Write-Host ""
Write-Host "📖 See SUBMISSION.md for detailed instructions"
