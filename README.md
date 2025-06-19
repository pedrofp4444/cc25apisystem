# 🧩 CoderCamp '25 API System

This project is a modular and extensible API system based on [FastAPI](https://fastapi.tiangolo.com/), configurable via JSON files, with optional authentication and support for GET, POST, PUT, and DELETE. Its primary goal is to serve CoderCamp '25 and related projects.

---

## 🚀 Running Locally

### Prerequisites:
- Python 3.10+
- [Uvicorn](https://www.uvicorn.org/)
- [FastAPI](https://fastapi.tiangolo.com/)

### Install dependencies:

```bash
make install
```

### Run with hot-reload:

```bash
# Without authentication
make run PORT=8000

# With authentication
make run PORT=8000 AUTH_ON=true
```

---

## 🐳 Docker

### Build the image:

```bash
make build
```

### Run the container:

```bash
# Without authentication
make docker-run PORT=8000

# With authentication
make docker-run AUTH_ON=true PORT=8000
```

---

## 🔐 Authentication

* When `AUTH_ON=true`, all routes require `?token=abc123` (or another token defined in `config.py`).
* When `AUTH_ON=false`, authentication is ignored.

Valid tokens are defined in `config.py`.

### ⚙️ Environment Variables

This project uses a `.env` file to keep credentials and sensitive settings out of the codebase.

Create a `.env` file by copying the contents of the `.env.example` file:

> ❗ This file is included in `.gitignore` for security.

---

## 📁 Structure

```
cc25apisystem/
│
├── main.py               # FastAPI server
├── routes.json           # Route configuration file
├── config.py             # Settings like AUTH_ON and valid tokens
├── auth.py               # Token authentication middleware
├── handlers/             # Individual handler modules
│   └── (...)
├── scaffold.py           # Script to create handlers and update routes.json
├── requirements.txt
├── Dockerfile
├── Makefile
└── README.md
```

---

## ➕ Create New Routes with the Scaffold

Use the command below to create a new handler and automatically add it to `routes.json`.

```bash
make scaffold
```

### Example input:

```text
Route name: /users
HTTP Methods: GET,POST
```

This command:

* Creates the file `handlers/users.py` with a default function.
* Updates `routes.json` with the new route.

---

## 📞 Usage Examples

```http
GET http://localhost:47326/tempo?cidade=Guarda&token=dojo
```
