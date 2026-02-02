# 🤖 Multi-Agent MCP Chatbot (FastMCP + Python)

A simple **Multi-Agent chatbot** built using **FastMCP** that demonstrates how an agent can call server-side tools over HTTP. The project shows how to:

- Create and register MCP tools
- Build an async chat agent
- Pass user input (like a name) to tools
- Get structured responses back from the MCP server

This is a great starting point for **tool-based agents**, **MCP architecture**, and **agent-to-server communication**.

---

## 🧱 Architecture Overview

```
User Input
   ↓
ChatAgent (client)
   ↓  call_tool()
FastMCP Server (HTTP)
   ↓
Tool Function (get_user_info)
   ↓
Response back to Agent
```

---

## 📁 Project Structure

```
.
├── agents/
│   ├── chat_agent.py   # Chat agent that calls MCP tools
│   ├── time_agent.py   # Time agent that calls MCP tools
│   └── orchestrator_agent.py  # It routes intent to the right agent
├── server.py        # FastMCP server with tool definitions
├── client.py       # CLI client to interact with the agent
├── .env             # Environment variables (optional)
├── requirements.txt
├── README.md        # Project documentation
```

---

## ⚙️ Prerequisites

- Python **3.10+** (tested with 3.12)
- pip
- Virtual environment (recommended)

---

## 📦 Installation

### 1️⃣ Create and activate a virtual environment

```bash
python -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows
pip install -r .\requirements.txt
```

### 2️⃣ Install dependencies

```bash
pip install fastmcp python-dotenv
```

---

## 🚀 Running the Project

### Step 1: Start the MCP Server

```bash
python server.py
```

Expected output:

```
Starting MCP server 'multi-agent-mcp' with transport 'http'
```

> ⚠️ Important: Restart the server every time you add or change a tool.

---

### Step 2: Run the Client

```bash
python client.py
```

You should see:

```
🤖 Multi-Agent MCP Chatbot (type 'exit' to quit)
```

---

## 💬 Example Interaction

```
You: my name is Monika
Bot: Hello Monika! 👋 How can I help you today?
You: What time is it now?
Bot: 2026-02-02 10:21:51
You: Nice to meet you! Bye!
Bot: Nice to meet you! 😊
```

---

## 🌱 Future Enhancements

- 🧠 Add memory (store user names per session)
- 📄 Validate tool inputs with Pydantic schemas
- 🤝 Multiple agents with task delegation
- 🔐 Authenticated MCP server
- 🌐 Web UI instead of CLI

---

## 📚 References

- FastMCP Documentation
- MCP (Model Context Protocol) Concepts
- Async Python (`async` / `await`)

## Screenshot
<img width="365" height="157" alt="image" src="https://github.com/user-attachments/assets/a3017b75-bc9c-4a66-b634-935093520d0e" />
