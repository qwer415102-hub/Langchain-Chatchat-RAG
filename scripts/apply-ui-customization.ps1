param(
    [string]$ProjectRoot = (Resolve-Path (Join-Path $PSScriptRoot "..")).Path
)

$ErrorActionPreference = "Stop"

$SourceRoot = Join-Path $ProjectRoot "customizations\chatchat_ui"
$PackageRoot = Join-Path $ProjectRoot ".venv\Lib\site-packages\chatchat"

if (-not (Test-Path $SourceRoot)) {
    throw "未找到界面定制文件：$SourceRoot"
}

if (-not (Test-Path $PackageRoot)) {
    throw "未找到 Chatchat 安装目录：$PackageRoot。请先完成虚拟环境安装。"
}

Copy-Item -LiteralPath (Join-Path $SourceRoot "webui.py") `
    -Destination (Join-Path $PackageRoot "webui.py") -Force
Copy-Item -LiteralPath (Join-Path $SourceRoot "webui_pages\custom_ui.py") `
    -Destination (Join-Path $PackageRoot "webui_pages\custom_ui.py") -Force
Copy-Item -LiteralPath (Join-Path $SourceRoot "webui_pages\kb_chat.py") `
    -Destination (Join-Path $PackageRoot "webui_pages\kb_chat.py") -Force
Copy-Item -LiteralPath (Join-Path $SourceRoot "webui_pages\dialogue\dialogue.py") `
    -Destination (Join-Path $PackageRoot "webui_pages\dialogue\dialogue.py") -Force
Copy-Item -LiteralPath (Join-Path $SourceRoot "webui_pages\knowledge_base\knowledge_base.py") `
    -Destination (Join-Path $PackageRoot "webui_pages\knowledge_base\knowledge_base.py") -Force

Write-Host "界面定制已应用。请重启 Chatchat 后查看效果。"
