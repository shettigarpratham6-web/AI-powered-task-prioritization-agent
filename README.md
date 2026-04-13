# 🚀 AI Task Prioritization Agent (LLM Powered)

Transform messy task lists into clear, actionable priorities using the power of Large Language Models.

---

## 📌 Overview

This project is an AI-powered task management tool that automatically categorizes unstructured tasks into:

* 🔴 High Priority
* 🟡 Medium Priority
* 🟢 Low Priority

It leverages **LLMs** to simulate intelligent decision-making — turning raw text into structured outputs that improve productivity and planning.

---

## ⚡ Key Features

* 🧠 **LLM-Based Classification** — Uses advanced language models for intelligent prioritization
* 📂 **Unstructured Input Handling** — Accepts raw task lists (no formatting needed)
* 🧩 **Modular Code Design** — Clean separation of reading, processing, and output
* 🔐 **Secure API Handling** — Environment-based key management using dotenv
* ⚡ **Fast Inference** — Powered by Groq for low-latency responses

---

## 🛠️ Tech Stack

* Python
* Groq API
* LLaMA 3.1 Model
* Prompt Engineering
* python-dotenv

---

## 🧠 How It Works

1. Read tasks from a text file
2. Send tasks to LLM with a structured prompt
3. Model analyzes and categorizes tasks
4. Output is formatted into priority buckets

---

## 📥 Input Example

```
Finish assignment
Buy groceries
Watch Netflix
Prepare for exam
```

---

## 📤 Output Example

```
High Priority:
- Finish assignment
- Prepare for exam

Medium Priority:
- Buy groceries

Low Priority:
- Watch Netflix
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/ai-task-prioritizer.git
cd ai-task-prioritizer
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Set Environment Variables

Create a `.env` file in the root directory:

```
GROQ_API_KEY=your_api_key_here
```

---

## ▶️ Run the Project

```bash
python main.py
```

---

## 📁 Project Structure

```
📦 ai-task-prioritizer
 ┣ 📜 main.py
 ┣ 📜 tasks.txt
 ┣ 📜 requirements.txt
 ┗ 📜 README.md
```

---

## 🚧 Future Improvements

* 🌐 Web Interface (React + FastAPI)
* 📅 Deadline-aware prioritization
* 📊 Task analytics & insights
* 🗂️ Database integration
* 🧾 Export results (PDF / CSV)

---

## 💡 Learning Outcomes

* Practical integration of LLM APIs
* Prompt engineering for structured outputs
* Clean Python project architecture
* Real-world AI application development

---



---

## 🌟 Support

If you found this useful, consider giving it a ⭐ on GitHub!

---
