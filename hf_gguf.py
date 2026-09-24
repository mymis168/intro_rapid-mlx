import streamlit as st


st.set_page_config(
    page_title="GGUF 模型格式指南",
    page_icon="G",
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
h1 { font-size:clamp(2.8rem,6vw,6.5rem); line-height:.95; font-weight:800; margin:.4rem 0 1.2rem; }
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
.hero-copy { color:var(--muted); font-size:1.1rem; max-width:760px; line-height:1.85; }
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
    '<div class="topbar"><div class="brand">GGUF <em>／</em> 模型格式指南</div><div style="display:flex;align-items:center;gap:1rem;flex-wrap:wrap"><div class="topmeta">MODEL FORMAT · QUANTIZATION · LOCAL INFERENCE</div></div></div>',
    unsafe_allow_html=True,
)

st.markdown(
    """
<div class="hero">
  <div class="eyebrow">GGUF / A Portable Inference Container</div>
  <h1>理解 GGUF，<br>把模型帶回本地。</h1>
  <div class="hero-copy">GGUF 是大型語言模型常用的單檔／分片模型格式，將權重、張量型別、模型超參數與 tokenizer metadata 放在同一套可攜式容器中，方便 llama.cpp、LM Studio、Ollama 與其他本地推理工具載入。</div>
  <div class="hero-kicker">WEIGHTS · METADATA · TOKENIZER · QUANTIZATION</div>
</div>
""",
    unsafe_allow_html=True,
)

st.markdown('<div class="section-label">01 / 基本知識</div>', unsafe_allow_html=True)
st.header("GGUF 是什麼？")
st.markdown(
    """
GGUF（GPT-Generated Unified Format）是為本地推理設計的二進位容器格式。它不是一個模型架構，也不是新的訓練方法；它更像是「把已訓練模型整理成推理引擎容易讀取的封裝」。

常見優點包括：

- **可攜性**：模型權重與必要 metadata 集中在 `.gguf` 檔案中。
- **快速載入**：推理引擎可以 memory-map 檔案，減少不必要的轉換與複製。
- **量化支援**：同一模型可輸出 Q4、Q5、Q8 或 F16 等不同精度版本，調整記憶體與速度。
- **本地生態成熟**：常見於 llama.cpp、LM Studio、KoboldCpp、Open WebUI、Ollama 等工具。
"""
)

cols = st.columns(3)
for col, (num, title, body) in zip(
    cols,
    [
        ("01 / CONTAINER", "一個可讀取的容器", "檔案包含 header、metadata、tensor directory 與 tensor data，不只是單純把 PyTorch 權重改副檔名。"),
        ("02 / INFERENCE", "為推理而生", "GGUF 通常由推理引擎直接載入；訓練與微調通常仍在 Transformers／Safetensors 工作流進行。"),
        ("03 / PORTABLE", "適合本地部署", "把模型帶到開發機、工作站或企業內網，搭配 CPU、CUDA、Metal 或其他 backend 執行。"),
    ],
):
    with col:
        st.markdown(f'<div class="panel"><div class="num">{num}</div><h3>{title}</h3><p>{body}</p></div>', unsafe_allow_html=True)

st.markdown('<div class="section-label">02 / 檔案架構</div>', unsafe_allow_html=True)
st.header("一個 GGUF 檔案裡面有什麼？")
st.code(
    """GGUF file
+-------------------------------+
| Magic + version               |  Header: 格式識別與版本
| tensor_count + metadata_count |
+-------------------------------+
| Metadata KV                    |  架構、context、tokenizer、quantization
+-------------------------------+
| Tensor directory               |  名稱、shape、dtype、offset
+-------------------------------+
| Tensor data                    |  權重資料與對齊後的 binary payload
+-------------------------------+""",
    language="text",
)
st.markdown(
    """
**Metadata** 會描述模型架構、layer 數量、hidden size、context length、RoPE 設定、tokenizer vocab、special tokens、chat template 與量化資訊。**Tensor data** 則是實際的 embedding、attention、MLP／FFN、normalization 等權重。

檔案內的資料不是一個固定的「所有模型都一樣」布局。不同模型架構的 tensor 名稱與 metadata 會不同，推理引擎必須支援該 architecture，才能正確解讀。
"""
)

st.markdown('<div class="section-label">03 / 模型組成與量化</div>', unsafe_allow_html=True)
st.header("從 Transformer 權重，到可使用的 GGUF")
cols = st.columns(4)
for col, (label, title, body) in zip(
    cols,
    [
        ("A", "Embedding", "把 token id 轉成向量，通常包含 token embedding 與輸出 head。"),
        ("B", "Attention", "以 Q、K、V 與 output projection 處理上下文關係，常搭配 RoPE。"),
        ("C", "MLP / FFN", "每層的非線性轉換與專家路由；MoE 模型還會包含多組 experts。"),
        ("D", "Norm + Output", "Normalization、最後的語言模型 head 與 tokenizer metadata 共同完成生成。"),
    ],
):
    with col:
        st.markdown(f'<div class="panel"><div class="num">{label} / TENSOR GROUP</div><h3>{title}</h3><p>{body}</p></div>', unsafe_allow_html=True)

st.subheader("常見量化名稱怎麼看？")
st.dataframe(
    [
        {"格式": "F16 / BF16", "特性": "高精度、檔案大、記憶體需求高；接近原始浮點推理。"},
        {"格式": "Q8_0", "特性": "較高品質的 8-bit 量化；檔案與記憶體約低於 F16。"},
        {"格式": "Q6_K / Q5_K_M", "特性": "品質與大小的折衷，適合希望保留較多能力的本地部署。"},
        {"格式": "Q4_K_M / Q4_0", "特性": "常見的 4-bit 路徑，檔案小、速度快，但品質依模型與任務而變。"},
    ],
    use_container_width=True,
    hide_index=True,
)
st.markdown('<div class="warning">量化不是「越小越好」。要一起評估模型能力、context 長度、同時使用人數、Metal／CUDA backend 與實際任務品質；正式採用前應用企業資料做一組固定評測。</div>', unsafe_allow_html=True)

st.markdown('<div class="section-label">04 / 從 Hugging Face 下載</div>', unsafe_allow_html=True)
st.header("下載 GGUF 模型的兩種方式")
st.subheader("方式 A：使用 Hugging Face CLI")
st.code(
    """# 安裝與登入
python -m pip install -U huggingface_hub
hf auth login

# 下載整個 GGUF repository 到指定資料夾
hf download TheBloke/Mistral-7B-Instruct-v0.2-GGUF \\
  --local-dir ./models/mistral-7b-gguf

# 只下載指定量化檔案與說明
hf download <ORG>/<GGUF-REPO> \\
  <MODEL>.Q4_K_M.gguf README.md \\
  --local-dir ./models/<MODEL>""",
    language="bash",
)
st.subheader("方式 B：使用 Python API")
st.code(
    """from huggingface_hub import hf_hub_download

path = hf_hub_download(
    repo_id="<ORG>/<GGUF-REPO>",
    filename="<MODEL>.Q4_K_M.gguf",
    local_dir="./models/<MODEL>",
)
print(path)""",
    language="python",
)
st.markdown('<div class="note">下載前確認 license、模型卡、量化版本、context 限制與是否需要允許條款。私有或 gated repository 需要先以 <code>hf auth login</code> 完成授權。</div>', unsafe_allow_html=True)

st.markdown('<div class="section-label">05 / 變成可使用的模型</div>', unsafe_allow_html=True)
st.header("轉換、分片與合併：三個情境要分清楚")
st.markdown(
    """
「合併」在 GGUF 工作流裡有三種不同意思，不能把所有 `.gguf` 檔案直接用文字或 `cat` 串接：

1. **下載分片 GGUF**：同一模型因為檔案太大被拆成 `model-00001-of-00003.gguf` 等多個檔案。它們是同一組模型的 shards，保持同一資料夾並交給支援分片的 loader；不是手動合成一個 binary。
2. **LoRA 合併**：LoRA adapter 與 base model 是不同資產，通常先在 Transformers／PEFT 工作流合併成 full model，再轉成 GGUF。
3. **HF Safetensors 轉 GGUF**：原始模型權重先用 llama.cpp 的 converter 轉成 F16 GGUF，再用 quantize 工具產生 Q4／Q5／Q8 GGUF。
"""
)
st.subheader("A. HF Safetensors → F16 GGUF → 量化 GGUF")
st.code(
    """# llama.cpp 工具與 converter 依版本可能位於 repo 的 tools 目錄
# 先把 Hugging Face 模型下載到本地
hf download <ORG>/<MODEL> --local-dir ./models/<MODEL>

# 轉成可攜式 F16 GGUF
python convert_hf_to_gguf.py ./models/<MODEL> \\
  --outfile ./models/<MODEL>.f16.gguf \\
  --outtype f16

# 量化成較小的 4-bit 模型
./llama-quantize ./models/<MODEL>.f16.gguf \\
  ./models/<MODEL>.Q4_K_M.gguf Q4_K_M

# 測試模型（llama.cpp 範例）
./llama-cli -m ./models/<MODEL>.Q4_K_M.gguf \\
  -p "請用一句話介紹自己""",
    language="bash",
)
st.subheader("B. LoRA adapter 先合併，再轉 GGUF")
st.code(
    """# 概念流程，不是把 adapter.gguf 直接附加到 base.gguf
# 1. 以 PEFT / Transformers 載入 base + LoRA
# 2. model = model.merge_and_unload()
# 3. save_pretrained() 輸出完整 merged HF model
# 4. 用 convert_hf_to_gguf.py 轉成 F16 GGUF
# 5. 用 llama-quantize 產生目標量化版本

# 也可保留 adapter，交給支援 LoRA runtime 的工具於載入時套用""",
    language="bash",
)
st.markdown('<div class="warning">最重要的原則：同一組 GGUF 分片要完整保留，LoRA 不能用檔案拼接方式合併，HF 模型也不能只改副檔名變成 GGUF。轉換工具版本與模型架構必須相容。</div>', unsafe_allow_html=True)

st.markdown('<div class="section-label">06 / 載入方式</div>', unsafe_allow_html=True)
st.header("常見本地推理工具")
st.code(
    """# llama.cpp
./llama-cli -m ./models/model.Q4_K_M.gguf -p "Hello"

# llama-server：提供 OpenAI-compatible API
./llama-server -m ./models/model.Q4_K_M.gguf --port 8080

# Ollama：建立 Modelfile 後建立本地模型
ollama create my-model -f Modelfile
ollama run my-model

# 確認模型檔案資訊（llama.cpp 工具）
./llama-info ./models/model.Q4_K_M.gguf""",
    language="bash",
)
st.markdown('<div class="note">Rapid-MLX 主要使用自己的模型 alias 與 MLX runtime。GGUF 是另一條常見的本地推理格式；若要在 Rapid-MLX 使用特定模型，請先確認該版本是否支援該模型架構與格式，不要假設所有 GGUF 都能直接載入。</div>', unsafe_allow_html=True)

st.markdown('<div class="section-label">07 / 檢查清單</div>', unsafe_allow_html=True)
st.header("正式部署前，請確認這些事")
st.dataframe(
    [
        {"項目": "模型身份", "確認內容": "來源、revision、license、base model 與 chat template。"},
        {"項目": "量化選擇", "確認內容": "F16／Q8／Q6／Q5／Q4 的品質、檔案大小與硬體記憶體。"},
        {"項目": "檔案完整性", "確認內容": "分片數量齊全、檔案 checksum、下載沒有中斷或部分檔案。"},
        {"項目": "推理相容性", "確認內容": "推理工具版本、模型 architecture、context、tokenizer 與 special tokens。"},
        {"項目": "企業驗證", "確認內容": "用實際領域問題評估準確率、延遲、吞吐、資料權限與日誌策略。"},
    ],
    use_container_width=True,
    hide_index=True,
)

st.markdown('<div class="footer">GGUF 模型格式指南 · 內容涵蓋格式、量化、Hugging Face 下載與本地推理工作流；實際轉換參數請以所使用的 llama.cpp、模型卡與推理工具版本為準。<br><br><strong>AI落地服務提供單位</strong><br>美亮資訊顧問有限公司<br>需求洽談：<a href="mailto:mymis168@mymis.tw">mymis168@mymis.tw</a><br>官網：<a href="https://www.mis.com.tw" target="_blank">www.mis.com.tw</a> · <a href="https://www.mymis.tw" target="_blank">www.mymis.tw</a></div>', unsafe_allow_html=True)
