import streamlit as st


def caesar_shift(text: str, shift: int) -> str:
    result = []
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            shifted = (ord(char) - base + shift) % 26
            result.append(chr(base + shifted))
        else:
            result.append(char)
    return "".join(result)


def encrypt_password(password: str, shift: int = 3) -> str:
    return caesar_shift(password, shift)


def decrypt_password(password: str, shift: int = 3) -> str:
    return caesar_shift(password, -shift)


st.set_page_config(
    page_title="CipherX",
    page_icon="🔐",
    layout="centered",
)

st.markdown(
    """
    <style>
        @import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;500;700;800&display=swap');
        html, body, [data-testid="stAppViewContainer"] {
            background: radial-gradient(circle at top, #1d1030, #09070e 50%);
            color: #f4ebff;
            font-family: 'JetBrains Mono', monospace;
        }
        .block-container {
            padding-top: 2rem;
            padding-bottom: 2rem;
        }
        div[data-testid="stSidebar"] {
            background: rgba(18, 10, 31, 0.9);
        }
        h1, h2, h3 {
            color: #ff4ecb;
        }
        .stTextInput > div > div > input,
        .stSlider > div > div > div {
            background: #120b1d;
            color: #f4ebff;
            border: 1px solid #33224a;
        }
        .stButton > button {
            background: linear-gradient(90deg, #ff2ec4, #7a1c66, #37e6ff);
            color: #0a0410;
            font-weight: 700;
            border: none;
            border-radius: 8px;
        }
        .stAlert {
            background: rgba(55,230,255,0.08);
            border: 1px solid rgba(55,230,255,0.3);
            color: #ddfaff;
        }
        code {
            background: #0d0716;
            color: #37e6ff;
            padding: 0.4rem 0.6rem;
            border-radius: 6px;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

st.title("CipherX 🔐")
st.caption("Encrypt and decrypt passwords using the Caesar-shift method.")

with st.container():
    mode = st.radio("Choose a mode", ["Encrypt", "Decrypt"], horizontal=True)
    password = st.text_input("Password", type="password", placeholder="Enter a secret password")
    shift = st.slider("Shift value", 1, 25, 3)

    if password:
        if mode == "Encrypt":
            result = encrypt_password(password, shift)
            action_text = "Encrypted password"
        else:
            result = decrypt_password(password, shift)
            action_text = "Decrypted password"

        st.success(action_text)
        st.code(result)
    else:
        st.info("Type a password to begin.")

st.markdown("---")
st.caption("Tip: use the same shift value when decrypting to reverse the encryption.")
