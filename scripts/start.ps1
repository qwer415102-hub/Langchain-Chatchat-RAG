$ErrorActionPreference = "Stop"

$Root = Split-Path -Parent $PSScriptRoot
$Chatchat = Join-Path $Root ".venv\Scripts\chatchat.exe"

if (-not (Test-Path $Chatchat)) {
    throw "Chatchat is not installed. Run .\scripts\setup.ps1 first."
}

& $Chatchat start -a
