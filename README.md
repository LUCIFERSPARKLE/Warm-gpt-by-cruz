# 🧬 WormGPT — Dark Mode Edition

A high-performance, multi-language Telegram AI chatbot built with Python and `python-telegram-bot` v21+, powered by OpenRouter (DeepSeek-V3).

> ⚠️ Educational & experimental project. Use responsibly.

---

## ✨ Features

| Feature | Description |
|---------|-------------|
| 🧠 **AI Powered** | DeepSeek-V3 via OpenRouter — fast & smart |
| 💬 **Conversation Memory** | Bot remembers context (up to 20 messages) |
| 🌐 **Multi-Language** | 🇺🇸 English · 🇮🇩 Indonesian · 🇮🇳 Hindi · 🇵🇰 Urdu |
| ⚡ **Fully Async** | Non-blocking httpx — handles 100+ users |
| 🔐 **Force Join** | Require users to join your channel first |
| 🛡️ **Anti-Flood** | Built-in slowmode (2 sec) per user |
| 📊 **User Stats** | `/stats` command shows usage info |
| 🧹 **Reset Chat** | `/reset` clears conversation history |
| 🏓 **Ping/Latency** | `/ping` for bot latency check |
| 📖 **Help Menu** | `/help` shows all bot commands |
| 🔧 **Easy Deploy** | Railway / VPS / Replit compatible |

---

## 📂 Project Structure

```
WormGPT/
├── main.py              # Entry point (loads .env, starts bot)
├── telegram_bot.py      # Core bot logic
├── keep_alive.py        # Flask keep-alive server
├── system-prompt.txt    # Custom system prompt
├── wormgpt_config.json  # Optional advanced config
├── requirements.txt     # Dependencies
├── .env.example         # Environment template
├── .gitignore           # Git ignore rules
├── railway.toml         # Railway deployment config
└── README.md            # This file
```

---

## 🔧 Installation

### 1. Clone & Setup

```bash
git clone https://github.com/OGAbdulOfficial/WormGPT.git
cd WormGPT
pip install -r requirements.txt
```

### 2. Configure Environment

```bash
cp .env.example .env
# Edit .env with your actual values
```

### 3. Run

```bash
python main.py
```

---

## 🔑 Environment Variables

| Variable | Required | Description |
|----------|----------|-------------|
| `TELEGRAM_TOKEN` | ✅ | Bot token from @BotFather |
| `OPENROUTER_KEY` | ✅ | API key from openrouter.ai |
| `MODEL_NAME` | ❌ | AI model (default: `deepseek/deepseek-chat`) |
| `API_BASE_URL` | ❌ | API endpoint (default: OpenRouter) |
| `REQUIRED_CHANNEL` | ❌ | Force-join channel username |

---

## 🤖 Bot Commands

| Command | Description |
|---------|-------------|
| `/start` | Welcome message + language selection |
| `/help` | Show all available commands |
| `/setlang en\|id\|hi\|ur` | Change response language |
| `/reset` | Clear conversation history |
| `/stats` | View your usage statistics |
| `/ping` | Check bot response latency |

---

## 🚀 Deploy on Railway

1. Push this repo to GitHub
2. Create a new Railway service → Deploy from GitHub
3. Add environment variables (`TELEGRAM_TOKEN`, `OPENROUTER_KEY`)
4. Deploy ✅

---

## 🧾 Requirements

```
python-telegram-bot==21.5
httpx>=0.27.0
python-dotenv>=1.0.0
flask>=3.0.0
```

---

## 🧧 Credits

- **Development**: AbdulDev (@AbdulBotzOfficial)
- **AI Provider**: [OpenRouter.ai](https://openrouter.ai)
- **Model**: DeepSeek Chat V3
- **Framework**: [python-telegram-bot](https://python-telegram-bot.org)

> ⚠️ Please do not remove credits. Respect open-source ethics.

---

## ❤️ License

MIT License — Free to fork, modify, and improve. Attribution required.
