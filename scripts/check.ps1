$ErrorActionPreference = "Stop"

$Root = Split-Path -Parent $PSScriptRoot
$Python = Join-Path $Root ".venv\Scripts\python.exe"
$Chatchat = Join-Path $Root ".venv\Scripts\chatchat.exe"

Write-Host "== Langchain-Chatchat RAG 项目检查 =="
Write-Host "项目目录: $Root"

if (Test-Path $Python) {
    & $Python --version
} else {
    Write-Warning "未找到 Python 虚拟环境，请先运行 .\scripts\setup.ps1"
}

if (Test-Path $Chatchat) {
    Write-Host "Chatchat: $Chatchat"
} else {
    Write-Warning "未找到 chatchat.exe，请先安装依赖。"
}

if (Get-Command ollama -ErrorAction SilentlyContinue) {
    ollama --version
    ollama list
} else {
    Write-Warning "未找到 ollama 命令。请确认 Ollama 已安装并加入 PATH。"
}

$RequiredFiles = @(
    "README.md",
    ".gitignore",
    ".env.example",
    "requirements.txt",
    "model_settings.yaml",
    "kb_settings.yaml",
    "scripts\start.ps1",
    "scripts\stop.ps1",
    "scripts\apply-ui-customization.ps1"
)

foreach ($File in $RequiredFiles) {
    $Path = Join-Path $Root $File
    if (Test-Path $Path) {
        Write-Host "OK  $File"
    } else {
        Write-Warning "缺少 $File"
    }
}

Write-Host "检查完成。"
