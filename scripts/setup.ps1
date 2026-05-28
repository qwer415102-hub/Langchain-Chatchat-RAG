$ErrorActionPreference = "Stop"

$Root = Split-Path -Parent $PSScriptRoot
$Python = Join-Path $Root ".venv\Scripts\python.exe"

if (-not (Test-Path $Python)) {
    python -m venv (Join-Path $Root ".venv")
}

& $Python -m pip install --upgrade pip setuptools "wheel<0.46"
& $Python -m pip install -r (Join-Path $Root "requirements.txt")
