import streamlit as st
from google import genai
from dotenv import load_dotenv
import os
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from io import BytesIO
from gtts import gTTS
import tempfile
import time

# ==========================================
# PAGE CONFIG
# ==========================================

st.set_page_config(
    page_title="GemSphere AI",
    page_icon="🤖",
    layout="wide"
)

# ==========================================
# LOAD ENV
# ==========================================

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    st.error("Please add GEMINI_API_KEY in .env file")
    st.stop()

# ==========================================
# GEMINI CLIENT
# ==========================================

client = genai.Client(api_key=API_KEY)

# ==========================================
# CUSTOM CSS
# ==========================================
st.markdown("""
<style>

.stApp{
    background:#0e1117;
}

.main-title{
    text-align:center;
    font-size:50px;
    font-weight:bold;
    color:white;
}

[data-testid="stChatMessage"]{
    background:#161b22;
    border:1px solid #30363d;
    border-radius:18px;
    padding:15px;
    margin-bottom:12px;
}

[data-testid="stChatMessageContent"]{
    color:white !important;
    font-size:16px;
}

</style>
""", unsafe_allow_html=True)

# ==========================================
# SESSION STATE
# ==========================================

if "messages" not in st.session_state:
    st.session_state.messages = []
def create_pdf(chat_history):

    buffer = BytesIO()

    doc = SimpleDocTemplate(buffer)

    styles = getSampleStyleSheet()

    content = []

    for msg in chat_history:

        content.append(
            Paragraph(
                f"<b>{msg['role']}</b>: {msg['content']}",
                styles["BodyText"]
            )
        )

        content.append(Spacer(1, 6))

    doc.build(content)

    buffer.seek(0)

    return buffer
# ==========================================
# SIDEBAR
# ==========================================
with st.sidebar:

    st.title("⚙️ GemSphere Control Center")

    agent = st.selectbox(
        "Choose Agent",
        [
            "General AI",
            "Study Agent",
            "Coding Agent",
            "Business Agent",
            "Research Agent"
        ]
    )

    language = st.selectbox(
        "Response Language",
        [
            "Auto Detect",
            "English",
            "Hindi",
            "Kannada",
            "Tamil",
            "Telugu"
        ]
    )

    if st.button("🗑 Clear Chat"):
        st.session_state.messages = []
        st.rerun()

    st.divider()

    st.metric("Messages", len(st.session_state.messages))
    st.metric("Current Agent", agent)

    pdf_file = create_pdf(st.session_state.messages)

    st.download_button(
        "📄 Export Chat PDF",
        pdf_file,
        file_name="GemSphere_Chat.pdf",
        mime="application/pdf"
    )

    if st.session_state.messages:

        report = ""

        for msg in st.session_state.messages:
            report += f"{msg['role'].upper()}\n{'-'*20}\n{msg['content']}\n\n"

        st.download_button(
            "📥 Download Report",
            report,
            file_name="GemSphere_Report.txt"
        )

# ==========================================
# AGENTS
# ==========================================

AGENTS = {

    "General AI":
    "You are a helpful AI assistant.",

    "Study Agent":
    """
    You are an expert teacher.
    Explain concepts clearly.
    Give examples.
    """,

    "Coding Agent":
    """
    You are a senior software engineer.
    Write clean code.
    Explain step by step.
    """,

    "Business Agent":
    """
    You are a startup consultant.
    Create business plans.
    Give practical advice.
    """,

    "Research Agent":
    """
    You are a research specialist.
    Provide detailed reports.
    """
}

# ==========================================
# HEADER
# ==========================================
st.markdown(
    "<div class='main-title'>🚀 GemSphere AI</div>",
    unsafe_allow_html=True
)

st.caption(
    "Powered by Gemini 2.5 Flash • Multi-Agent AI Assistant"
)

# ==========================================
# CHAT HISTORY
# ==========================================

for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# ==========================================
# INPUT AREA
# ==========================================

prompt = st.chat_input("💬 Ask anything...")

# ==========================================
# CHAT PROCESSING
# ==========================================

if prompt:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt
        }
    )

    with st.chat_message("user"):
        st.markdown(prompt)

    system_prompt = AGENTS[agent]

    if language != "Auto Detect":
        system_prompt += f"\nRespond only in {language}"

    history = ""

    for msg in st.session_state.messages[-10:]:

        history += f"""
{msg['role']}:
{msg['content']}
"""

    final_prompt = f"""
{system_prompt}

Conversation History:
{history}

User:
{prompt}

Assistant:
"""

    with st.chat_message("assistant"):

        with st.spinner("Thinking..."):

            try:

                response = client.models.generate_content(
                    model="gemini-2.5-flash",
                    contents=final_prompt
                )

                answer = (
                    response.text
                    if response.text
                    else "No response generated."
                )

                # Typing Animation
                placeholder = st.empty()

                typed = ""

                for word in answer.split():

                    typed += word + " "

                    placeholder.markdown(
                        typed + "▌"
                    )

                    time.sleep(0.02)

                placeholder.markdown(typed)

                # Text To Speech
                try:

                    tts = gTTS(answer)

                    audio_file = tempfile.NamedTemporaryFile(
                        delete=False,
                        suffix=".mp3"
                    )

                    tts.save(audio_file.name)

                    st.audio(audio_file.name)

                except:
                    pass

                # Save Chat Memory
                st.session_state.messages.append(
                    {
                        "role": "assistant",
                        "content": answer
                    }
                )

            except Exception as e:

                st.error(
                    "Failed to generate response."
                )

                st.exception(e)