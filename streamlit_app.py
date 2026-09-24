import streamlit as st


st.set_page_config(
    page_title="美亮資訊｜落地模型方案",
    page_icon="◒",
    layout="wide",
    initial_sidebar_state="collapsed",
)

web_nav = st.navigation([     
    st.Page("main.py", title= "Home"),
    st.Page("apple_mlx.py",title="Apple MLX模型"),
    st.Page("llamacpp_intro.py",title= "LlamaCpp介紹"),
    st.Page("hface.py",title= "HuggingFace Cli介紹"),
    st.Page("hf_gguf.py",title= "GGUF模型介邵")     
    ],
    position = "top"
)

web_nav.run()

