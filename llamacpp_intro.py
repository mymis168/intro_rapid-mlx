import streamlit as st


st.set_page_config(
    page_title="llama.cpp 建置與部署指南",
    page_icon="LC",
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
.hero-copy { color:var(--muted); font-size:1.1rem; max-width:780px; line-height:1.85; }
.hero-kicker { display:inline-block; background:var(--lime); padding:.4rem .75rem; font:500 .73rem 'DM Mono',monospace; margin-top:1.1rem; }
.section-label { display:flex; align-items:center; gap:.8rem; color:var(--muted); font:500 .72rem 'DM Mono',monospace; text-transform:uppercase; letter-spacing:.08em; }
.section-label:after { content:""; height:1px; width:55px; background:var(--gold); }
.panel { background:#fffef9; border:1px solid var(--line); border-radius:6px; padding:1.3rem; min-height:190px; box-shadow:0 12px 28px rgba(21,61,53,.045); }
.panel .num { color:var(--rust); font:500 .73rem 'DM Mono',monospace; margin-bottom:1.7rem; }
.panel p { color:var(--muted); font-size:.92rem; }
.note { background:#e6f1eb; border-left:4px solid var(--gold); padding:1rem 1.2rem; color:#40544c; }
.warning { background:#fff4df; border-left:4px solid var(--rust); padding:1rem 1.2rem; color:#684736; }
.footer { border-top:1px solid var(--line); margin-top:3rem; padding-top:1rem; color:var(--muted); font-size:.75rem; }
[data-testid="stSidebar"] { background:var(--forest); }
@media (max-width:700px) { .block-container { padding:1.3rem 1.25rem 3rem; } .hero { padding:3.2rem 0 3rem; } .topbar { align-items:flex-start; flex-direction:column; } }
</style>
""",
    unsafe_allow_html=True,
)

st.markdown(
    '<div class="topbar"><div class="brand">llama.cpp <em>／</em> 建置與部署</div><div style="display:flex;align-items:center;gap:1rem;flex-wrap:wrap"><div class="topmeta">CUDA · METAL · LOCAL INFERENCE</div><a class="nav-link" href="http://localhost:8504" target="_self">GGUF 格式指南 ↗</a><a class="nav-link" href="http://localhost:8502" target="_self">美亮資訊方案 ↗</a></div></div>',
    unsafe_allow_html=True,
)

st.markdown(
    """
<div class="hero">
  <div class="eyebrow">llama.cpp / CUDA + Metal Deployment</div>
  <h1>同一個模型，<br>兩條本地路徑。</h1>
  <div class="hero-copy">llama.cpp 是以 C/C++ 實作的本地推理工具鏈，能把 GGUF 模型跑在 NVIDIA CUDA 與 Apple Metal 上。這份指南從第一個 prompt 開始，帶你完成 DGX Spark 與 Mac 的建置、模型載入、API 部署、資源管理與進階調校。</div>
  <div class="hero-kicker">DGX SPARK / CUDA · MAC / METAL · GGUF</div>
</div>
""",
    unsafe_allow_html=True,
)

st.markdown('<div class="section-label">01 / 入門心智模型</div>', unsafe_allow_html=True)
st.header("llama.cpp 負責什麼？")
cols = st.columns(3)
for col, (num, title, body) in zip(
    cols,
    [
        ("01 / RUNTIME", "推理 runtime", "讀取 GGUF，執行 tokenization、sampling、KV cache 與 token generation。"),
        ("02 / BACKEND", "硬體 backend", "同一套上層 CLI 可搭配 CPU、CUDA、Metal、Vulkan 或其他已支援 backend。"),
        ("03 / SERVICE", "服務入口", "llama-server 提供 OpenAI-compatible API，讓應用程式與 agent 連接本地模型。"),
    ],
):
    with col:
        st.markdown(f'<div class="panel"><div class="num">{num}</div><h3>{title}</h3><p>{body}</p></div>', unsafe_allow_html=True)

st.markdown('<div class="section-label">02 / 環境建置</div>', unsafe_allow_html=True)
st.header("先選平台，再選 backend")
st.dataframe(
    [
        {"平台": "NVIDIA DGX Spark", "硬體路徑": "CUDA / NVIDIA GPU backend", "建置重點": "ARM64、CUDA toolkit、GPU driver、CMake、CUDA arch 與顯存／統一記憶體觀察。"},
        {"平台": "Apple M-Chip Mac", "硬體路徑": "Metal / Apple Silicon backend", "建置重點": "Xcode Command Line Tools、CMake、Metal backend、統一記憶體與量化模型選擇。"},
    ],
    use_container_width=True,
    hide_index=True,
)
st.markdown('<div class="note">DGX Spark 與 Mac 的共同層是 GGUF 與 llama.cpp CLI；差異主要在編譯 backend、GPU offload 參數、記憶體模型與效能調校。先用同一個模型做功能驗證，再分平台調整效能。</div>', unsafe_allow_html=True)

st.markdown('<div class="section-label">03 / DGX Spark</div>', unsafe_allow_html=True)
st.header("NVIDIA DGX Spark：CUDA 建置步驟")
st.subheader("A. 環境檢查")
st.code(
    """# 確認系統架構、GPU 與 driver
uname -m
nvidia-smi
nvcc --version
cmake --version

# DGX Spark 可能使用 ARM64；請使用與環境相容的 CUDA toolkit、compiler 與 llama.cpp 版本
""",
    language="bash",
)
st.subheader("B. 從原始碼編譯 CUDA backend")
st.code(
    """git clone https://github.com/ggml-org/llama.cpp.git
cd llama.cpp
cmake -B build -DGGML_CUDA=ON -DCMAKE_BUILD_TYPE=Release
cmake --build build --config Release -j

# 確認 binary
./build/bin/llama-cli --help
./build/bin/llama-server --help""",
    language="bash",
)
st.markdown('<div class="warning">DGX Spark 是 ARM64／Grace Blackwell 類型的 NVIDIA 平台，實際 CUDA、driver、compiler 與預編譯 binary 相容性要以你的映像與版本為準。若預編譯檔無法執行，優先在目標環境從 source build。</div>', unsafe_allow_html=True)
st.subheader("C. 第一個推理請求")
st.code(
    """# 先用小型 Q4 GGUF 驗證 CUDA 路徑
./build/bin/llama-cli \\
  -m ./models/model.Q4_K_M.gguf \\
  -ngl 999 \\
  -c 4096 \\
  -p "請用三句話介紹 DGX Spark""",
    language="bash",
)

st.markdown('<div class="section-label">04 / Mac</div>', unsafe_allow_html=True)
st.header("Apple M-Chip Mac：Metal 建置步驟")
st.subheader("A. 安裝工具與編譯")
st.code(
    """# 安裝 Apple Command Line Tools
xcode-select --install

# 取得 llama.cpp
 git clone https://github.com/ggml-org/llama.cpp.git
cd llama.cpp

# Metal 在 Apple Silicon 通常是預設啟用；明確指定可增加可讀性
cmake -B build -DGGML_METAL=ON -DCMAKE_BUILD_TYPE=Release
cmake --build build --config Release -j

./build/bin/llama-cli --help""",
    language="bash",
)
st.subheader("B. 以 Metal 載入 GGUF")
st.code(
    """./build/bin/llama-cli \\
  -m ./models/model.Q4_K_M.gguf \\
  -ngl 999 \\
  -c 4096 \\
  --temp 0.7 \\
  -p "請說明 Apple M-Chip 的統一記憶體""",
    language="bash",
)
st.markdown('<div class="note">`-ngl 999` 代表盡可能將 layers offload 到 GPU；若模型太大或遇到記憶體壓力，改用較小量化、降低 context，或逐步降低 GPU layers。Apple Silicon 的 CPU、GPU 與模型共同使用 unified memory。</div>', unsafe_allow_html=True)

st.markdown('<div class="section-label">05 / 模型來源</div>', unsafe_allow_html=True)
st.header("模型從哪裡來？")
cols = st.columns(3)
for col, (num, title, body) in zip(
    cols,
    [
        ("01 / HF GGUF", "Hugging Face GGUF repository", "使用 `hf download` 下載已轉換與量化的 GGUF；先讀模型卡、license、量化說明與 chat template。"),
        ("02 / LOCAL", "企業內部模型目錄", "把模型放在固定的 `/models` 或版本化目錄，以 checksum、revision、量化版本與 owner 管理。"),
        ("03 / CONVERT", "HF Safetensors 轉換", "先用 llama.cpp converter 轉成 F16 GGUF，再用 quantize 產生 Q4／Q5／Q8 版本。"),
    ],
):
    with col:
        st.markdown(f'<div class="panel"><div class="num">{num}</div><h3>{title}</h3><p>{body}</p></div>', unsafe_allow_html=True)

st.code(
    """# Hugging Face CLI
hf auth login
hf download <ORG>/<GGUF-REPO> \\
  <MODEL>.Q4_K_M.gguf \\
  --local-dir ./models/<MODEL>

# llama.cpp 直接從 Hugging Face 載入的選項名稱依版本不同，先查 help
./build/bin/llama-cli --help | grep -E "hf|repo|file"

# Safetensors -> F16 GGUF -> quantized GGUF
python convert_hf_to_gguf.py ./models/hf-model \\
  --outfile ./models/model.f16.gguf --outtype f16
./build/bin/llama-quantize \\
  ./models/model.f16.gguf ./models/model.Q4_K_M.gguf Q4_K_M""",
    language="bash",
)

st.markdown('<div class="section-label">06 / 載入與設定</div>', unsafe_allow_html=True)
st.header("把模型設定成可重複的啟動命令")
st.dataframe(
    [
        {"參數": "-m / --model", "作用": "指定 GGUF 檔案路徑；分片模型保持同目錄並依版本說明載入。"},
        {"參數": "-ngl / --n-gpu-layers", "作用": "指定 offload 到 GPU 的 layers；先求能跑，再以 benchmark 調整。"},
        {"參數": "-c / --ctx-size", "作用": "上下文長度；越大通常需要更多 KV cache 記憶體。"},
        {"參數": "-b / -ub", "作用": "logical batch 與 physical micro-batch；影響 prefill 記憶體與速度。"},
        {"參數": "-t / --threads", "作用": "CPU threads；CPU 或部分 prefill workload 可調整。"},
        {"參數": "--flash-attn", "作用": "在支援的 backend／模型上啟用 Flash Attention 路徑，需實測驗證。"},
        {"參數": "--temp / - top-p / top-k", "作用": "控制 sampling；評測時固定 seed 與 sampling 設定。"},
    ],
    use_container_width=True,
    hide_index=True,
)
st.code(
    """# 建議把固定設定寫成可審查的 shell script
MODEL=./models/model.Q4_K_M.gguf
CTX=8192

./build/bin/llama-cli \\
  -m "$MODEL" \\
  -ngl 999 \\
  -c "$CTX" \\
  -b 512 -ub 128 \\
  --flash-attn auto \\
  --temp 0.2 \\
  -p "你的測試問題""",
    language="bash",
)

st.markdown('<div class="section-label">07 / 部署服務</div>', unsafe_allow_html=True)
st.header("llama-server：給應用程式使用的 API")
st.code(
    """# DGX Spark / Linux
./build/bin/llama-server \\
  -m ./models/model.Q4_K_M.gguf \\
  -ngl 999 -c 8192 \\
  --host 0.0.0.0 --port 8080 \\
  --parallel 2

# Mac 本機服務
./build/bin/llama-server \\
  -m ./models/model.Q4_K_M.gguf \\
  -ngl 999 -c 4096 \\
  --host 127.0.0.1 --port 8080

# API smoke test
curl http://127.0.0.1:8080/v1/chat/completions \\
  -H "Content-Type: application/json" \\
  -d '{"model":"local","messages":[{"role":"user","content":"Hello"}]}'""",
    language="bash",
)
st.markdown('<div class="warning">只有在確定要提供內網服務時才使用 `--host 0.0.0.0`。請搭配反向代理、TLS、API key、網路 ACL 與 request log policy；不要把未驗證的本地 server 直接暴露到公網。</div>', unsafe_allow_html=True)

st.markdown('<div class="section-label">08 / 從入門到進階管理</div>', unsafe_allow_html=True)
st.header("一套可維運的模型管理觀念")
steps = [
    ("01 / 入門", "先讓模型可重現地跑起來", "固定 llama.cpp commit、GGUF 檔案 checksum、prompt、sampling、context 與硬體環境；先建立 smoke test。"),
    ("02 / 部署", "把 CLI 變成服務", "使用 llama-server、systemd 或容器管理啟停；以 health check、access log、資源監控與明確 port 管理服務。"),
    ("03 / 效能", "以實測決定參數", "記錄 prompt tokens、generation tokens、TTFT、tokens/s、RAM／VRAM 使用量與併發數，不要只比較單次主觀速度。"),
    ("04 / 進階", "建立模型與版本治理", "模型、量化、chat template、llama.cpp binary、設定檔與評測結果一起版本化；升級前先做回歸測試。"),
]
for number, title, body in steps:
    st.markdown(f'<div class="panel" style="margin:.7rem 0;min-height:0"><div class="num">{number}</div><h3>{title}</h3><p>{body}</p></div>', unsafe_allow_html=True)

st.markdown('<div class="section-label">09 / 平台選擇</div>', unsafe_allow_html=True)
st.header("DGX Spark 與 Mac 怎麼分工？")
st.dataframe(
    [
        {"情境": "個人與部門 PoC", "建議": "Apple M-Chip + Metal + Q4／Q5 GGUF；快速驗證資料、Prompt 與 RAG。"},
        {"情境": "企業內網多人服務", "建議": "DGX Spark + CUDA + llama-server；依併發、context 與模型大小規劃 offload 與 parallel。"},
        {"情境": "模型比較與發布", "建議": "以同一 GGUF、固定 prompt 與 benchmark protocol 分別測 Mac 與 DGX Spark。"},
        {"情境": "敏感資料環境", "建議": "模型、服務與 log 留在內網；建立 token 權限、資料遮罩、審計與更新流程。"},
    ],
    use_container_width=True,
    hide_index=True,
)

st.markdown('<div class="footer">llama.cpp 建置與部署指南 · 實際 CMake flags、CLI 參數與模型支援會隨 llama.cpp commit、CUDA／Metal backend 與模型架構變更，正式部署前請以目標版本的 <code>--help</code> 與 benchmark 結果為準。<br><br><strong>AI落地服務提供單位</strong><br>美亮資訊顧問有限公司<br>需求洽談：<a href="mailto:mymis168@mymis.tw">mymis168@mymis.tw</a><br>官網：<a href="https://www.mis.com.tw" target="_blank">www.mis.com.tw</a> · <a href="https://www.mymis.tw" target="_blank">www.mymis.tw</a></div>', unsafe_allow_html=True)
