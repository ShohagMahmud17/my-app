from flask import Flask
from models import init_db

app = Flask(__name__)

# Initialize database on startup
init_db()



