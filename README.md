# RAG Project
This project is 

## Requirements
- Python 3.11.5 or later

## Installation

### Install requieed packages
```bash
$ pip install -r requirements.txt
```

### Set up the environment variables
```bash
$ copy .env.example .env
```

Set enviroment variable in the `.env` file, such as `OPENAI_API_KEY` value

## Run Docker Compose Services
```bash
$ cd docker
$ copy .env.example .env
```

Then update .env with your credentials

## Run the FastAPI server
```bash
$ uvicorn main:app --reload --host 0.0.0.0 --port 5000
```
