# 本地论文知识库问答系统（Langchain-Chatchat RAG）

这是一个基于 Langchain-Chatchat 搭建的本地化 RAG 知识库问答项目，面向论文、专业文档、课程资料和企业内部资料等场景。项目支持本地模型部署、文档上传、文本切分、向量化入库、语义检索、引用片段展示和多轮问答。

## 项目亮点

- 本地运行：基于 Ollama 调用本地大语言模型，适合隐私敏感文档。
- RAG 问答：先检索知识库相关片段，再由大模型生成答案，降低幻觉。
- 知识库管理：支持上传文档、重建向量库、查看和维护文档片段。
- 中文界面：对 Langchain-Chatchat WebUI 做了中文化和视觉优化。
- 工程化脚本：提供安装、启动、停止、检查和界面定制恢复脚本。
- GitHub 友好：忽略本地模型、虚拟环境、日志、向量索引和个人论文原文。

## 技术栈

- Python
- Langchain-Chatchat 0.3.1.3
- LangChain
- Ollama
- Qwen2-7B
- bge-m3 Embedding
- Streamlit WebUI
- PowerShell 脚本

## 当前本地配置

| 项目 | 配置 |
| --- | --- |
| 项目目录 | `F:\Langchain-Chatchat-RAG` |
| LLM | `qwen2:7b` |
| Embedding | `bge-m3` |
| 模型目录 | `F:\OllamaModels` |
| API | `http://127.0.0.1:7861` |
| WebUI | `http://127.0.0.1:8501` |

## 目录说明

```text
basic_settings.yaml                 Chatchat 基础服务配置
kb_settings.yaml                    知识库配置
model_settings.yaml                 模型平台、LLM、Embedding 配置
prompt_settings.yaml                提示词配置
tool_settings.yaml                  工具配置
requirements.txt                    最小安装依赖
requirements-lock.txt               当前可运行环境依赖锁定
scripts/                            Windows 辅助脚本
customizations/chatchat_ui/         中文 WebUI 定制文件
data/knowledge_base/**/content/     可提交的知识库示例内容
GITHUB_CHECKLIST.md                 上传 GitHub 前检查清单
.env.example                        环境变量示例
```

## 快速开始

### 1. 安装 Python 依赖

在项目根目录执行：

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\setup.ps1
```

或者手动执行：

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install --upgrade pip setuptools "wheel<0.46"
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

### 2. 准备 Ollama 模型

```powershell
ollama pull qwen2:7b
ollama pull bge-m3
```

建议把模型放到空间较大的磁盘：

```powershell
setx OLLAMA_MODELS "F:\OllamaModels"
```

设置后重新打开命令行或重启 Ollama。

### 3. 应用中文界面定制

如果重新安装依赖后界面恢复默认版，执行：

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\apply-ui-customization.ps1
```

### 4. 重建知识库

```powershell
.\.venv\Scripts\chatchat.exe kb -r -n papers -e bge-m3
.\.venv\Scripts\chatchat.exe kb -r -n samples -e bge-m3
```

### 5. 启动服务

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\start.ps1
```

启动后访问：

- WebUI: `http://127.0.0.1:8501`
- API Docs: `http://127.0.0.1:7861/docs`

### 6. 停止服务

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\stop.ps1
```

## 项目检查

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\check.ps1
```

该脚本会检查虚拟环境、Chatchat、Ollama、模型列表和关键项目文件。

## 知识库说明

- `samples`：示例知识库，包含 Markdown、CSV、XLSX、PDF、TXT 示例文件。
- `papers`：论文/RAG 演示知识库，默认提交 Markdown 演示文件。

个人上传的论文 PDF、Word 文档、向量索引和数据库文件已加入 `.gitignore`，避免误传到公开仓库。
