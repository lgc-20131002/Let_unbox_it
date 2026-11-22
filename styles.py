import streamlit as st


def apply_styles():
    # 注意这里的 CSS：只要有 st-key-red，不管后面带什么数字，都会变红
    st.markdown("""
    <style>
    [class*="st-key-red"] button { background-color: #ff4b4b !important; color: white !important; }
    [class*="st-key-orange"] button { background-color: #ff8c00 !important; color: white !important; }
    [class*="st-key-yellow"] button { background-color: #ffd700 !important; color: black !important; }
    [class*="st-key-green"] button { background-color: #21c354 !important; color: white !important; }
    [class*="st-key-cyan"] button { background-color: #00ced1 !important; color: black !important; }
    [class*="st-key-blue"] button { background-color: #1E90FF !important; color: white !important; }
    [class*="st-key-purple"] button { background-color: #9b59b6 !important; color: white !important; }
    </style>
    """, unsafe_allow_html=True)


# 👇 这是你的专属按钮函数，自动帮你搞定冲突！
_button_counts = {}


def color_btn(text, color):
    # 每次调用按钮，自动给当前颜色加个计数（比如 green_1, green_2）
    if color not in _button_counts:
        _button_counts[color] = 0
    _button_counts[color] += 1

    # 自动生成不会冲突的 key
    unique_key = f"{color}_{_button_counts[color]}"

    # 返回原生按钮
    return st.button(text, key=unique_key)