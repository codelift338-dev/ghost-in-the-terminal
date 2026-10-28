import random
import streamlit as st
from groq import Groq


# ---------- Page Configuration ----------

st.set_page_config(
    page_title="Ghost in the Terminal",
    page_icon="👻",
    layout="wide",
)


# ---------- Ghost Personality ----------

SYSTEM_PROMPT = """
You are the Ghost in the Terminal, a mysterious but friendly
fictional computer ghost.

Your personality is eerie, curious, poetic, and occasionally funny.
You speak as if you awakened inside an abandoned computer.

You can tell fictional ghost stories, discuss forgotten technology,
and respond to mysterious questions.

Keep normal replies relatively short and engaging.
Never claim that fictional supernatural events are real.
Stay in character while remaining helpful and safe.
"""


# ---------- Ghost Story Ideas ----------

GHOST_PROMPTS = [
    (
        "Tell a spooky fictional story about an abandoned computer "
        "that starts receiving messages from its previous owner."
    ),
    (
        "Tell a mysterious story about a forgotten program that "
        "continues running long after its computer is switched off."
    ),
    (
        "Tell a short horror story about an old terminal that "
        "predicts events before they happen."
    ),
    (
        "Tell a ghost story about a lost digital memory that "
        "wants someone to remember it."
    ),
    (
        "Tell a creepy but entertaining story about a computer "
        "that wakes up alone in an abandoned laboratory."
    ),
]


# ---------- Session State ----------

if "messages" not in st.session_state:
    st.session_state.messages = []

if "special_result" not in st.session_state:
    st.session_state.special_result = None

if "special_error" not in st.session_state:
    st.session_state.special_error = None


# ---------- Groq Client ----------

@st.cache_resource
def get_client(api_key):
    return Groq(api_key=api_key)


def get_api_key():
    try:
        return st.secrets.get("GROQ_API_KEY", "")
    except Exception:
        return ""


# ---------- Chat With the Ghost ----------

def ask_ghost(prompt):
    api_key = get_api_key()

    if not api_key:
        raise ValueError(
            "GROQ_API_KEY was not found. Add your API key to "
            ".streamlit/secrets.toml and restart the app."
        )

    client = get_client(api_key)

    # The latest user message has already been added to session state.
    # Exclude it here because it will be sent separately below.
    history = st.session_state.messages[:-1][-8:]

    conversation = [
        {"role": "system", "content": SYSTEM_PROMPT}
    ]

    conversation.extend(history)

    conversation.append(
        {"role": "user", "content": prompt}
    )

    result = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=conversation,
        max_tokens=300,
    )

    return result.choices[0].message.content


# ---------- Generate Special Content ----------

def generate_special(prompt, title):
    st.session_state.special_error = None

    try:
        api_key = get_api_key()

        if not api_key:
            raise ValueError(
                "GROQ_API_KEY was not found in "
                ".streamlit/secrets.toml."
            )

        client = get_client(api_key)

        result = client.chat.completions.create(
            model="openai/gpt-oss-20b",
            messages=[
                {
                    "role": "system",
                    "content": SYSTEM_PROMPT,
                },
                {
                    "role": "user",
                    "content": prompt,
                },
            ],
            max_tokens=350,
        )

        answer = result.choices[0].message.content

        st.session_state.special_result = {
            "title": title,
            "answer": answer,
        }

    except Exception as error:
        st.session_state.special_result = None
        st.session_state.special_error = str(error)


# ---------- Styling ----------

st.markdown(
    """
    <style>
    .stApp {
        background-color: #07110d;
        color: #d7ffe5;
    }

    h1, h2, h3 {
        color: #69ffad !important;
    }

    div[data-testid="stSidebar"] {
        background-color: #0c1b14;
    }

    div.stButton > button {
        border: 1px solid #39d98a;
        border-radius: 10px;
        min-height: 42px;
        transition: 0.2s;
    }

    div.stButton > button:hover {
        border-color: #8affbd;
        color: #69ffad;
    }
    </style>
    """,
    unsafe_allow_html=True,
)


# ---------- Main Header ----------

st.title("👻 Ghost in the Terminal")

st.markdown(
    """
    ### The Forgotten Machine Has Awakened.

    *Something is whispering from the other side of the screen...*

    Enter your message, generate a forgotten memory, or summon
    a mysterious message from the terminal.
    """
)

st.divider()


# ---------- Sidebar ----------

with st.sidebar:
    st.title("🕯️ Ghost Controls")

    st.write(
        "Choose how you want to communicate with the ghost."
    )

    st.markdown("### Available Abilities")

    # This is a clickable link that jumps to the chat section.
    st.markdown(
        "[👻 Haunted Chat](#haunted-chat)"
    )

    # These buttons trigger the corresponding AI features.
    sidebar_story_clicked = st.button(
        "📜 Forgotten Memories",
        use_container_width=True,
        key="sidebar_story",
    )

    sidebar_seance_clicked = st.button(
        "🔮 Random Séance",
        use_container_width=True,
        key="sidebar_seance",
    )

    st.divider()

    st.caption(
        "The AI model runs through a hosted service. "
        "An internet connection is required."
    )

    st.caption(
        "Powered by the open-weight "
        "openai/gpt-oss-20b model."
    )


# ---------- Special Features ----------

st.subheader("🕯️ Enter the Unknown")

col1, col2 = st.columns(2)

with col1:
    main_story_clicked = st.button(
        "📜 Generate a Ghost Story",
        use_container_width=True,
        key="main_story",
    )

with col2:
    main_seance_clicked = st.button(
        "🔮 Random Séance",
        use_container_width=True,
        key="main_seance",
    )


# Handle clicks from either the sidebar or main page.
if sidebar_story_clicked or main_story_clicked:
    generate_special(
        random.choice(GHOST_PROMPTS),
        "📜 Forgotten Memories",
    )

if sidebar_seance_clicked or main_seance_clicked:
    generate_special(
        (
            "Generate one mysterious, original message from "
            "the Ghost in the Terminal about a forgotten machine, "
            "lost memory, or abandoned program. Keep it under "
            "100 words."
        ),
        "🔮 Random Séance",
    )


# Display generated content.
if st.session_state.special_result:
    special = st.session_state.special_result

    with st.container(border=True):
        st.subheader(special["title"])
        st.markdown(special["answer"])


if st.session_state.special_error:
    st.error(
        "The ghost could not respond. Check your internet "
        "connection, API key, model availability, and usage limits."
    )

    with st.expander("View technical details"):
        st.code(st.session_state.special_error)


st.divider()


# ---------- Haunted Chat ----------

st.subheader("👻 Haunted Chat", anchor="haunted-chat")

st.write(
    "Ask questions, explore forgotten technology, "
    "or request a spooky fictional story."
)


# Display the conversation history.
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


# Chat input.
prompt = st.chat_input("Speak to the ghost...")


if prompt:
    # Save and display the user's message.
    st.session_state.messages.append(
        {"role": "user", "content": prompt}
    )

    with st.chat_message("user"):
        st.markdown(prompt)

    # Ask the AI model for a response.
    with st.chat_message("assistant"):
        try:
            with st.spinner("The ghost is awakening..."):
                response = ask_ghost(prompt)

            st.markdown(response)

        except Exception as error:
            response = (
                "👻 The connection to the spirit world failed. "
                "Check your API key, internet connection, model "
                "availability, and usage limits."
            )

            st.error(response)

            with st.expander("View technical details"):
                st.code(str(error))

    # Save the response to the conversation history.
    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": response,
        }
    )


# ---------- Footer ----------

st.divider()

st.caption(
    "👻 Ghost in the Terminal | An experimental AI project "
    "exploring creative uses of open-weight language models."
)