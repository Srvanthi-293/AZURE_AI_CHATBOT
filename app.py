#!/usr/bin/env python
# coding: utf-8

import streamlit as st
from openai import AzureOpenAI


AZURE_ENDPOINT    = "Add_Your_End_Point"
AZURE_API_KEY     = "Add_Your_API_Key"
AZURE_DEPLOYMENT  = "gpt-4.1-2"
AZURE_API_VERSION = "2024-12-01-preview"

client = AzureOpenAI(
    api_key=AZURE_API_KEY,
    azure_endpoint=AZURE_ENDPOINT,
    api_version=AZURE_API_VERSION,
)

st.set_page_config(page_title="Chat with Mini", page_icon="🤖", layout="wide")

# -----------------------------
#  Tiny styles
# -----------------------------
st.markdown("""
<style>
/* Make chat a bit comfier */
.block-container { padding-top: 1.2rem; }
.chat-header { font-weight: 700; font-size: 1.2rem; margin-bottom: .25rem; }
.sidebar-robot { display: grid; place-items: center; }
.sidebar-robot svg { width: 120px; height: 120px; }
.hint { color: #94a3b8; font-size: 0.9rem; }
</style>
""", unsafe_allow_html=True)

# -----------------------------
#  Mini Robot SVG
# -----------------------------
ROBOT_MINI = """
<svg viewBox="0 0 200 200" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Mini robot">
  <ellipse cx="100" cy="170" rx="42" ry="10" fill="black" opacity="0.18"/>
  <rect x="65" y="25" width="70" height="38" rx="10" fill="#0f172a" stroke="#a78bfa" stroke-width="2"/>
  <circle cx="85" cy="44" r="6" fill="#7dd3fc"/>
  <circle cx="115" cy="44" r="6" fill="#7dd3fc"/>
  <path d="M85 52 Q100 60 115 52" stroke="#7dd3fc" stroke-width="2" fill="none" stroke-linecap="round"/>
  <line x1="100" y1="18" x2="100" y2="25" stroke="#7dd3fc" stroke-width="3" stroke-linecap="round"/>
  <circle cx="100" cy="14" r="4" fill="#7dd3fc"/>
  <rect x="50" y="70" width="100" height="70" rx="18" fill="#0b1320" stroke="#7dd3fc" stroke-width="2" opacity="0.95"/>
  <rect x="40" y="80" width="12" height="36" rx="6" fill="#0b1320" stroke="#a78bfa" stroke-width="2"/>
  <rect x="148" y="80" width="12" height="36" rx="6" fill="#0b1320" stroke="#a78bfa" stroke-width="2"/>
  <rect x="70" y="140" width="18" height="16" rx="5" fill="#0b1320" stroke="#7dd3fc" />
  <rect x="112" y="140" width="18" height="16" rx="5" fill="#0b1320" stroke="#7dd3fc" />
</svg>
"""

# -----------------------------
#Azure call
# -----------------------------
def ask_azure(question: str) -> str:
    try:
        resp = client.chat.completions.create(
            model=AZURE_DEPLOYMENT,
            messages=[
                {"role": "system", "content": "You are Mini, a friendly, concise helper."},
                {"role": "user", "content": question},
            ],
            temperature=0.6,
            max_tokens=700,
        )
        return (resp.choices[0].message.content or "").strip()
    except Exception as e:
        return f"⚠️ Error talking to Azure OpenAI: {e}"

# -----------------------------
# Chat state
# -----------------------------
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hi! I’m Mini 🤖 — ask me anything."}
    ]

# -----------------------------
#  MAIN: Chat area
# -----------------------------
st.markdown("<div class='chat-header'>Chat</div>", unsafe_allow_html=True)

for m in st.session_state.messages:
    with st.chat_message(m["role"]):
        st.write(m["content"])

user_text = st.chat_input("Type your message...")
if user_text:
    st.session_state.messages.append({"role": "user", "content": user_text})
    with st.chat_message("user"):
        st.write(user_text)

    with st.chat_message("assistant"):
        with st.spinner("Mini is thinking..."):
            reply = ask_azure(user_text)
        st.write(reply)
    st.session_state.messages.append({"role": "assistant", "content": reply})

# -----------------------------
# SIDEBAR: Title + mini robot + controls
# -----------------------------
with st.sidebar:
    st.title("Chat with Mini")
    st.markdown(f"<div class='sidebar-robot'>{ROBOT_MINI}</div>", unsafe_allow_html=True)
    st.markdown("Mini is a tiny robot pal who answers quickly and keeps things simple.")
    if st.button("Reset conversation"):
        st.session_state.messages = [
            {"role": "assistant", "content": "Chat reset! I’m Mini — how can I help?"}
        ]
        st.rerun()
    st.markdown("<div class='hint'>Tip: Use the sidebar button to clear the chat.</div>", unsafe_allow_html=True)
