## 🧠 MCP Architecture Overview

This project uses the **MCP (Multi-Component Platform)** system to modularly manage tools, context, and prompts across servers, clients, and host agents. Below is a complete breakdown of how the components interact.

---

### 📦 Key Components

| Component     | Description |
|--------------|-------------|
| **MCP Server**  | Stores shared tools, context (memory), and prompt templates. It does **not execute** tools. |
| **MCP Client**  | Lives inside the Host App. Connects to MCP Server and **pulls in** tools, context, and prompts. |
| **Host App**    | The actual app that runs the **agent**, handles user interaction, and **executes tools** received via MCP Client. |

---

### 🔗 Architecture Flow

```txt
[ MCP Server ]
   ├── Tools
   ├── Contexts
   └── Prompts
       |
       ▼
[ MCP Client in Host App ]
   └── Pulls tools/context/prompts from server
       |
       ▼
[ Agent in Host App ]
   ├── Receives user messages
   ├── Selects tool to run
   └── Executes tool using specified transport
