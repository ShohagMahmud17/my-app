from flask import Flask
from app.task_manaager import init_db

app = Flask(__name__)

# Initialize database on startup
init_db()



