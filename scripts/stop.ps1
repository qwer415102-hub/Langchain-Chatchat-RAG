$ErrorActionPreference = "Stop"

$Ports = @(7861, 8501)
$ProcessIds = Get-NetTCPConnection -LocalPort $Ports -ErrorAction SilentlyContinue |
    Select-Object -ExpandProperty OwningProcess -Unique |
    Where-Object { $_ -and $_ -ne 0 }

foreach ($ProcessId in $ProcessIds) {
    Stop-Process -Id $ProcessId -Force
}

if ($ProcessIds.Count -eq 0) {
    Write-Host "No Chatchat API/WebUI processes were found on ports 7861 or 8501."
} else {
    Write-Host "Stopped Chatchat processes: $($ProcessIds -join ', ')"
}
