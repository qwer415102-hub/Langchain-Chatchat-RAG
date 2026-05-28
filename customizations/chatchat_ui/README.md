# Chatchat 中文界面定制

这里保存了本项目对 Langchain-Chatchat WebUI 的本地定制版本。

因为 `.venv` 不适合提交到 GitHub，真正运行时的页面文件会安装在：

```text
.venv\Lib\site-packages\chatchat
```

如果重新安装依赖或换电脑后界面恢复成默认版，在项目根目录运行：

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\apply-ui-customization.ps1
```

然后重启 Chatchat 即可。
