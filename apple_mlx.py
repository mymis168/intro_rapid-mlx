import streamlit as st
from urllib.parse import quote


st.set_page_config(page_title="Rapid-MLX Field Guide", page_icon="⚡", layout="wide")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Mono:wght@400;500&family=Manrope:wght@400;600;700;800&display=swap');
:root { --ink:#17201f; --muted:#64706d; --paper:#f7f6f1; --lime:#c8f169; --orange:#f27e52; --line:#dfe2d8; }
.stApp { background:var(--paper); color:var(--ink); }
[data-testid="stSidebar"] { background:#202927; border-right:0; }
[data-testid="stSidebar"] * { color:#eef2e6; }
h1,h2,h3,p,li,.stMarkdown { font-family:'Manrope',sans-serif; }
h1 { font-size:clamp(2.5rem,5vw,5.6rem); line-height:.96; letter-spacing:-.04em; }
h2 { margin-top:2.2rem; letter-spacing:-.03em; }
code,pre,.stCode,[data-testid="stMetricValue"] { font-family:'DM Mono',monospace !important; }
.eyebrow { color:var(--orange); font:500 .78rem 'DM Mono',monospace; text-transform:uppercase; letter-spacing:.08em; }
.hero { padding:2.5rem 0 2rem; border-bottom:1px solid var(--line); }
.hero-copy { max-width:760px; color:var(--muted); font-size:1.13rem; line-height:1.7; }
.stamp { display:inline-block; background:var(--lime); padding:.35rem .7rem; margin-top:1rem; font:500 .72rem 'DM Mono',monospace; }
.panel { background:#fffef9; border:1px solid var(--line); border-radius:8px; padding:1.25rem 1.35rem; height:100%; box-shadow:0 8px 24px rgba(29,38,35,.04); }
.panel h3 { margin-top:0; }.panel p { color:var(--muted); line-height:1.6; }
.accent { border-left:4px solid var(--orange); padding-left:1rem; }
.flow { background:#202927; color:#eef2e6; border-radius:8px; padding:1.25rem; font:1rem/1.9 'DM Mono',monospace; }
.flow span { color:var(--lime); }.note { background:#edf4d7; border-radius:6px; padding:.8rem 1rem; color:#354030; }
.footer { margin-top:3rem; padding:1.3rem 0; border-top:1px solid var(--line); color:var(--muted); font-size:.8rem; }
div[data-testid="stMetric"] { background:#fffef9; border:1px solid var(--line); padding:1rem; border-radius:8px; }
</style>
""", unsafe_allow_html=True)


def code_block(text: str, language: str = "bash") -> None:
    st.code(text.strip(), language=language)


def header(eyebrow: str, title: str, description: str) -> None:
    st.markdown(f'<div class="hero"><div class="eyebrow">{eyebrow}</div><h1>{title}</h1><div class="hero-copy">{description}</div></div>', unsafe_allow_html=True)


def card(title: str, body: str) -> None:
    st.markdown(f'<div class="panel"><h3>{title}</h3><p>{body}</p></div>', unsafe_allow_html=True)


def architecture_page() -> None:
    header("01 / architecture", "Local inference,<br>without the detour.", "Rapid-MLX 是針對 Apple Silicon 的本地 AI inference engine。它以 Apple MLX 為核心，用同一套模型與 runtime 同時支援 terminal chat、OpenAI / Anthropic 相容服務，以及 macOS Desktop。")
    st.markdown('<span class="stamp">M1 → M4 · macOS · unified memory</span>', unsafe_allow_html=True)
    st.write("")
    cols = st.columns(3)
    with cols[0]: card("MLX-native", "直接使用 Apple Silicon 的 GPU / unified memory；不依賴 llama.cpp fallback，也不需要遠端 API 金鑰。")
    with cols[1]: card("API compatible", "serve 模式提供 OpenAI-compatible `/v1`，也提供 Anthropic `/v1/messages`，可接 agent、SDK 與既有應用。")
    with cols[2]: card("One engine", "Chat、Serve、Desktop 不是三套模型；它們共用模型 catalog、下載快取與推理核心，只是操作入口不同。")
    st.subheader("從模型到回應")
    st.markdown('<div class="flow"><span>model alias</span> → Hugging Face / local cache → <span>MLX runtime</span> → prompt + KV cache → <span>streaming tokens</span> → chat / API / Desktop</div>', unsafe_allow_html=True)
    st.subheader("三種入口，三種工作節奏")
    cols = st.columns(3)
    with cols[0]: card("Chat", "單人、互動、最快開始。啟動 REPL，輸入 `/help` 查看 slash commands，`/exit` 結束。")
    with cols[1]: card("Serve", "把模型變成本機服務。其他程式只需將 base URL 指到 `http://localhost:8000/v1`。")
    with cols[2]: card("Desktop", "macOS 原生 GUI。適合管理模型、檔案、圖片、語音與日常對話；Windows / Linux 目前沒有官方 build。")
    st.markdown('<div class="note">注意：Rapid-MLX 的官方執行環境是 macOS + Apple Silicon。此導覽頁可在其他平台閱讀，但 CLI / Desktop 推理不保證可用。</div>', unsafe_allow_html=True)


def chat_page() -> None:
    header("02 / chat mode", "Chat mode：<br>開一個本地 REPL。", "適合探索模型、測 prompt、快速驗證上下文與思考模式。第一次使用指定模型時會自動下載權重。")
    st.subheader("開始使用")
    code_block("""# 安裝（擇一）
brew install rapid-mlx
# 或
uv tool install rapid-mlx@latest

# 使用預設模型 qwen3.5-4b-4bit
rapid-mlx chat

# 指定模型 alias
rapid-mlx chat qwen3.5-9b-4bit

# 查看 chat 所有選項
rapid-mlx chat --help""")
    st.markdown('<div class="accent"><b>互動操作</b><br>進入 REPL 後輸入 `/help` 查看 slash commands；輸入 `/exit` 離開。Qwen 3.5 / 3.6 預設可能開啟 thinking，可用 `--no-think` 取得更快、較短的回覆。</div>', unsafe_allow_html=True)
    st.subheader("常用 chat 參數")
    st.dataframe([{"語法":"rapid-mlx chat [MODEL]","用途":"以 alias 啟動互動對話；省略時使用預設模型。"},{"語法":"--think / --no-think","用途":"開啟或關閉 thinking / chain-of-thought 路徑。"},{"語法":"--help","用途":"列出目前版本支援的所有 chat flags。"}], use_container_width=True, hide_index=True)
    st.subheader("模型選擇邏輯")
    st.markdown("""
- 先用 `rapid-mlx recipe` 看目前 Mac RAM 的 Smart / Fast 建議。
- 用 `rapid-mlx models` 看完整 alias catalog。
- 用 `rapid-mlx info <alias>` 檢查模型大小、parser、MoE / hybrid 與推理能力。
- 權重通常會留在本機快取；模型過大時，改用較小 quant，別只調低輸出長度。
""")


def serve_page() -> None:
    header("03 / serve mode", "Serve mode：<br>把模型變成本機 API。", "Serve 會在本機啟動 HTTP server，讓 OpenAI SDK、LangChain、Aider、OpenCode 或自己的程式共用同一個模型。")
    st.subheader("啟動 server")
    code_block("""# 預設 port 8000，指定模型
rapid-mlx serve qwen3.5-4b-4bit

# 另一個常用模型
rapid-mlx serve qwen3.5-9b-4bit

# 查看 serve flags
rapid-mlx serve --help""")
    st.metric("OpenAI-compatible endpoint", "http://localhost:8000/v1")
    cols = st.columns(2)
    with cols[0]:
        st.markdown("**curl 測試**")
        code_block("""curl http://localhost:8000/v1/chat/completions \\
  -H "Content-Type: application/json" \\
  -d '{"model":"default","messages":[{"role":"user","content":"Say hello"}]}'""")
    with cols[1]:
        st.markdown("**Python / OpenAI SDK**")
        code_block("""from openai import OpenAI

client = OpenAI(base_url="http://localhost:8000/v1", api_key="not-needed")
answer = client.chat.completions.create(
    model="default",
    messages=[{"role": "user", "content": "Say hello"}],
)
print(answer.choices[0].message.content)""", "python")
    st.subheader("連接方式")
    st.dataframe([{"客戶端":"OpenAI SDK / Aider / LangChain","Base URL":"http://localhost:8000/v1","路由":"/v1/chat/completions"},{"客戶端":"Claude Code / Anthropic SDK","Base URL":"http://localhost:8000","路由":"/v1/messages"},{"客戶端":"Codex CLI","Base URL":"http://localhost:8000/v1","路由":"/v1/responses"}], use_container_width=True, hide_index=True)
    st.markdown('<div class="note">安全提醒：server 預設服務 localhost。若要暴露到網路，必須設定 `RAPID_MLX_API_KEY`，並使用 HTTPS；不要把未驗證的本機服務直接公開。</div>', unsafe_allow_html=True)


def desktop_page() -> None:
    header("04 / desktop mode", "Desktop：<br>把引擎放進日常工作流。", "Rapid-MLX Desktop 是 macOS Apple Silicon 的原生應用，適合不想記 CLI、需要檔案與多媒體操作，或要快速切換模型的人。")
    cols = st.columns(3)
    with cols[0]: card("下載", "從 rapidmlx.com/desktop 或 GitHub signed releases 下載。需要 M-series Mac；目前沒有 Windows / Linux build。")
    with cols[1]: card("模型", "Desktop 使用與 CLI 相同的 model picker / recommendation catalog；依 unified memory 顯示合適選項。")
    with cols[2]: card("能力", "對話、模型管理、vision、檔案、voice 與 image generation 集中在同一個 GUI 工作區。")
    st.subheader("建議操作順序")
    for number, title, body in [("01","檢查硬體","確認 M-series Mac 與 unified memory；RAM 越大可選的 quant / context 越寬。"),("02","選擇模型","在 model picker 先選推薦模型，不確定時選較小的 4-bit alias。"),("03","開始工作","在 Chat、Files、Images 或 Voice 入口操作；模型下載與快取由 Desktop 管理。"),("04","接入工具","需要讓外部程式呼叫時，改用 CLI 的 `serve`；Desktop 比較像個人工作台。")]:
        st.markdown(f"**{number}  {title}**  \n{body}")
    st.markdown('<div class="note">Desktop 與 CLI 的差異：Desktop 強調可視化工作流；`rapid-mlx serve` 才是給其他應用程式接入的 API 邊界。</div>', unsafe_allow_html=True)


def commands_page() -> None:
    header("05 / command map", "Command map：<br>把常用語法收在一頁。", "先記住四個動詞：`chat` 對話、`serve` 服務、`models` 找模型、`doctor` 排障。其餘指令再依工作情境展開。")
    commands = [("chat [MODEL]","啟動 terminal REPL。","rapid-mlx chat qwen3.5-4b-4bit"),("serve [MODEL]","啟動 OpenAI / Anthropic-compatible API。","rapid-mlx serve qwen3.5-4b-4bit"),("models","列出全部 model aliases。","rapid-mlx models"),("recipe","依 Mac RAM 顯示 Smart / Fast 建議。","rapid-mlx recipe --json"),("info <ALIAS>","查看單一模型 profile。","rapid-mlx info qwen3.5-4b-4bit"),("ls / pull / rm","列出、下載、刪除本地模型。","rapid-mlx pull qwen3.5-4b-4bit"),("ps","查看目前運行的 Rapid-MLX processes。","rapid-mlx ps"),("doctor","執行內建環境自我檢查。","rapid-mlx doctor"),("launch <CLIENT>","為支援的 agent / IDE 設定本地 endpoint。","rapid-mlx launch claude-code"),("agents <NAME> --setup","寫入特定 agent 的本地設定。","rapid-mlx agents codex --setup"),("benchmark catalog / plan / run / share","查看、預覽、執行與選擇性分享 benchmark。","rapid-mlx benchmark run qwen3.5-9b-4bit"),("connect","連接到遠端 / reverse-tunnel workflow。","rapid-mlx connect --help"),("alias","管理模型 alias。","rapid-mlx alias --help"),("upgrade","升級 Rapid-MLX。","rapid-mlx upgrade"),("telemetry","查看或調整 telemetry 設定。","rapid-mlx telemetry off"),("feedback","開啟回饋入口。","rapid-mlx feedback --no-open"),("--help","任何層級都可查現行版本語法。","rapid-mlx serve --help")]
    st.dataframe([{"指令":name,"用途":purpose,"範例":example} for name,purpose,example in commands], use_container_width=True, hide_index=True)
    st.subheader("可選模型 runtime")
    code_block("""# Vision / multimodal
pip install 'rapid-mlx[vision]'

# Audio: TTS / STT
pip install 'rapid-mlx[audio]'

# Image generation
pip install 'rapid-mlx[image]'
rapid-mlx serve flux2-klein-4b

# Full optional surface
pip install 'rapid-mlx[all]'""")


def main() -> None:
    with st.sidebar:
        st.markdown("## ⚡ rapid-mlx")
        st.caption("FIELD GUIDE / 2026")
        page_names = ["架構總覽", "Chat 模式", "Serve 模式", "Desktop 操作", "指令速查"]
        page = st.query_params.get("section", "架構總覽")
        if page not in page_names:
            page = "架構總覽"
        st.markdown("**導覽**")
        for page_name in page_names:
            marker = "● " if page_name == page else "○ "
            st.markdown(f"[{marker}{page_name}](?section={quote(page_name)})")
        st.markdown("---")
        st.markdown("**核心定位**")
        st.caption("Local inference for Apple Silicon")
        st.markdown("[官方文件 ↗](https://rapidmlx.com/docs/)  ·  [GitHub ↗](https://github.com/raullenchai/Rapid-MLX)")
    {"架構總覽":architecture_page,"Chat 模式":chat_page,"Serve 模式":serve_page,"Desktop 操作":desktop_page,"指令速查":commands_page}[page]()
    st.markdown('<div class="footer">Rapid-MLX Field Guide · 內容依官方 README 與 CLI 文件整理，實際 flags 請以目前安裝版本的 <code>rapid-mlx --help</code> 為準。<br><br><strong>AI落地服務提供單位</strong><br>美亮資訊顧問有限公司<br>需求洽談：<a href="mailto:mymis168@mymis.tw">mymis168@mymis.tw</a><br>官網：<a href="https://www.mis.com.tw" target="_blank">www.mis.com.tw</a> · <a href="https://www.mymis.tw" target="_blank">www.mymis.tw</a></div>', unsafe_allow_html=True)


if __name__ == "__main__":
    main()


if __name__ == "__main__":
    main()
