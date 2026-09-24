import streamlit as st


st.set_page_config(
    page_title="Hugging Face CLI 使用指南",
    page_icon="HF",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown(
    """
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Mono:wght@400;500&family=Manrope:wght@400;600;700;800&family=Noto+Sans+TC:wght@400;500;700;900&display=swap');
:root { --ink:#17221f; --forest:#153d35; --paper:#f5f5ef; --lime:#cfe86b; --gold:#e9b949; --rust:#b75e42; --line:#d7ded6; --muted:#63716b; }
.stApp { background:var(--paper); color:var(--ink); }
.block-container { max-width:1240px; padding:2.2rem 4rem 4rem; }
html, body, [class*="css"] { font-family:'Noto Sans TC','Manrope',sans-serif; }
h1,h2,h3 { font-family:'Manrope','Noto Sans TC',sans-serif; letter-spacing:-.035em; }
h1 { font-size:clamp(2.8rem,6vw,6.6rem); line-height:.95; font-weight:800; margin:.4rem 0 1.2rem; }
h2 { font-size:clamp(1.8rem,3vw,3rem); line-height:1; margin:2.8rem 0 1.1rem; }
h3 { font-size:1.1rem; margin:0 0 .6rem; }
p,li { line-height:1.75; }
code,pre,.stCode { font-family:'DM Mono',monospace !important; }
.topbar { display:flex; justify-content:space-between; align-items:center; border-bottom:1px solid var(--line); padding-bottom:1.1rem; gap:1rem; }
.brand { font:800 1.05rem 'Manrope',sans-serif; }.brand em { color:var(--rust); font-style:normal; }
.topmeta { color:var(--muted); font:.72rem 'DM Mono',monospace; letter-spacing:.06em; text-transform:uppercase; }
.nav-link { color:var(--forest); border:1px solid var(--forest); border-radius:4px; padding:.48rem .72rem; font-size:.78rem; font-weight:700; text-decoration:none; white-space:nowrap; }
.nav-link:hover { background:var(--lime); color:var(--ink); }
.eyebrow { color:var(--rust); font:500 .76rem 'DM Mono',monospace; letter-spacing:.1em; text-transform:uppercase; }
.hero { padding:5.3rem 0 4rem; border-bottom:1px solid var(--line); }
.hero-copy { color:var(--muted); font-size:1.1rem; max-width:730px; line-height:1.85; }
.hero-kicker { display:inline-block; background:var(--lime); padding:.4rem .75rem; font:500 .73rem 'DM Mono',monospace; margin-top:1.1rem; }
.section-label { display:flex; align-items:center; gap:.8rem; color:var(--muted); font:500 .72rem 'DM Mono',monospace; text-transform:uppercase; letter-spacing:.08em; }
.section-label:after { content:""; height:1px; width:55px; background:var(--gold); }
.panel { background:#fffef9; border:1px solid var(--line); border-radius:6px; padding:1.3rem; min-height:190px; box-shadow:0 12px 28px rgba(21,61,53,.045); }
.panel .num { color:var(--rust); font:500 .73rem 'DM Mono',monospace; margin-bottom:1.7rem; }
.panel p { color:var(--muted); font-size:.92rem; }
.note { background:#e6f1eb; border-left:4px solid var(--gold); padding:1rem 1.2rem; color:#40544c; }
.footer { border-top:1px solid var(--line); margin-top:3rem; padding-top:1rem; color:var(--muted); font-size:.75rem; }
[data-testid="stSidebar"] { background:var(--forest); }
@media (max-width:700px) { .block-container { padding:1.3rem 1.25rem 3rem; } .hero { padding:3.2rem 0 3rem; } .topbar { align-items:flex-start; flex-direction:column; } }
</style>
""",
    unsafe_allow_html=True,
)

st.markdown(
    '<div class="topbar"><div class="brand">Hugging Face <em>／</em> CLI 指南</div><div style="display:flex;align-items:center;gap:1rem;flex-wrap:wrap"><div class="topmeta">MODEL HUB · DATASET · SPACE</div></div></div>',
    unsafe_allow_html=True,
)

st.markdown(
    """
<div class="hero">
  <div class="eyebrow">Hugging Face Hub / Command Line Workflow</div>
  <h1>用 CLI 管理<br>模型的生命週期。</h1>
  <div class="hero-copy">Hugging Face CLI（現代指令為 <code>hf</code>）把模型、資料集、Spaces、權限與本地快取整合在同一個終端工作流。這是企業導入 LLM、RAG 與本地推理服務時，最常用的模型資產管理入口。</div>
  <div class="hero-kicker">INSTALL · AUTH · DOWNLOAD · UPLOAD · CACHE</div>
</div>
""",
    unsafe_allow_html=True,
)

st.markdown('<div class="section-label">01 / CLI 是什麼</div>', unsafe_allow_html=True)
st.header("從 Hub 到本地推理環境")
cols = st.columns(3)
for col, (num, title, body) in zip(
    cols,
    [
        ("01 / HUB", "模型與資料資產", "瀏覽與取得公開或私有的模型、資料集、Spaces 與版本資訊。"),
        ("02 / LOCAL", "下載與快取", "把模型下載到本機快取，供 Rapid-MLX、Transformers、vLLM 或其他推理工具使用。"),
        ("03 / TEAM", "權限與協作", "使用 token 存取 private repo，並把企業模型、資料集與 Space 以 Git-like 方式管理。"),
    ],
):
    with col:
        st.markdown(f'<div class="panel"><div class="num">{num}</div><h3>{title}</h3><p>{body}</p></div>', unsafe_allow_html=True)

st.markdown('<div class="section-label">02 / 安裝與登入</div>', unsafe_allow_html=True)
st.header("建立第一個可用的 hf 指令")
st.code(
    """# 安裝 Hugging Face Hub CLI
python -m pip install -U huggingface_hub

# 確認版本與環境
hf version
hf env

# 互動式登入（token 不要寫進程式碼或 Git）
hf auth login

# 查看目前登入帳號
hf auth whoami

# 登出目前環境
hf auth logout""",
    language="bash",
)
st.markdown('<div class="note">Token 建議從 Hugging Face Settings → Access Tokens 建立，並依工作需求選擇 read 或 write 權限。企業 CI/CD 請使用環境變數或 secret manager，不要把 token 放進 shell history、README 或原始碼。</div>', unsafe_allow_html=True)

st.markdown('<div class="section-label">03 / 下載模型與資料集</div>', unsafe_allow_html=True)
st.header("最常用的 hf download")
st.code(
    """# 下載完整模型 repository 到快取，輸出本地路徑
hf download Qwen/Qwen3.5-4B

# 只下載需要的檔案
hf download Qwen/Qwen3.5-4B config.json tokenizer.json

# 下載到指定資料夾
hf download Qwen/Qwen3.5-4B --local-dir ./models/qwen3.5-4b

# 下載特定 revision / branch / tag
hf download org/model-name --revision main

# 下載資料集 repository
hf download org/company-dataset --repo-type dataset

# 下載 Space repository
hf download org/demo-space --repo-type space""",
    language="bash",
)
cols = st.columns(2)
with cols[0]:
    st.markdown('<div class="panel"><div class="num">MODEL ID</div><h3>如何找到 repo id？</h3><p>模型頁 URL 的第一段是 owner，第二段是 repository，例如 <code>Qwen/Qwen3.5-4B</code>。私有 repo 必須先完成 <code>hf auth login</code>。</p></div>', unsafe_allow_html=True)
with cols[1]:
    st.markdown('<div class="panel"><div class="num">REPO TYPE</div><h3>模型、資料集、Space</h3><p>模型預設不需要 <code>--repo-type</code>；資料集用 <code>dataset</code>，Space 用 <code>space</code>。這個參數是最常見的差異。</p></div>', unsafe_allow_html=True)

st.markdown('<div class="section-label">04 / 上傳與協作</div>', unsafe_allow_html=True)
st.header("把企業產出放回 Hub")
st.code(
    """# 上傳單一檔案到模型 repo
hf upload org/model-name ./model.safetensors model.safetensors

# 上傳整個資料夾
hf upload org/model-name ./exported-model .

# 上傳資料集資料夾
hf upload org/company-dataset ./data . --repo-type dataset

# 上傳前先查看說明
hf upload --help

# 列出 repository 檔案
hf repo-files org/model-name""",
    language="bash",
)
st.markdown('<div class="note">首次上傳到尚不存在的 repo 時，請先在 Hugging Face Hub 建立 repository，或使用對應的 API／CLI 流程建立。大型模型建議先確認 Git LFS、網路、儲存空間與 repo 權限。</div>', unsafe_allow_html=True)

st.markdown('<div class="section-label">05 / 快取管理</div>', unsafe_allow_html=True)
st.header("找出模型、清理空間、保持環境可控")
st.code(
    """# 查看 Hugging Face 快取內容與大小
hf cache ls

# 檢查快取狀態
hf cache scan

# 互動式清理未使用的快取
hf cache prune

# 查看完整 cache 指令
hf cache --help""",
    language="bash",
)

st.markdown('<div class="section-label">06 / 與 Rapid-MLX 串接</div>', unsafe_allow_html=True)
st.header("下載模型，再交給本地推理服務")
st.code(
    """# 1. 下載或確認模型 alias / repo 所需檔案
hf download <ORG>/<MODEL> --local-dir ./models/<MODEL>

# 2. 以 Rapid-MLX 的 alias 啟動已支援模型
rapid-mlx serve qwen3.5-4b-4bit

# 3. 若使用本地路徑或自訂模型，先查看 Rapid-MLX 版本支援的 flags
rapid-mlx serve --help
rapid-mlx info <MODEL>""",
    language="bash",
)
st.markdown('<div class="note">Hugging Face 負責模型資產的發現、下載、版本與權限；Rapid-MLX 負責 Apple Silicon 上的本地推理與 API 服務。實際模型是否能直接載入，仍要依 Rapid-MLX 版本、模型格式與官方支援清單確認。</div>', unsafe_allow_html=True)

st.markdown('<div class="section-label">07 / 指令速查</div>', unsafe_allow_html=True)
st.header("常用 hf 指令地圖")
commands = [
    ("hf version / hf env", "查看 CLI 版本與執行環境。"),
    ("hf auth login / whoami / logout", "登入、查看帳號、登出。"),
    ("hf download", "下載模型、資料集或 Space。"),
    ("hf upload", "上傳檔案或資料夾到 Hub。"),
    ("hf repo-files", "查看 repository 內的檔案。"),
    ("hf cache ls / scan / prune", "檢查與管理本地快取。"),
    ("hf jobs", "在支援的環境管理 Hugging Face Jobs。"),
    ("hf upload-large-folder", "處理大型資料夾上傳工作流。"),
    ("hf <command> --help", "查詢目前安裝版本的完整參數。"),
]
st.dataframe([{"指令": command, "功能": description} for command, description in commands], use_container_width=True, hide_index=True)

st.markdown('<div class="footer">Hugging Face CLI 使用指南 · 現代 CLI 指令為 <code>hf</code>；舊版文件可能使用 <code>huggingface-cli</code>，請優先以目前套件版本的 <code>hf --help</code> 為準。<br><br><strong>AI落地服務提供單位</strong><br>美亮資訊顧問有限公司<br>需求洽談：<a href="mailto:mymis168@mymis.tw">mymis168@mymis.tw</a><br>官網：<a href="https://www.mis.com.tw" target="_blank">www.mis.com.tw</a> · <a href="https://www.mymis.tw" target="_blank">www.mymis.tw</a></div>', unsafe_allow_html=True)
