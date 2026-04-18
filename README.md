# 🌍 Multilingual AI Chatbot

Build your own ChatGPT-like chatbot in 15 minutes! Supports 8+ languages and runs completely FREE.

## ✨ Features

- 🌐 8 Languages (English, Spanish, French, German, Hindi, Japanese, Chinese, Arabic)
- 💬 Multiple Chat Histories
- ⚡ Lightning Fast (Groq API)
- 💰 100% FREE

## 🚀 Quick Start

### 1. Install

```bash
git clone https://github.com/yourusername/multilingual-chatbot.git
cd multilingual-chatbot
pip install groq streamlit
```

### 2. Get API Key

- Go to [console.groq.com](https://console.groq.com)
- Sign up (FREE, no credit card)
- Create API key
- Copy it

### 3. Add Your Key

Open `backend.py` and paste your key:
```python
self.client = Groq(api_key="paste_your_key_here")
```

### 4. Run

```bash
streamlit run ui.py
```

That's it! Open `http://localhost:8501` in your browser.

## 📁 Files

```
backend.py  → AI logic
ui.py       → User interface
```

## 🎨 Customize

**Add languages:** Edit the language list in `ui.py`

**Change AI personality:** Modify system message in `backend.py`

**Different model:** Change model name to `llama-3.1-8b-instant` for faster responses

## 🐛 Common Issues

**"Module not found"** → Run: `pip install groq streamlit`

**"Invalid API key"** → Get new key from console.groq.com

**"Model error"** → Use: `llama-3.3-70b-versatile`

## 🎥 Tutorial

Full video tutorial: [Watch on YouTube](https://www.youtube.com/watch?v=J8lGuK3Iv1E)

## 📝 License

MIT License - Free to use for any project!

---

⭐ Star this repo if you found it helpful!