from flask import Flask
import os

random_key = os.urandom(255)

app = Flask(__name__)

app.secret_key = random_key