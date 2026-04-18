import streamlit as st
from backend import MultilingualChatbot
from datetime import datetime

# ---------------------- PAGE CONFIG ----------------------
st.set_page_config(
    page_title="NEXUS AI",
    page_icon="🧠",
    layout="wide"
)

# ---------------------- CUSTOM CSS ----------------------
st.markdown("""
<style>
.stApp {
    background-color: #0E1117;
    color: white;
}
.title {
    font-size: 40px;
    font-weight: bold;
    color: #00F5FF;
    text-align: center;
}
.user-msg {
    background-color: #1E2A38;
    padding: 12px;
    border-radius: 12px;
    margin: 5px 0;
}
.bot-msg {
    background-color: #111827;
    padding: 12px;
    border-radius: 12px;
    margin: 5px 0;
    border: 1px solid #00F5FF;
}
section[data-testid="stSidebar"] {
    background-color: #020617;
}
.stButton button {
    border-radius: 10px;
    background: linear-gradient(90deg, #00F5FF, #007CF0);
    color: black;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)

# ---------------------- TITLE ----------------------
st.markdown('<div class="title">🚀 NEXUS AI</div>', unsafe_allow_html=True)
st.caption("Next-gen Multilingual Intelligence")

# ---------------------- SESSION ----------------------
if "all_chats" not in st.session_state:
    st.session_state.all_chats = {}

if "current_chat_id" not in st.session_state:
    st.session_state.current_chat_id = datetime.now().strftime("%Y%m%d_%H%M%S")
    st.session_state.all_chats[st.session_state.current_chat_id] = []

# ---------------------- SIDEBAR ----------------------
with st.sidebar:
    st.header("⚙️ Settings")

    language = st.selectbox("🌍 Language", [
        "English", "Spanish", "French", "German",
        "Hindi", "Japanese", "Chinese", "Arabic"
    ])

    if st.button("➕ New Chat"):
        st.session_state.current_chat_id = datetime.now().strftime("%Y%m%d_%H%M%S")
        st.session_state.all_chats[st.session_state.current_chat_id] = []
        st.rerun()

    st.markdown("---")
    st.subheader("💬 Conversations")

    for chat_id in reversed(list(st.session_state.all_chats.keys())):
        chat_messages = st.session_state.all_chats[chat_id]

        if chat_messages:
            preview = chat_messages[0]["content"][:25]
            is_current = chat_id == st.session_state.current_chat_id

            if st.button(
                f"{'🟢' if is_current else '⚪'} {preview}...",
                key=chat_id,
                use_container_width=True
            ):
                st.session_state.current_chat_id = chat_id
                st.rerun()

# ---------------------- CHAT DISPLAY ----------------------
current_messages = st.session_state.all_chats[st.session_state.current_chat_id]

for msg in current_messages:
    if msg["role"] == "user":
        st.markdown(f'<div class="user-msg">🧑‍💻 {msg["content"]}</div>', unsafe_allow_html=True)
        if "image" in msg:
            st.image(msg["image"])
    else:
        st.markdown(f'<div class="bot-msg">🤖 {msg["content"]}</div>', unsafe_allow_html=True)

# ---------------------- INPUT WITH IMAGE SUPPORT ----------------------
prompt_data = st.chat_input(
    "Ask NEXUS anything or upload an image...",
    accept_file=True,
    file_type=["jpg", "jpeg", "png"]
)

if prompt_data:

    # Correct extraction
    user_text = prompt_data.text
    uploaded_files = prompt_data.files

    # Save user message
    message = {"role": "user", "content": user_text}

    if uploaded_files:
        message["image"] = uploaded_files[0]

    current_messages.append(message)

    # Show user
    st.markdown(f'<div class="user-msg">🧑‍💻 {user_text}</div>', unsafe_allow_html=True)
    if uploaded_files:
        st.image(uploaded_files[0])

    # Bot response
    chatbot = MultilingualChatbot()
    response = chatbot.chat(user_text, language, current_messages)

    # Save bot message
    current_messages.append({"role": "assistant", "content": response})

    st.markdown(f'<div class="bot-msg">🤖 {response}</div>', unsafe_allow_html=True)

    st.session_state.all_chats[st.session_state.current_chat_id] = current_messages

    st.rerun()