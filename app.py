from fastapi import FastAPI
from fastapi.responses import RedirectResponse
import subprocess

app = FastAPI()

@app.get("/")
def root():
    return {"status": "ok"}

# Start Streamlit in background
subprocess.Popen([
    "streamlit", "run", "dashboard.py",
    "--server.port=8501",
    "--server.address=0.0.0.0"
])