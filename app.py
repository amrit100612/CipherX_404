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
    layout="wide",
)

st.markdown(
    """
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

        :root {
            --bg: #060d16;
            --bg-2: #0c1824;
            --panel: rgba(15, 23, 32, 0.96);
            --panel-2: rgba(10, 17, 26, 0.9);
            --line: rgba(148, 163, 184, 0.18);
            --text: #edf6ff;
            --muted: #9bb0c7;
            --primary: #77d8ff;
            --accent: #7b6cff;
            --glow: rgba(119, 216, 255, 0.38);
            --success: #68e0a7;
            --warning: #ffd166;
        }

        html, body, [data-testid="stAppViewContainer"] {
            background:
                radial-gradient(circle at top left, rgba(123, 108, 255, 0.25), transparent 30%),
                radial-gradient(circle at top right, rgba(119, 216, 255, 0.18), transparent 28%),
                linear-gradient(180deg, var(--bg) 0%, var(--bg-2) 100%);
            color: var(--text);
            font-family: 'Inter', sans-serif;
        }

        .block-container {
            max-width: 1280px;
            padding-top: 2.2rem;
            padding-bottom: 3rem;
        }

        .topbar {
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 1rem;
            margin-bottom: 1.2rem;
            padding: 0.35rem 0.2rem 0.7rem 0.2rem;
        }

        .brand-wrap {
            display: inline-flex;
            align-items: center;
            gap: 0.8rem;
            font-weight: 800;
            letter-spacing: -0.08em;
            font-size: 1.8rem;
            color: var(--text);
        }

        .brand-dot {
            width: 12px;
            height: 12px;
            border-radius: 50%;
            background: linear-gradient(135deg, var(--primary), var(--accent));
            box-shadow: 0 0 18px rgba(119, 216, 255, 0.8);
        }

        .chip {
            border: 1px solid rgba(119, 216, 255, 0.2);
            background: rgba(119, 216, 255, 0.06);
            color: var(--primary);
            border-radius: 999px;
            padding: 0.5rem 0.85rem;
            font-size: 0.7rem;
            letter-spacing: 0.12em;
            text-transform: uppercase;
            font-weight: 700;
        }

        .hero-shell {
            display: grid;
            grid-template-columns: 1.5fr 0.9fr;
            gap: 1.2rem;
            align-items: stretch;
            margin-bottom: 1.5rem;
        }

        .hero-copy,
        .hero-panel,
        .feature-card,
        .tool-panel {
            background: rgba(15, 23, 32, 0.95);
            border: 1px solid var(--line);
            border-radius: 24px;
            box-shadow: 0 28px 60px rgba(0,0,0,0.2);
        }

        .hero-copy {
            padding: 2rem 2rem 1.6rem 2rem;
        }

        .hero-panel {
            padding: 1.4rem;
            display: flex;
            flex-direction: column;
            justify-content: center;
        }

        .eyebrow {
            display: inline-flex;
            align-items: center;
            gap: 0.6rem;
            color: var(--primary);
            letter-spacing: 0.11em;
            text-transform: uppercase;
            font-size: 0.72rem;
            font-weight: 700;
        }

        .eyebrow::before {
            content: "";
            display: block;
            width: 8px;
            height: 8px;
            border-radius: 50%;
            background: var(--primary);
            box-shadow: 0 0 10px rgba(119, 216, 255, 0.8);
        }

        .hero-title {
            margin: 1rem 0 0.8rem 0;
            font-size: clamp(2.6rem, 5vw, 4.5rem);
            letter-spacing: -0.08em;
            line-height: 0.96;
            font-weight: 800;
            color: var(--text);
        }

        .hero-title .accent {
            color: var(--primary);
            text-shadow: 0 0 18px rgba(119, 216, 255, 0.4);
        }

        .hero-subtitle {
            color: var(--muted);
            font-size: 1.02rem;
            line-height: 1.75;
            margin: 0;
            max-width: 680px;
        }

        .cta-row {
            display: flex;
            flex-wrap: wrap;
            gap: 0.8rem;
            margin-top: 1.5rem;
        }

        .stat-grid {
            display: grid;
            grid-template-columns: repeat(3, minmax(0, 1fr));
            gap: 0.7rem;
            margin-top: 1.5rem;
        }

        .stat {
            background: rgba(10, 17, 26, 0.9);
            border: 1px solid var(--line);
            border-radius: 14px;
            padding: 0.9rem 0.8rem;
        }

        .stat strong {
            display: block;
            font-size: 1.15rem;
            color: var(--text);
            margin-bottom: 0.2rem;
        }

        .stat span {
            color: var(--muted);
            font-size: 0.76rem;
            letter-spacing: 0.04em;
            text-transform: uppercase;
        }

        .feature-list {
            list-style: none;
            margin: 0;
            padding: 0;
            display: grid;
            gap: 0.75rem;
        }

        .feature-list li {
            display: flex;
            align-items: center;
            gap: 0.8rem;
            padding: 0.7rem 0.8rem;
            border-radius: 12px;
            background: rgba(255,255,255,0.02);
            border: 1px solid rgba(148, 163, 184, 0.12);
            color: var(--text);
        }

        .feature-list .bullet {
            width: 10px;
            height: 10px;
            border-radius: 50%;
            background: linear-gradient(135deg, var(--primary), var(--accent));
            box-shadow: 0 0 12px rgba(119,216,255,0.8);
            flex-shrink: 0;
        }

        .feature-grid {
            display: grid;
            grid-template-columns: repeat(3, minmax(0, 1fr));
            gap: 1rem;
            margin-top: 1.2rem;
        }

        .feature-card {
            padding: 1.2rem;
        }

        .feature-card .icon {
            width: 42px;
            height: 42px;
            border-radius: 12px;
            background: linear-gradient(135deg, rgba(119,216,255,0.16), rgba(123,108,255,0.18));
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 1.2rem;
            margin-bottom: 0.8rem;
        }

        .feature-card h3 {
            margin: 0 0 0.45rem 0;
            font-size: 1.08rem;
            color: var(--text);
        }

        .feature-card p {
            margin: 0;
            line-height: 1.7;
            color: var(--muted);
        }

        .tool-panel {
            padding: 1.2rem;
            margin-top: 1.2rem;
        }

        .tool-grid {
            display: grid;
            grid-template-columns: 1.4fr 0.9fr;
            gap: 1rem;
            align-items: start;
        }

        .panel-title {
            margin: 0 0 1rem 0;
            font-size: 1.2rem;
            font-weight: 700;
            letter-spacing: -0.04em;
        }

        .stRadio > div {
            background: rgba(255, 255, 255, 0.02);
            border: 1px solid var(--line);
            border-radius: 14px;
            padding: 0.45rem 0.5rem;
        }

        .stRadio label {
            color: var(--text) !important;
            font-weight: 600;
        }

        .stTextInput > div > div > input,
        .stSlider > div > div > div {
            background: rgba(9,16,23,0.92);
            color: var(--text);
            border: 1px solid var(--line);
            border-radius: 12px;
            min-height: 52px;
            padding-left: 1rem;
        }

        .stTextInput label, .stSlider label {
            color: var(--muted) !important;
            font-weight: 600 !important;
            margin-bottom: 0.7rem !important;
        }

        .stButton > button {
            background: linear-gradient(135deg, var(--primary), var(--accent));
            color: #08131d;
            border: none;
            border-radius: 12px;
            min-height: 52px;
            width: 100%;
            font-weight: 800;
            letter-spacing: 0.04em;
            box-shadow: 0 12px 30px rgba(119, 216, 255, 0.22);
        }

        .stButton > button:hover {
            box-shadow: 0 14px 32px rgba(119, 216, 255, 0.28);
            filter: brightness(1.03);
        }

        .stAlert {
            border-radius: 12px;
            border: 1px solid rgba(105, 224, 164, 0.16);
            background: rgba(105, 224, 164, 0.08);
            color: #dffef0;
        }

        .stSuccess {
            border-radius: 12px;
            border: 1px solid rgba(119, 216, 255, 0.2);
            background: rgba(119, 216, 255, 0.07);
            color: #edfaff;
        }

        code {
            background: rgba(9, 15, 22, 0.96);
            color: var(--primary);
            border: 1px solid var(--line);
            border-radius: 12px;
            padding: 0.85rem 1rem;
            font-size: 0.92rem;
            line-height: 1.7;
            letter-spacing: 0.02em;
        }

        .muted {
            color: var(--muted);
        }

        @media (max-width: 980px) {
            .hero-shell, .tool-grid, .feature-grid {
                grid-template-columns: 1fr;
            }
        }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="topbar">
        <div class="brand-wrap"><span class="brand-dot"></span> CipherX</div>
        <div class="chip">Secure utility</div>
    </div>
    <div class="hero-shell">
        <div class="hero-copy">
            <div class="eyebrow">Password security</div>
            <h1 class="hero-title"><span class="accent">Cipher</span>X</h1>
            <p class="hero-subtitle">Transform your credentials using a robust Caesar-shift workflow designed for secure, readable, and fast password encryption and decryption.</p>
            <div class="cta-row">
                <div class="chip">🚀 Fast</div>
                <div class="chip">🔒 Secure</div>
                <div class="chip">⚡ Simple</div>
            </div>
            <div class="stat-grid">
                <div class="stat"><strong>26</strong><span>Alphabet shifts</span></div>
                <div class="stat"><strong>3</strong><span>Default offset</span></div>
                <div class="stat"><strong>100%</strong><span>Browser-safe</span></div>
            </div>
        </div>
        <div class="hero-panel">
            <ul class="feature-list">
                <li><span class="bullet"></span> Encrypt sensitive text instantly</li>
                <li><span class="bullet"></span> Decrypt using the same shift key</li>
                <li><span class="bullet"></span> Works with letters while preserving symbols</li>
            </ul>
        </div>
    </div>
    <div class="feature-grid">
        <div class="feature-card">
            <div class="icon">🔐</div>
            <h3>Secure workflow</h3>
            <p>Protect your password with a clear and dependable transformation model.</p>
        </div>
        <div class="feature-card">
            <div class="icon">⚙️</div>
            <h3>Flexible control</h3>
            <p>Adjust the shift value to match your encryption preference or decrypt workflow.</p>
        </div>
        <div class="feature-card">
            <div class="icon">✨</div>
            <h3>Clean output</h3>
            <p>Readable result formatting helps you copy and reuse the transformed text safely.</p>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown('<div class="tool-panel">', unsafe_allow_html=True)
col_left, col_right = st.columns([1.25, 0.9])

with col_left:
    st.markdown('<h3 class="panel-title">Conversion tool</h3>', unsafe_allow_html=True)
    with st.form(key="cipher_form"):
        mode = st.radio("Mode", ["Encrypt", "Decrypt"], horizontal=True)
        password = st.text_input("Password", type="password", placeholder="Enter your password")
        shift = st.slider("Shift value", 1, 25, 3)
        submitted = st.form_submit_button("Encrypt Password" if mode == "Encrypt" else "Decrypt Password", use_container_width=True)

    if submitted:
        if not password.strip():
            st.warning("Please enter a password first.")
        else:
            if mode == "Encrypt":
                result = encrypt_password(password, shift)
                action_text = "Encrypted password"
            else:
                result = decrypt_password(password, shift)
                action_text = "Decrypted password"

            st.success(action_text)
            st.code(result)

with col_right:
    st.markdown('<h3 class="panel-title">How it works</h3>', unsafe_allow_html=True)
    st.markdown(
        """
        <div class="muted">
            1. Enter a password<br>
            2. Select Encrypt or Decrypt<br>
            3. Choose your shift value<br>
            4. Read the transformed output
        </div>
        """,
        unsafe_allow_html=True,
    )

st.markdown('</div>', unsafe_allow_html=True)

st.markdown("---")
st.caption("Use the same shift value for decryption to reverse the transformation.")
