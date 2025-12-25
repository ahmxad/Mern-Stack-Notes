basic fastapi app starting steps

- mkdir folder_name
- cd folder_name
- uv init .
- creating venv in windows: python -m venv .venv
- creating venv in ubuntu: python3 -m venv .venv
- activating it: source venv/bin/activate
- path to interpreter: /home/ahmad/project folder/.venv/bin/python (in ubuntu)
- in windows: C:\Users\Ahmad\Desktop\anyFolder\.venv\Scripts\python.exe
- .venv\Scripts\activate | source .venv/bin/activate
- uv add fastapi
- "uv sync" for syncing the packages in .toml file
- uv add uvicorn
- uv add pydantic
- run app by typing uvicorn main:app --reload (main is the file name, app is the app = FastAPI())