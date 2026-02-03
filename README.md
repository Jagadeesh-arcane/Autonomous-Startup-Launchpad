
---

```markdown
# 🚀 Autonomous Startup Launchpad

An end-to-end, production-grade **Multi-Agent System (MAS)** that converts a simple startup idea into a structured business plan using autonomous AI agents.

This project is designed to run with **local LLMs via Ollama** — **no OpenAI API key required**.

---

## ✨ What This Project Does

Given a startup idea, the system automatically:

1. Performs **market research**
2. Generates **financial projections**
3. Creates a **go-to-market & content strategy**
4. Assembles a complete **business plan**
5. Allows the plan to be **downloaded as a PDF**

All of this is orchestrated using multiple specialized AI agents.

---

## 🧠 Architecture Overview

### Agents
- **Market Research Analyst**  
  Identifies target customers, problems, competitors, and market size.
- **Startup Financial Strategist**  
  Produces first-year financial projections and assumptions.
- **Content & Growth Marketer**  
  Creates a go-to-market and content marketing strategy.

### Technology Stack
- **CrewAI** – Multi-agent orchestration  
- **LiteLLM** – LLM provider abstraction  
- **Ollama** – Local LLM runtime  
- **Streamlit** – Web-based UI  
- **Pydantic v2** – Schema validation  
- **DuckDuckGo Search** – Market research tool  
- **ReportLab** – PDF generation  

---

## 📁 Project Structure


    autonomous-startup-launchpad/
    │
    ├── app.py                     # Streamlit UI
    ├── README.md                  # Project documentation
    ├── requirements.txt           # Python dependencies
    │
    ├── src/
    │   ├── main.py                # Crew execution entry point
    │   ├── crew.py                # Task and agent orchestration
    │   │
    │   ├── agents/
    │   │   ├── market_researcher.py
    │   │   ├── financial_strategist.py
    │   │   └── content_marketer.py
    │   │
    │   ├── tools/
    │   │   ├── llm.py             # Ollama + LiteLLM configuration
    │   │   └── web_tools.py       # DuckDuckGo market search tool
    │   │
    │   ├── utils/
    │   │   └── pdf_generator.py   # Business plan PDF generator
    │   │
    │   └── config/
    │       └── settings.py        # Model and configuration values
    │
    └── venv/                      # Virtual environment (ignored by git)


## ⚙️ Setup Instructions

### 1️⃣ Create a Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate   # Windows
````

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Install and Run Ollama

```bash
ollama pull llama3
ollama serve
```

### 4️⃣ Start the Application

```bash
streamlit run app.py
```

---

## 🖥️ How to Use the App

1. Open the Streamlit app in your browser
2. Enter a startup idea (for example:
   *“A mobile app that helps small retail shop owners track daily sales using voice input”*)
3. Click **Generate Business Plan**
4. Review the generated content
5. Click **Download PDF** to save the plan
6. Use **Reset** to start over

---

## 🔒 No OpenAI API Key Required

* The system uses **Ollama locally**
* No external LLM APIs are required
* All AI inference runs on your machine
* Only web search requires internet access

---

## 🧩 Design Notes

* Tool schemas are intentionally **relaxed** to handle imperfect LLM tool calls
* Agent retry limits prevent infinite execution loops
* All agent outputs are normalized to plain strings before UI or PDF usage
* Streamlit session state is used to avoid unnecessary re-execution

---

## 🚀 Future Enhancements

* Structured **10-page business plan** using Pydantic models
* Human-in-the-loop approval steps
* DOCX export
* Agent memory and long-term context
* Async agent execution
* Charts and visuals in PDF output

---

## 👤 Author

Built as a learning-focused, production-style AI system demonstrating modern
multi-agent architectures with local LLMs.

---

## 📜 License

MIT License
