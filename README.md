# 🤖 Multi-Agent Research System

An AI-powered **multi-agent research system** that automates the process of researching topics across the web.

The system combines **Tavily web search**, **BeautifulSoup web scraping**, and **LLM-powered agents** to search for relevant information, extract useful content, and generate a consolidated research response.

---

## 🚀 Overview

Traditional web research often requires manually searching multiple websites, opening articles, extracting important information, and combining the findings.

This project aims to automate that workflow using a **multi-agent architecture**.

Instead of relying on a single agent to perform every task, different agents are given specialized responsibilities.

### 🔎 Research Workflow

```text
                    User Query
                        │
                        ▼
                 ┌─────────────┐
                 │  Streamlit  │
                 │     UI      │
                 └──────┬──────┘
                        │
                        ▼
                 ┌─────────────┐
                 │  Research   │
                 │   Pipeline  │
                 └──────┬──────┘
                        │
              ┌─────────┴─────────┐
              ▼                   ▼
       ┌─────────────┐     ┌─────────────┐
       │   Search    │     │     Web     │
       │    Agent    │     │  Scraping   │
       │             │     │    Agent    │
       └──────┬──────┘     └──────┬──────┘
              │                   │
              ▼                   ▼
          Tavily API         BeautifulSoup
              │                   │
              └─────────┬─────────┘
                        ▼
                 ┌─────────────┐
                 │ Information │
                 │  Processing │
                 └──────┬──────┘
                        │
                        ▼
                 ┌─────────────┐
                 │     LLM     │
                 │  Response   │
                 └──────┬──────┘
                        │
                        ▼
                  Research Report
```

---

## ✨ Features

* 🔍 AI-powered web research
* 🌐 Web search using Tavily
* 🕷️ Web scraping using BeautifulSoup
* 🤖 Multiple specialized AI agents
* 🔄 Automated research pipeline
* 🧠 LLM-powered information processing
* 📊 Streamlit-based user interface
* 🔐 Environment-variable-based API key management
* 🧩 Modular project architecture

---

## 🛠️ Tech Stack

| Technology        | Purpose                                   |
| ----------------- | ----------------------------------------- |
| 🐍 Python         | Core programming language                 |
| 🤖 LangChain      | LLM and agent orchestration               |
| 🔎 Tavily         | Web search                                |
| 🕷️ BeautifulSoup | Web scraping                              |
| 🖥️ Streamlit     | User interface                            |
| 🔐 python-dotenv  | Environment variable management           |
| 🧠 LLM            | Research analysis and response generation |

---

## 📁 Project Structure

```text
multi-agent-research-system/
│
├── app.py
├── agents.py
├── pipeline.py
├── tools.py
├── requirements.txt
├── .gitignore
└── README.md
```

### `app.py`

Contains the Streamlit application and user interface.

### `agents.py`

Contains the AI agents responsible for different research tasks.

### `tools.py`

Contains the external tools used by the agents, including:

* Tavily search
* BeautifulSoup web scraping

### `pipeline.py`

Coordinates the research workflow and connects the different components of the system.

### `requirements.txt`

Contains the Python dependencies required to run the project.


---

## ▶️ Running the Application

### 1. Clone the repository

```bash
git clone https://github.com/garvitagupta12/multi-agent-research-system.git
```

### 2. Navigate to the project

```bash
cd multi-agent-research-system
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Start the application

```bash
streamlit run app.py
```

The application will open in your browser.

---

## 💡 Example Use Cases

This system can be used for:

* 🔬 Researching technical topics
* 📰 Gathering information from multiple web sources
* 📚 Collecting background information for projects
* 📊 Comparing information from different sources
* 🧠 Generating summarized research reports
* 🌐 Extracting useful information from web pages

### Example Query

```text
What are the latest applications of RAG in healthcare?
```

The system can:

1. Search the web for relevant sources.
2. Identify useful pages.
3. Scrape webpage content.
4. Process the collected information.
5. Generate a consolidated response.

---

## 🧠 Why Multi-Agent?

Instead of asking one agent to perform every task, this project separates responsibilities between specialized agents.

For example:

```text
Search Agent
      │
      ▼
Find relevant sources
      │
      ▼
Scraping Agent
      │
      ▼
Extract webpage content
      │
      ▼
Research Pipeline
      │
      ▼
LLM
      │
      ▼
Final Research Response
```

This modular architecture makes the system easier to understand, maintain, and extend.

---

## 🔮 Future Improvements

* [ ] Add a dedicated summarization agent
* [ ] Add conversation history
* [ ] Add research report export as PDF

---

## 👩‍💻 Author

**Garvita Gupta**

Building and learning GenAI projects with Python, LLMs, agents, and AI tools.

---

## ⭐ Contributing

Suggestions and improvements are welcome!

If you find this project useful, consider giving the repository a ⭐.
