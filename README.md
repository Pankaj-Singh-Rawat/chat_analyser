# 📊 WhatsApp Conversation Intelligence Dashboard

A production-ready Streamlit application that transforms raw WhatsApp chat exports into actionable insights and visual analytics.

---

## 🚀 Live Demo

👉 *Add your deployed link here (Streamlit Cloud)*

---

## 🧠 Problem Statement

WhatsApp chats contain rich behavioral and communication data, but are unstructured and difficult to analyze manually.
This project converts raw chat logs into structured insights such as activity trends, user behavior, and communication patterns.

---

## ⚙️ Features

### 📈 Core Analytics
- Total messages, words, media, and links
- User-wise message breakdown
- Most active users (chat participation %)

### 📅 Temporal Analysis
- Monthly timeline of messages
- Time-based activity trends

### ☁️ Text Analysis
- WordCloud visualization
- Most common words (with stopword filtering)

### 😀 Emoji Analysis
- Emoji frequency distribution
- Pie chart visualization

### 👥 Multi-User Support
- Analyze individual users or overall group activity

### 🧪 Built-in Demo Mode
- Automatically loads sample chat if no file is uploaded

---

## 🏗️ Architecture

```
User Input (File / Sample Data)
         ↓
Preprocessing Layer (Regex + Parsing)
         ↓
Feature Engineering (Time, Users, Messages)
         ↓
Analytics Layer (Helper Functions)
         ↓
Visualization Layer (Streamlit + Matplotlib)
```

---

## 🛠️ Tech Stack

| Layer | Tool |
|---|---|
| Frontend / UI | Streamlit |
| Data Processing | Pandas |
| Visualization | Matplotlib |
| Text Analysis | WordCloud |
| Utilities | URLExtract, Emoji |

---

## 📂 Project Structure

```
chat-analyser/
│
├── app.py                # Streamlit app (UI layer)
├── preprocessor.py       # Data parsing & feature extraction
├── helper.py             # Analytics & computations
├── sample_chat.txt       # Demo dataset
├── stop_hinglish.txt     # Stopwords for filtering
└── requirements.txt      # Dependencies
```

---

## 📥 Input Format

The app expects a WhatsApp exported chat in the following format:

```
12/09/25, 20:40 - User: Message
```

To export a chat from WhatsApp:
1. Open a chat → Tap the three-dot menu → **More** → **Export chat**
2. Choose **Without Media** for faster processing
3. Upload the resulting `.txt` file to the app

---

## ▶️ How to Run Locally

```bash
# Clone the repository
git clone https://github.com/Pankaj-Singh-Rawat/chat-analyser.git
cd chat-analyser

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py
```

The app will open at `http://localhost:8501` in your browser.

---

## ☁️ Deploy on Streamlit Cloud

1. Push the repository to GitHub
2. Go to [streamlit.io/cloud](https://streamlit.io/cloud) and sign in
3. Click **New app** → select your repo, branch, and `app.py`
4. Click **Deploy** — your app will be live in minutes

---

## 📸 Screenshots

> *Add screenshots of the dashboard here*

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

1. Fork the repository
2. Create a new branch: `git checkout -b feature/your-feature`
3. Commit your changes: `git commit -m 'Add your feature'`
4. Push to the branch: `git push origin feature/your-feature`
5. Open a Pull Request

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

## 🙋‍♂️ Author

Built with ❤️ — feel free to connect or raise an issue if you have questions!
