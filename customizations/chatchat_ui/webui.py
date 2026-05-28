import sys

import streamlit as st
import streamlit_antd_components as sac

from chatchat import __version__
from chatchat.server.utils import api_address
from chatchat.webui_pages.custom_ui import APP_TITLE, inject_custom_style, page_header
from chatchat.webui_pages.dialogue.dialogue import dialogue_page
from chatchat.webui_pages.kb_chat import kb_chat
from chatchat.webui_pages.knowledge_base.knowledge_base import knowledge_base_page
from chatchat.webui_pages.utils import *

api = ApiRequest(base_url=api_address())


if __name__ == "__main__":
    is_lite = "lite" in sys.argv  # TODO: remove lite mode

    st.set_page_config(
        APP_TITLE,
        get_img_base64("chatchat_icon_blue_square_v2.png"),
        initial_sidebar_state="expanded",
        menu_items={
            "Get Help": "https://github.com/chatchat-space/Langchain-Chatchat",
            "Report a bug": "https://github.com/chatchat-space/Langchain-Chatchat/issues",
            "About": f"欢迎使用 {APP_TITLE}，当前版本：{__version__}",
        },
        layout="wide",
    )
    inject_custom_style()

    with st.sidebar:
        st.image(
            get_img_base64("logo-long-chatchat-trans-v2.png"), use_column_width=True
        )
        st.markdown(
            f"""
            <div class="lc-brand">
                <div class="lc-brand-title">本地知识库问答</div>
                <div class="lc-brand-subtitle">论文 / 专业文档 RAG 工作台</div>
            </div>
            <div class="lc-version">当前版本：{__version__}</div>
            """,
            unsafe_allow_html=True,
        )

        selected_page = sac.menu(
            [
                sac.MenuItem("普通对话", icon="chat"),
                sac.MenuItem("知识库问答", icon="database"),
                sac.MenuItem("知识库管理", icon="hdd-stack"),
            ],
            key="selected_page",
            open_index=0,
        )

        sac.divider()

    if selected_page == "知识库管理":
        page_header(
            "知识库管理",
            "上传论文和专业文档，维护知识库说明，并按需重建向量索引。",
            ("PDF / Word / Markdown", "本地向量库", "批量入库"),
        )
        knowledge_base_page(api=api, is_lite=is_lite)
    elif selected_page == "知识库问答":
        page_header(
            "知识库问答",
            "选择知识库后提问，系统会先检索相关片段，再交给本地模型生成回答。",
            ("RAG 检索", "引用片段", "本地模型"),
        )
        kb_chat(api=api)
    else:
        page_header(
            "普通对话",
            "直接与本地大语言模型交流，也可以按需启用工具或图片输入。",
            ("本地对话", "工具调用", "可导出记录"),
        )
        dialogue_page(api=api, is_lite=is_lite)
