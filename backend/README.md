# Navegue para o diretório backend

```bash
cd backend
```

# Crie um ambiente virtual

```bash
python -m venv .venv
```

# Ative o ambiente virtual

```bash
source .venv/bin/activate # macOS/Linux
```

```bash
.\.venv\Scripts\Activate.ps1 # Windows PowerShell
```

```bash
.venv\Scripts\activate.bat # Windows Command Prompt
```

# Instale as dependências

```bash
pip install -r requirements.txt
```

# Executando a aplicação

```bash
python -m uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

# Ou execute diretamente

```bash
python -m app.main
```

# Instalando com Docker

```bash
# Usando Docker Compose (recomendado)
docker-compose up --build backend_api

# Ou usando Docker individual
docker build -t chat-backend
docker run -p 8000:8000 --env-file .env chat-backend
```
