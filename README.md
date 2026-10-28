# 👻 Ghost in the Terminal

### The Forgotten Machine Has Awakened.

What if an abandoned computer could speak?

**Ghost in the Terminal** is a spooky, interactive AI chatbot inspired by forgotten computers, lost digital memories, and mysterious abandoned programs. It combines a terminal-inspired interface with an AI-powered ghost that can chat with users, tell fictional horror stories, and generate mysterious messages.

Built with Python and Streamlit, this project explores how open-weight AI models can make creative AI applications accessible without requiring expensive computer hardware.

## ✨ Features

### 👻 Haunted Chat
Talk to a fictional computer ghost. Ask questions, explore forgotten technology, or start a mysterious conversation.

### 📜 Forgotten Memories
Generate original spooky stories about abandoned computers, lost programs, forgotten memories, and mysterious machines.

### 🔮 Random Séance
Summon a mysterious message from the ghost with a single click.

### 🕯️ Dark Interface
Explore a dark, terminal-inspired interface designed to create a mysterious atmosphere.

## 🛠️ Tech Stack

- **Python** — application logic
- **Streamlit** — interactive web interface
- **Groq Python SDK** — connection to the hosted AI model
- **`openai/gpt-oss-20b`** — open-weight language model
- **Groq-hosted inference** — runs the model remotely

The application uses a hosted inference service, so you do not need a dedicated GPU to run it locally.

## 🚀 Getting Started

Follow these instructions to run Ghost in the Terminal on your computer.

### Prerequisites

You will need:

- Python 3.10 or a compatible newer version
- An internet connection
- A Groq account and API key
- A terminal such as PowerShell, Command Prompt, or a Linux/macOS terminal

### 1. Clone the repository

Replace `YOUR_GITHUB_USERNAME` with your GitHub username.

```bash
git clone https://github.com/YOUR_GITHUB_USERNAME/ghost-in-the-terminal.git
cd ghost-in-the-terminal
```

### 2. Install the dependencies

```bash
python -m pip install -r requirements.txt
```

### 3. Configure your API key

Obtain an API key through the official [Groq Console](https://console.groq.com/).

Inside the project directory, create a folder named `.streamlit` if it does not already exist.

Inside that folder, create a file named `secrets.toml`.

Your project structure should look like this:

```text
ghost-in-the-terminal/
├── .streamlit/
│   └── secrets.toml
├── .gitignore
├── app.py
├── README.md
└── requirements.txt
```

Add the following to `.streamlit/secrets.toml`:

```toml
GROQ_API_KEY = "YOUR_GROQ_API_KEY"
```

Replace `YOUR_GROQ_API_KEY` with your actual API key.

**Security warning:** Never publish your API key, commit `secrets.toml`, or paste your key into public issues or discussions. The `.gitignore` file should exclude `.streamlit/secrets.toml`.

### 4. Launch the application

Run:

```bash
python -m streamlit run app.py
```

Streamlit will display a local address, usually:

```text
http://localhost:8501
```

Open that address in your browser and start talking to the ghost.

## 🧠 Why Open-Weight AI?

Open-weight models allow developers to experiment with AI systems and build applications around models whose weights are publicly available under their respective licenses.

This project demonstrates how an individual developer can use an open-weight language model to create an interactive AI experience without owning powerful AI hardware.

The application code can be inspected and adapted by other developers, while model inference is handled by a hosted provider.

**Important distinction:** Open-weight does not automatically mean unrestricted or fully open-source. Review the model's license and the provider's terms before redistributing or deploying the project.

## 🌍 Open Innovation

Ghost in the Terminal explores a simple idea: creative AI development should not require an expensive computer.

By combining accessible Python tools, a hosted inference API, and an open-weight language model, the project provides a starting point for developers who want to experiment with conversational AI.

The project can be extended with additional personalities, story-generation modes, persistent memories, or other creative features.

## ⚠️ Limitations

- **Internet required:** AI responses depend on a working internet connection.
- **Hosted inference:** Prompts are sent to the inference provider to generate responses.
- **API limits:** Availability and usage limits depend on the provider and account.
- **No offline inference:** The application does not currently run the language model entirely on the user's computer.
- **AI-generated content:** Responses may be inaccurate, repetitive, or unexpected.
- **Privacy:** Do not enter passwords, API keys, personal information, or confidential data into the chatbot.

## 🔮 Future Improvements

Potential future enhancements include:

- More ghost personalities and interactive story modes
- Downloadable generated stories
- Optional conversation export
- Improved interface animations and sound effects
- A publicly accessible hosted demo
- Support for additional compatible language models

## 🎃 The Story Behind the Project

The idea is simple: imagine an old computer left forgotten in a dark room. Its programs have been abandoned, its memories have faded, but something is still running.

One day, the terminal begins to answer.

Is it a bug, a memory, or just a clever language model?

You decide.

## 📜 License

No license for this application's source code has been declared in this repository yet.

Before redistributing or reusing the code, add an appropriate project license. The underlying model and hosted inference service have their own terms, which are separate from the application's license.

---

**Built with Python, Streamlit, and open-weight AI.**

*The machine remembers. The terminal whispers. The ghost is waiting.*