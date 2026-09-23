import streamlit as st


st.set_page_config(
    page_title="美亮資訊｜Apple M-Chip 落地模型方案",
    page_icon="◒",
    layout="wide",
    initial_sidebar_state="collapsed",
)


st.markdown(
    """
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Mono:wght@400;500&family=Manrope:wght@400;600;700;800&family=Noto+Sans+TC:wght@400;500;700;900&display=swap');
:root {
  --ink: #17221f;
  --forest: #153d35;
  --mint: #dceee6;
  --paper: #f5f5ef;
  --lime: #cfe86b;
  --gold: #e9b949;
  --rust: #b75e42;
  --line: #d7ded6;
  --muted: #63716b;
}
.stApp { background: var(--paper); color: var(--ink); }
.block-container { max-width: 1240px; padding: 2.2rem 4rem 4rem; }
html, body, [class*="css"] { font-family: 'Noto Sans TC', 'Manrope', sans-serif; }
h1, h2, h3 { font-family: 'Manrope', 'Noto Sans TC', sans-serif; letter-spacing: -0.035em; }
h1 { font-size: clamp(2.8rem, 6.3vw, 7.2rem); line-height: .94; font-weight: 800; margin: .35rem 0 1.2rem; }
h2 { font-size: clamp(1.8rem, 3vw, 3.1rem); line-height: 1; margin: 2.9rem 0 1.15rem; }
h3 { font-size: 1.12rem; margin: 0 0 .6rem; }
p, li { line-height: 1.75; }
code, pre, .stCode { font-family: 'DM Mono', monospace !important; }
.topbar { display:flex; justify-content:space-between; align-items:center; border-bottom:1px solid var(--line); padding-bottom:1.1rem; }
.brand { font: 800 1.05rem 'Manrope', sans-serif; letter-spacing:-.03em; }
.brand em { color: var(--rust); font-style:normal; }
.topmeta { color:var(--muted); font: .72rem 'DM Mono', monospace; letter-spacing:.06em; text-transform:uppercase; }
.main-link { color:var(--forest); border:1px solid var(--forest); border-radius:4px; padding:.48rem .72rem; font-size:.78rem; font-weight:700; text-decoration:none; white-space:nowrap; }
.main-link:hover { background:var(--lime); color:var(--ink); }
.eyebrow { color:var(--rust); font: 500 .76rem 'DM Mono', monospace; letter-spacing:.1em; text-transform:uppercase; }
.hero { padding: 5.4rem 0 4.5rem; border-bottom:1px solid var(--line); position:relative; overflow:hidden; }
.hero-copy { color:var(--muted); font-size:1.12rem; max-width:660px; line-height:1.85; }
.hero-kicker { display:inline-block; background:var(--lime); padding:.4rem .75rem; font:500 .73rem 'DM Mono',monospace; margin:1.2rem 0 0; }
.hero-orbit { position:absolute; right:4%; top:17%; width:250px; height:250px; border:1px solid #adc5bb; border-radius:50%; opacity:.7; }
.hero-orbit:before, .hero-orbit:after { content:""; position:absolute; inset:26px; border:1px solid #adc5bb; border-radius:50%; }
.hero-orbit:after { inset:76px; background:var(--gold); border:0; opacity:.85; }
@media (max-width: 700px) { .block-container { padding: 1.3rem 1.25rem 3rem; } .hero { padding:3.2rem 0 3rem; } .hero-orbit { width:150px; height:150px; right:-42px; top:24%; opacity:.35; } }
.section-label { display:flex; align-items:center; gap:.8rem; color:var(--muted); font:500 .72rem 'DM Mono',monospace; text-transform:uppercase; letter-spacing:.08em; }
.section-label:after { content:""; height:1px; width:55px; background:var(--gold); }
.service-card { background:#fffef9; border:1px solid var(--line); border-radius:6px; padding:1.35rem; min-height:230px; box-shadow:0 12px 28px rgba(21,61,53,.045); }
.service-card .num { color:var(--rust); font:500 .74rem 'DM Mono',monospace; margin-bottom:2.2rem; }
.service-card p { color:var(--muted); font-size:.92rem; }
.service-card strong { color:var(--ink); }
.m-chip { background:var(--forest); color:#f2f5ec; border-radius:6px; padding:2rem; min-height:280px; }
.m-chip h3 { color:var(--lime); font-size:1.45rem; }
.m-chip p { color:#c5d6ce; }
.m-chip .chip-line { color:#f2f5ec; font: .73rem 'DM Mono',monospace; margin-top:1.4rem; }
.feature { border-top:3px solid var(--gold); padding-top:1rem; min-height:180px; }
.feature p { color:var(--muted); font-size:.92rem; }
.workflow { background:var(--mint); border-radius:6px; padding:1.45rem; min-height:190px; }
.workflow .step { color:var(--rust); font:500 .72rem 'DM Mono',monospace; }
.workflow p { color:#40544c; font-size:.9rem; }
.callout { background:var(--forest); color:#f3f6eb; border-radius:6px; padding:2.1rem 2.2rem; }
.callout h2 { color:var(--lime); margin-top:0; }
.callout p { color:#cad9d1; }
.contact { display:flex; gap:1rem; align-items:center; flex-wrap:wrap; margin-top:1.2rem; }
.contact a { color:var(--ink); background:var(--lime); border-radius:4px; padding:.65rem 1rem; font-weight:700; text-decoration:none; }
.footer { border-top:1px solid var(--line); margin-top:3rem; padding-top:1rem; color:var(--muted); font-size:.75rem; }
[data-testid="stSidebar"] { background:var(--forest); }
</style>
""",
    unsafe_allow_html=True,
)


st.markdown(
    '<div class="topbar"><div class="brand">美亮資訊 <em>／</em> 顧問服務</div><div style="display:flex;align-items:center;gap:1rem;flex-wrap:wrap"><div class="topmeta">LOCAL AI · ENTERPRISE MODEL DELIVERY</div><a class="main-link" href="http://localhost:8501" target="_self">Rapid-MLX 技術導覽 ↗</a><a class="main-link" href="http://localhost:8503" target="_self">Hugging Face CLI 指南 ↗</a><a class="main-link" href="http://localhost:8504" target="_self">GGUF 格式指南 ↗</a><a class="main-link" href="http://localhost:8505" target="_self">llama.cpp 部署指南 ↗</a></div></div>',
    unsafe_allow_html=True,
)

st.markdown(
    """
<div class="hero">
  <div class="hero-orbit"></div>
    <div class="eyebrow">Professional AI Deployment &amp; Advisory</div>
    <h1>專業落地建置<br>與部署專業服務</h1>
    <div class="hero-copy">美亮資訊顧問有限公司提供從模型選型、環境建置、資料整合到正式部署的專業技術顧問團隊，協助企業將 LLM、Audio、Video 與 Text-Speech-Text 應用導入實際業務流程。</div>
    <div class="hero-kicker">LLM · AUDIO · VIDEO · TEXT-SPEECH-TEXT</div>
</div>
""",
    unsafe_allow_html=True,
)

st.markdown('<div class="section-label">00 / 專業技術顧問團隊</div>', unsafe_allow_html=True)
st.header("從模型能力，到企業真正用得起來的服務")
st.markdown(
        """
        我們的顧問團隊涵蓋模型訓練、推理部署、資料工程、語音技術、影音生成與企業系統整合，
        依照企業的資料敏感度、硬體條件、使用情境與預算，規劃可落地、可維運、可持續擴充的 AI 方案。
        """
)

advisor_cols = st.columns(4)
advisor_services = [
        ("LLM", "大型語言模型", "模型部署、微調、Prompt、Agent、RAG 與企業知識系統整合。"),
        ("AUDIO", "語音與聲音服務", "語音辨識、文字轉語音、語音分析與企業語音流程導入。"),
        ("VIDEO", "影音模型服務", "影像理解、影片分析、生成式影音與多媒體工作流建置。"),
        ("T-S-T", "Text-Speech-Text", "文字、語音雙向轉換，打造客服、助理、會議與現場作業的自然互動入口。"),
]
for col, (label, title, body) in zip(advisor_cols, advisor_services):
        with col:
                st.markdown(f'<div class="service-card"><div class="num">{label} / ADVISORY</div><h3>{title}</h3><p>{body}</p></div>', unsafe_allow_html=True)

st.markdown('<div class="section-label">01 / 我們提供什麼</div>', unsafe_allow_html=True)
st.header("企業落地模型的完整路徑")

services = [
    ("01", "落地模型建置", "依據企業硬體、資料與資安要求，完成模型部署、推理服務、權限邊界與日常維運。"),
    ("02", "SLM 專屬模型訓練", "把公司知識、ERP 資訊與工作流程轉成可查詢、可輔助決策的企業領域模型。"),
    ("03", "教育訓練", "從模型訓練基礎開發，到 RAG、向量嵌入與企業資料平台，建立團隊自己的 AI 能力。"),
    ("04", "顧問與整合", "從需求盤點、PoC、架構選型，到上線後的資料治理與效能調校，陪伴方案持續成長。"),
]
cols = st.columns(4)
for col, (number, title, body) in zip(cols, services):
    with col:
        st.markdown(f'<div class="service-card"><div class="num">{number} / SERVICE</div><h3>{title}</h3><p>{body}</p></div>', unsafe_allow_html=True)

st.markdown('<div class="section-label">02 / 核心方案</div>', unsafe_allow_html=True)
st.header("Apple M-Chip：企業本地 AI 的靈活起點")
cols = st.columns([1.2, 1, 1])
with cols[0]:
    st.markdown(
        """
<div class="m-chip">
  <h3>為什麼選 Apple M-Chip？</h3>
  <p>Apple Silicon 以統一記憶體架構整合 CPU、GPU 與模型資料，適合建立低延遲、私有化、可在辦公場域運作的本地 AI 工作站。</p>
  <div class="chip-line">M-SERIES / UNIFIED MEMORY / ON-PREMISE</div>
</div>
""",
        unsafe_allow_html=True,
    )
with cols[1]:
    st.markdown('<div class="feature"><h3>資料不必離開企業</h3><p>模型與企業資料可在內部環境運作，降低敏感文件上傳外部服務的風險，並保留資料存取治理的主導權。</p></div>', unsafe_allow_html=True)
with cols[2]:
    st.markdown('<div class="feature"><h3>從個人工作站到部門服務</h3><p>可先以 M-Chip 進行模型選型、Prompt 與 RAG 驗證，再依使用量擴充成部門級或混合式部署。</p></div>', unsafe_allow_html=True)

st.markdown("""
<div class="note" style="background:#fffef9;border-left:4px solid #e9b949;padding:1rem 1.2rem;margin-top:1.2rem;color:#63716b;">
Apple M-Chip 方案適合重視隱私、希望快速啟動 PoC，或需要在無網路／有限網路環境下運行模型的企業。實際硬體、模型大小與量化方式，會依資料量、同時使用人數及任務類型評估。
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="section-label">03 / 技術服務矩陣</div>', unsafe_allow_html=True)
st.header("不只 Apple：依場景選擇部署平台")
platforms = st.columns(3)
with platforms[0]:
    st.markdown('<div class="workflow"><div class="step">01 / NVIDIA RTX GPU</div><h3>Nvidia RTX GPU 系列落地模型建置</h3><p>適合需要較高推理吞吐、視覺模型、多人併發與彈性擴充的企業內部服務。</p></div>', unsafe_allow_html=True)
with platforms[1]:
    st.markdown('<div class="workflow"><div class="step">02 / NVIDIA DGX SPARK</div><h3>Nvidia DGX Spark 落地模型訓練</h3><p>支援企業進行模型訓練、微調與實驗環境建置，將資料與訓練流程集中管理。</p></div>', unsafe_allow_html=True)
with platforms[2]:
    st.markdown('<div class="workflow"><div class="step">03 / APPLE M-CHIP</div><h3>Apple M-Chip 系列落地建置</h3><p>以低維運負擔與本地化為優先，適合個人、部門與中小型企業快速部署私有模型。</p></div>', unsafe_allow_html=True)

st.markdown('<div class="section-label">04 / 企業專屬模型</div>', unsafe_allow_html=True)
st.header("SLM 訓練：把公司的經驗變成可用的知識")
slm_cols = st.columns(3)
for col, title, body in zip(
    slm_cols,
    ["公司資料查詢", "公司相關知識系統模型訓練", "公司 ERP 資訊與模型整合訓練"],
    ["建立自然語言查詢入口，讓同仁更快找到制度、流程、產品與營運資料。", "整合內規、手冊、SOP、FAQ 與專案文件，讓模型回答有來源、有脈絡。", "串接 ERP 既有資訊與權限邏輯，將查詢、彙整與分析帶進日常工作流程。"],
):
    with col:
        st.markdown(f'<div class="feature"><h3>{title}</h3><p>{body}</p></div>', unsafe_allow_html=True)

st.markdown('<div class="section-label">05 / 教育訓練</div>', unsafe_allow_html=True)
st.header("讓團隊從使用者，成為建置者")
training = st.columns(4)
training_items = [
    ("A", "模型訓練之基礎開發", "理解模型、資料、Prompt、微調與評估的基本方法。"),
    ("B", "RAG 文件與向量嵌入服務", "從文件切分、嵌入、檢索到回覆引用，建立可追溯的知識服務。"),
    ("C", "Snowflake 企業資料倉儲", "認識企業資料倉儲、資料治理與 AI 應用的連接方式。"),
    ("D", "Fabric 企業雲端資料整合分析", "串起資料整合、分析與模型應用，建立跨部門的資料工作流。"),
]
for col, (mark, title, body) in zip(training, training_items):
    with col:
        st.markdown(f'<div class="service-card" style="min-height:195px"><div class="num">{mark} / TRAINING</div><h3>{title}</h3><p>{body}</p></div>', unsafe_allow_html=True)

st.markdown('<div class="section-label">06 / 合作方式</div>', unsafe_allow_html=True)
cols = st.columns([1.25, 1])
with cols[0]:
    st.markdown(
        """
<div class="callout">
  <h2>從一個清楚的問題開始。</h2>
  <p>我們會先釐清資料在哪裡、誰會使用、模型要回答什麼，以及企業需要保留哪些控制權，再選擇適合的硬體、模型與導入路徑。</p>
  <div class="contact"><a href="mailto:mymis168@mymis.tw">mymis168@mymis.tw</a><span>美亮資訊顧問有限公司</span></div>
</div>
""",
        unsafe_allow_html=True,
    )
with cols[1]:
    st.markdown('<div class="feature"><h3>適合洽談的起點</h3><p>想在企業內部使用生成式 AI</p><p>需要模型與 ERP / 文件系統整合</p><p>評估 Apple M-Chip、RTX 或 DGX Spark</p><p>規劃團隊 AI 與資料平台教育訓練</p></div>', unsafe_allow_html=True)

st.markdown('<div class="footer">美亮資訊顧問有限公司 · Apple M-Chip / NVIDIA GPU / Enterprise SLM / RAG · 聯絡：mymis168@mymis.tw<br><br><strong>AI落地服務提供單位</strong><br>美亮資訊顧問有限公司<br>需求洽談：<a href="mailto:mymis168@mymis.tw">mymis168@mymis.tw</a><br>官網：<a href="https://www.mis.com.tw" target="_blank">www.mis.com.tw</a> · <a href="https://www.mymis.tw" target="_blank">www.mymis.tw</a></div>', unsafe_allow_html=True)
