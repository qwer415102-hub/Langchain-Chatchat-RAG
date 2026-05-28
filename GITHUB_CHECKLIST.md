# GitHub 上传前检查清单

## 不要提交

- `.venv/` 虚拟环境
- `F:\OllamaModels` 或任何本地模型文件
- `data/logs/`、`data/temp/`、`data/media/`
- `data/knowledge_base/info.db`
- `data/knowledge_base/**/vector_store/`
- 个人论文原文，例如 `data/knowledge_base/papers/content/*.pdf`
- `.env`、密钥、Token、私有 API Key

## 建议提交

- `README.md`
- `.gitignore`
- `.env.example`
- `requirements.txt`
- `requirements-lock.txt`
- `scripts/`
- `customizations/`
- `*.yaml`
- `data/knowledge_base/**/content/*.md`

## 上传后推荐在 README 展示

- 项目目标：本地论文/专业文档 RAG 问答系统
- 技术栈：Langchain-Chatchat、LangChain、Ollama、Qwen2、bge-m3、Streamlit
- 核心能力：文档上传、文本切分、向量入库、语义检索、引用片段、多轮问答、中文 WebUI
- 隐私优势：模型和知识库均可本地运行
