# Event Recommender Bot (LangChain + Telegram)

This is a Minimum Viable Product (MVP) of a chatbot that helps users discover and get notified about events based on their preferences. The bot runs on Telegram and is powered by an open-source LLM (Mistral via Ollama) with LangChain for natural language understanding.

---

## 🔧 Features

- Understands user preferences via natural language
- Stores preferences and city using a local SQLite DB
- Checks for upcoming events every 6 hours
- Sends notifications via Telegram when matching events are found

---

## 🚀 Tech Stack

- **LangChain** (`langchain`, `langchain_community`, `langchain_ollama`)
- **Python Telegram Bot** (`python-telegram-bot`)
- **Ollama** (runs local Mistral model)
- **FastAPI (optional)** for future API expansion
- **SQLite** for storing user data
- **APScheduler** for scheduled event checks

---

## 📁 Project Structure

event_bot_mvp/
├── app/
│ ├── bot.py # Telegram interaction
│ ├── db.py # User and preference DB
│ ├── llm_agent.py # LangChain + Ollama logic
│ ├── event_checker.py # Notifier and scheduler
│ └── events.json # Sample event dataset
├── main.py # Entry point
├── requirements.txt # Dependencies
└── README.md


---

## ⚙️ Setup Instructions

### 1. Clone the Repository

git clone https://github.com/your-username/event-bot-mvp.git
cd event-bot-mvp

### 2. Create Virtual Environment

python -m venv venv
venv\Scripts\activate     # On Windows

### 3. Install Requirements

pip install -r requirements.txt

### 4. Install Ollama & Model
Download from https://ollama.com

Then:


ollama pull mistral

### 5. Set Telegram Token (PowerShell)

$env:TELEGRAM_TOKEN = your-telegram-bot-token


Run the Bot

python main.py

🧪 Example Usage
User says:

I love food festivals and music concerts in Bangalore.

Bot replies:

Got it! I’ll notify you when matching events happen in Bangalore.

