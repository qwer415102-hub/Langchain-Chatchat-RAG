import streamlit as st


APP_TITLE = "本地论文知识库问答系统"


def inject_custom_style() -> None:
    st.markdown(
        """
        <style>
        :root {
            --lc-bg: #f6f8fb;
            --lc-panel: #ffffff;
            --lc-border: #d8e0e8;
            --lc-text: #172033;
            --lc-muted: #64748b;
            --lc-accent: #0f766e;
            --lc-accent-2: #2563eb;
            --lc-sidebar: #111827;
        }

        .stApp {
            background:
                radial-gradient(circle at top left, rgba(15, 118, 110, 0.10), transparent 32rem),
                linear-gradient(180deg, #f8fafc 0%, #eef5f4 100%);
            color: var(--lc-text);
        }

        .block-container {
            max-width: 1180px;
            padding-top: 1.1rem;
            padding-bottom: 6rem;
        }

        [data-testid="stSidebar"] {
            background: linear-gradient(180deg, #111827 0%, #172033 100%);
            border-right: 1px solid rgba(255,255,255,0.08);
        }

        [data-testid="stSidebar"] * {
            color: rgba(255,255,255,0.90);
        }

        [data-testid="stSidebarUserContent"] {
            padding-top: 1.2rem;
        }

        [data-testid="stBottomBlockContainer"] {
            padding-bottom: 1rem;
            background: rgba(246, 248, 251, 0.92);
            backdrop-filter: blur(10px);
            border-top: 1px solid rgba(15, 23, 42, 0.08);
        }

        .lc-brand {
            padding: 0.85rem 0.2rem 1rem;
        }

        .lc-brand-title {
            font-size: 1.18rem;
            font-weight: 750;
            line-height: 1.25;
            color: #ffffff;
        }

        .lc-brand-subtitle {
            margin-top: 0.35rem;
            color: rgba(255,255,255,0.64);
            font-size: 0.88rem;
        }

        .lc-version {
            color: rgba(255,255,255,0.58);
            font-size: 0.78rem;
            text-align: right;
            margin-top: -0.35rem;
            margin-bottom: 0.7rem;
        }

        .lc-page-header {
            background: rgba(255,255,255,0.74);
            border: 1px solid rgba(216,224,232,0.95);
            border-radius: 8px;
            padding: 1rem 1.15rem;
            margin-bottom: 1rem;
            box-shadow: 0 10px 24px rgba(15, 23, 42, 0.06);
        }

        .lc-page-kicker {
            color: var(--lc-accent);
            font-size: 0.76rem;
            font-weight: 700;
            letter-spacing: 0;
            margin-bottom: 0.25rem;
        }

        .lc-page-title {
            font-size: 1.55rem;
            font-weight: 760;
            line-height: 1.22;
            color: var(--lc-text);
        }

        .lc-page-subtitle {
            color: var(--lc-muted);
            font-size: 0.94rem;
            line-height: 1.7;
            margin-top: 0.32rem;
        }

        .lc-chip-row {
            display: flex;
            gap: 0.45rem;
            flex-wrap: wrap;
            margin-top: 0.65rem;
        }

        .lc-chip {
            display: inline-flex;
            align-items: center;
            border: 1px solid #cbd5e1;
            background: #f8fafc;
            color: #334155;
            border-radius: 999px;
            padding: 0.24rem 0.56rem;
            font-size: 0.78rem;
            line-height: 1.2;
        }

        .stButton > button,
        .stDownloadButton > button,
        [data-testid="baseButton-secondary"],
        [data-testid="baseButton-primary"] {
            border-radius: 8px !important;
            border: 1px solid #cbd5e1;
            box-shadow: 0 1px 2px rgba(15, 23, 42, 0.05);
            font-weight: 650;
        }

        [data-testid="baseButton-primary"] {
            background: var(--lc-accent) !important;
            border-color: var(--lc-accent) !important;
        }

        div[data-testid="stExpander"] {
            border: 1px solid var(--lc-border);
            border-radius: 8px;
            background: rgba(255,255,255,0.78);
            box-shadow: 0 8px 18px rgba(15, 23, 42, 0.04);
        }

        div[data-testid="stFileUploader"] section {
            border-radius: 8px;
            border-color: #bdd1d3;
            background: rgba(255,255,255,0.72);
        }

        div[data-baseweb="input"],
        div[data-baseweb="select"] > div,
        textarea {
            border-radius: 8px !important;
        }

        .stChatMessage {
            border-radius: 8px;
        }

        iframe {
            border-radius: 8px;
        }

        #MainMenu, footer, [data-testid="stToolbar"] {
            visibility: hidden;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


def page_header(title: str, subtitle: str = "", chips: tuple[str, ...] = ()) -> None:
    chips_html = "".join(f"<span class='lc-chip'>{chip}</span>" for chip in chips)
    subtitle_html = f"<div class='lc-page-subtitle'>{subtitle}</div>" if subtitle else ""
    chip_row = f"<div class='lc-chip-row'>{chips_html}</div>" if chips_html else ""
    st.markdown(
        f"""
        <div class="lc-page-header">
            <div class="lc-page-kicker">LOCAL RAG WORKSPACE</div>
            <div class="lc-page-title">{title}</div>
            {subtitle_html}
            {chip_row}
        </div>
        """,
        unsafe_allow_html=True,
    )
